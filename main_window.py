# 输出在第一次识别到人脸的时间
# 添加设置打卡截止时间
# 修改输出 迟到 信息
# 定义一个数组，存储已打卡的人员信息，从而实现输出信息的筛选

# 导入系统模块
import sys

# 导入一些PyQt5模块
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QTime,QDate

# 导入人脸数据
from face_data import *


# 导入opencv模块
# import cv2

from ui_main_window import *
# 创建MainWindow类
class MainWindow(QWidget):
    # 初始化函数
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.check_success = ["admin"]
        self.lastname = "NULL0"
        self.ui.dead_time.setTime(QTime(8,0,0))
        self.ui.label.setText("打卡截止时间：")
        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)
        self.ui.control_bt.clicked.connect(self.controlTimer)
        
        
    # 视频人脸识别处理
    def viewCam(self):
    	
        # 输出系统时间
        current_time = QTime.currentTime()
        time_string = current_time.toString()
        self.ui.time_label.setText(time_string)
       
        # 读取一个BGR格式的图像帧
        ret, raw_frame = self.cap.read()
    
        # 把图像帧缩小到1/4，从而实行更快的人脸识别处理
        small_frame = cv2.resize(raw_frame, (0, 0), fx=0.25, fy=0.25)
    
        # 把摄像头采集的BGR图像转换成RGB图像
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        if True :
            # 在视频当前帧中找到所有的脸部，并进行脸部信息编码
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            
            name = "NULL"
            
            for face_encoding in face_encodings:
                # 检测图像帧中的脸是否和已知的脸部信息匹配
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    
                # 将新的脸部信息和它的face_distances最接近的已知脸部信息匹配
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                # 设置匹配阈值，满足条件的就和已知信息匹配，如果不满足就设置成未知
                if face_distances[best_match_index] < 0.55 and matches[best_match_index]:
                    name = known_face_names[best_match_index]
                else:
                    name = "Unknown"
                        
                face_names.append(name)
   
      # 显示识别结果（用矩形框将识别到的人脸标记出来）
        for (top, right, bottom, left), name in zip(face_locations, face_names):        
            
            # 由于之前将图像帧缩小了1/4，现在将尺度放大四倍，以便和原始图片尺寸匹配
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            
            # 在图像帧中的人脸部位画标记框
            cv2.rectangle(raw_frame, (left, top), (right, bottom), (0, 0, 255), 2)
    
        # 将经过标记处理的原始图像帧从BGR格式转换成RGB格式
        frame = cv2.cvtColor(raw_frame, cv2.COLOR_BGR2RGB)
        
        # 获取图像帧信息
        height, width, channel = frame.shape
        step = channel * width

        # 将图像帧转换成pyqt可以显示的格式
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
    
        # 用pyqt显示图像帧
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))
        
        # (1)当视频帧中存在已知人脸且未打卡时，若打卡时间早于截止时间，输出打卡时间、人员姓名、打卡成功等信息；若打卡时间迟于截止时间，输出人员姓名、迟到等信息
        # (2)当视频帧中存在已知人脸且已打卡时，输出人员姓名、已打卡等信息
        # (3)当视频帧中存在未知人脸时，输出“未注册人脸信息”
        # (4)当视频帧中不存在人脸时，输出为空
        
        if(name == "NULL"):
            self.ui.textBrowser.clear()
            self.lastname = "NULL"
        elif(name == "Unknown"):
            self.ui.textBrowser.setText("未注册人脸信息")
            self.lastname = "Unknown"
        elif(name == self.lastname):
             self.lastname = name
        elif(name in self.check_success):
            self.ui.textBrowser.setText(name + "已打卡")
        else:
            # 判断当前打卡时间是否迟到
            dead_time = self.ui.dead_time.time()
            if (dead_time.hour()<current_time.hour()):
                isLate = 1
            elif (dead_time.hour()==current_time.hour() and dead_time.minute()<current_time.minute()):
                isLate = 1
            elif (dead_time.minute()==current_time.minute() and dead_time.second()<current_time.second()):
                isLate = 1
            else:
                isLate = 0
            
            # 如果isLate=1，输出迟到信息；如果isLate=01，输出打卡成功信息；
            if(isLate):
                self.ui.textBrowser.setText( name + "迟到")
            else:
                self.ui.textBrowser.setText(time_string + ":\n" + name + "打卡成功")
                self.check_success.append(name)
                self.lastname = name;

    # 通过点击按钮来控制开启/关闭定时器
    def controlTimer(self):
        # 当定时器停止时，按下按钮就打开摄像头、开启定时器、改变按钮的标识、输出日期信息
        if not self.timer.isActive():
            # 打开摄像头，0表示内置摄像头，1表示外接摄像头
            self.cap = cv2.VideoCapture(0)
            self.cap.set(3, 1280)
            self.cap.set(4, 720)
            # 开启定时器，定时时间为20ms
            self.timer.start(20)
            # 更改按钮标识
            self.ui.control_bt.setText("Stop")
            # 输出日期信息
            current_date = QDate.currentDate()
            self.ui.date_label.setText(current_date.toString("yyyy-MM-dd"))
        
        # 当定时器开启时，按下按钮就关闭定时器、关闭摄像头、更改按钮的标识
        else:
            # 关闭定时器
            self.timer.stop()
            # 关闭摄像头
            self.cap.release()
            # 更改按钮标识
            self.ui.control_bt.setText("Start")



if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建并显示窗口
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
    
    
