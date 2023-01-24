import os
import cv2
import time
dataset = "surf"
file_dir='D:/video_SOD/datasets/'+dataset+'/images/'
list=[]
for root,dirs,files in os.walk(file_dir):
    for file in files:
       list.append(file)  #获取目录下文件名列表

video=cv2.VideoWriter('D:/video_SOD/datasets/'+dataset+'/'+ dataset +'.avi',cv2.VideoWriter_fourcc(*'MJPG'),10,(1280,720))  #定义保存视频目录名称及压缩格式，fps=10,像素为1280*720
for i in range(1,len(list)):
    img=cv2.imread(file_dir+list[i-1])  #读取图片
    img=cv2.resize(img,(1280,720)) #将图片转换为1280*720
    # print(img.shape)
    # print(type(img))
    video.write(img)   #写入视频

video.release()