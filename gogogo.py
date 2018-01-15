import os,time
from PIL import Image
from aip import AipOcr
from baiduai import Ai
import config






"""获取题目图片"""
def getImg():
    os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png")
    os.system("adb pull /sdcard/screenshot.png ./screenshot.png")
    im = Image.open(r"./screenshot.png")
    img_size = im.size
    w = im.size[0]
    h = im.size[1]
    print("xx:{}".format(img_size))
    region = im.crop((70,200, w-50,1200))    #裁剪的区域
    region.save(r"./crop_test1.png")


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def search():
    image = get_file_content(r"./crop_test1.png")
    client = AipOcr(config.APP_ID, config.API_KEY, config.SECRET_KEY)
    respon = client.basicGeneral(image)   #用完500次后可改 respon = client.basicAccurate(image) 这个还可用50次
    titles = respon['words_result']          #获取问题
    issue = ''
    answer = ['','','','','','']
    countone = 0
    answercount = 0
    for title in titles:
          countone+=1
          if(countone >=len(titles)-2):
            answer[answercount] = title['words']
            answercount+=1
          else:
            issue = issue +title['words']


    tissue = issue[1:2]
    if str.isdigit(tissue):            #去掉题目索引
         issue = issue[3:]
    else:
         issue = issue[2:]

    print(issue)       #打印问题
    print('  A:'+answer[0]+' B:'+answer[1]+' C:'+answer[2])       #打印答案

    ai=Ai(issue,answer)
    ai.search()




def main():
    print("开始答题后，输入回车继续，q退出：")
    while 1:

        if input().lower() == 'q':
            print("欢迎继续使用！")
            break
        start = time.time()
        getImg()
        search()
        end = time.time()
        print('本次用时用时：' + str(end - start) + '秒')

if __name__=="__main__":
    main()