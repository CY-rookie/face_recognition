项目名称：基于人脸识别的打卡签到系统

此系统在树莓派4上搭配摄像头运行

程序运行说明如下：
1. 首先安装所需的函数库dlib、face_recognition、opencv、pyqt5
   pip3 install libdlib-dev
   pip3 install face_recognition
   sudo apt install python3-opencv
   sudo apt install pyqt5
2. 用python指令运行文件夹中的main_window.py文件以启动程序：python3 ./main_window.py
3. 在打开窗口中的“打卡截止时间”后面的时间框中修改设置系统的打卡截止时间，默认截止时间是8:00:00；
   若要修改时间，请在开启系统之前进行；系统启动后若要修改时间，请退出后重新运行程序
4. 在打开的窗口中点击“start”按钮开启打卡系统
   (1)当视频帧中存在已知人脸且未打卡时，若打卡时间早于截止时间，输出打卡时间、人员姓名、打卡成功等信息；若打卡时间迟于截止时间，输出人员姓名、迟到等信息；
   (2)当视频帧中存在已知人脸且已打卡时，输出人员姓名、已打卡等信息；
   (3)当视频帧中存在未知人脸时，输出“未注册人脸信息”；
   (4)当视频帧中不存在人脸时，输出为空；
5. 系统运行时，点击窗口中“stop”按钮，可以让系统停止工作；

6. 关于main_window.py文件说明：
   此文件包含系统运行所需要的函数，包括初始化函数__init__()、视频人脸识别处理函数viewCam()和按钮功能函数controlTimer()

6. 关于face_data.py文件说明：
   此文件采集人脸信息数据
   采集过程包括(以含有人脸的“example.jpg”图片为例)：
   (1)将“example.jpg”图片face_data.py所在的文件夹
   (2)增加识别example.jpg的代码，并生成相应的人脸数据(example_face_encoding)
      example_image = face_recognition.load_image_file("example.jpg")
      example_face_encoding = face_recognition.face_encodings(example_image)[0]
   (3)将生成的 example_face_encoding数据存入known_face_encodings数据列表中
   (4)将图片中存在的人的名字存入known_face_names数据列表中（以字符串形式存入）

7. 关于ui_main_window.ui文件说明
   此文件是用pyqt5生成程序操作界面的文件

8. 关于ui_main_window.py文件说明
   此文件是ui_main_window.ui经过编译之后得到的文件，导入main_window.py程序中，可以将程序功能和界面相应控件进行连接，实现可视化操作
