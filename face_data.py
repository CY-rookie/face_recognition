# 此文件采集人脸信息数据
# 采集过程包括(以含有人脸的“example.jpg”图片为例)：
# (1)将“example.jpg”图片face_data.py所在的文件夹
# (2)增加识别example.jpg的代码，并生成相应的人脸数据(example_face_encoding)
#    example_image = face_recognition.load_image_file("example.jpg")
#    example_face_encoding = face_recognition.face_encodings(example_image)[0]
# (3)将生成的 example_face_encoding数据存入known_face_encodings数据列表中
# (4)将图片中存在的人的名字存入known_face_names数据列表中（以字符串形式存入）

import face_recognition
import cv2
import numpy as np

# 识别obama图片
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# 识别biden图片
biden_image = face_recognition.load_image_file("biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# #可将下面的XX_image.jpg改成任意你所添加图片的名称，
# #并更改known_face_encodings和known_face_names中相应的XX，即可添加新的人脸数据
# # 识别XX图片，并编码成特征向量
# XX_image = face_recognition.load_image_file("XX_image.jpg")
# XX_image_face_encoding = face_recognition.face_encodings(XX_image)[0]

# 创建已识别的人脸信息编码向量和相应的姓名，编码向量和姓名的顺序保持一致
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding,
    XX
]
known_face_names = [
    "Barack Obama",
    "Joe Biden",
    "XX"
]

# 初始化一些变量参数
face_locations = []
face_encodings = []
face_names = []


