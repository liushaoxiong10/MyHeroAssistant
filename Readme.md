#百万英雄答题助手


# 用的是python3.6版本
使用adb截图。

# 把问题区域裁剪出来后用百度的ocr识别出文本，然后调用百度搜索（把搜索到的前两个答案显示在屏幕）
1,安装ADB 驱动，可以到[这里下载](https://adb.clockworkmod.com/)<br />
   安装 ADB 后，请在环境变量里将 adb 的安装路径保存到 PATH 变量里，确保 adb 命令可以被识别到
  
2.需要安装模块 在命令行输入(pip install -r requirements.txt) 

3.config.py里填写自己百度ocr的APPid</br>
百度ocr：http://ai.baidu.com/tech/ocr/general

4.连接手机<br>运行python gogogo.py (搜索百度的内容) 
