import cv2
import os
 
videos_path = r'D:\video_SOD\video/'
videos = os.listdir(videos_path)
for video_name in videos:
    file_name = video_name.split('.')[0] #视频文件名
    folder_name = videos_path + file_name
    os.makedirs(folder_name, exist_ok=True)#创建与视频同名目录保存截取的图片
    print(videos_path + video_name)
 
    video_path = videos_path + video_name #视频路径
 
    vc = cv2.VideoCapture(video_path)  # 读入视频文件，打开视频
    c = 0
    timeS = 20 # 视频帧计数间隔频率
    rval = vc.isOpened() #视频是否打开成功，返回true表示成功，false表示不成功
 
    while rval:  # 循环读取视频帧
        c = c + 1
        # cap.read()按帧读取视频，ret, frame是获cap.read()方法的两个返回值。
        # 其中ret是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False。
        # frame就是每一帧的图像，是个三维矩阵。
        rval, frame = vc.read()
        print(rval, frame)
        pic_path = folder_name + '//'  #图片保存目录
        if rval:#c%timeS==0：c除尽timeS时取帧保存，图片，即隔timeS保存一次图片
            pic_name = file_name + '_' + str(c) + '.jpg'
            cv2.imencode('.jpg', frame)[1].tofile(pic_path + pic_name)
            print(pic_path + pic_name)  # 打印生成的路径名
            cv2.waitKey(1)
            # cv2.waitKey()参数是1，表示延时1ms切换到下一帧图像，参数过大如cv2.waitKey(1000)，会因为延时过久而卡顿感觉到卡顿。
            # 参数为0，如cv2.waitKey(0)只显示当前帧图像，相当于视频暂停。
        else:
            break
    vc.release()