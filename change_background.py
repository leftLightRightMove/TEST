import os
import cv2

dataset = "elephant"
background = "desert"
def change_back(img_ori, img_seg, img_back, name):
    # ret,img_seg = cv2.threshold(img_seg,191,1,cv2.THRESH_BINARY)
    img_seg = img_seg/255.0
    print(type(img_seg), type(img_ori))
    print(img_seg.shape, img_ori.shape)
    foreground = img_ori * img_seg
    img_final = foreground + (img_back*(1-img_seg))
    cv2.imwrite("D:/video_SOD/datasets/"+dataset+"/results/"+name+".jpg", img_final)
    # cv2.imshow("fore", foreground)
    # cv2.waitKey(0)
    # cv2.imshow("fore", img_final)
    # cv2.waitKey(0)

def img2video():
    file_dir='D:/video_SOD/datasets/'+dataset+'/results/'
    list=[]
    for root,dirs,files in os.walk(file_dir):
        for file in files:
            list.append(file)  #获取目录下文件名列表

    video=cv2.VideoWriter('D:/video_SOD/datasets/'+dataset+'/'+background+'.avi',cv2.VideoWriter_fourcc(*'MJPG'),10,(1280,720))  #定义保存视频目录名称及压缩格式，fps=10,像素为1280*720
    for i in range(1,len(list)):
        img=cv2.imread(file_dir+list[i-1])  #读取图片
        img=cv2.resize(img,(1280,720)) #将图片转换为1280*720
        video.write(img)   #写入视频

    video.release()

def main():
    img_path = "D:/video_SOD/datasets/"+dataset+"/images/"
    seg_path = "D:/video_SOD/datasets/"+dataset+"/segments/"
    back_path = "D:/video_SOD/datasets/backgrounds/"+background+".jpg"
    dirs = os.listdir(img_path)
    img_back = cv2.imread(back_path)
    begin = True
    count = 0
    for file in dirs:
        if count > 0:
            count -= 1
            continue
        name = file[:-4]
        # print(name)
        img_ori = cv2.imread(img_path+name+'.jpg')
        img_seg = cv2.imread(seg_path+name+'.png')
        if begin:
            x, y = img_ori.shape[0:2]
            print(x, y)
            img_back = cv2.resize(img_back, (y, x))
            begin = False
        change_back(img_ori, img_seg, img_back, name)
        # cv2.imshow(file+str(count), img_ori)
        # cv2.waitKey(0)
        # cv2.imshow("seg",img_seg)
        # cv2.waitKey(0)
        # cv2.imshow("back", img_back)
        # cv2.waitKey(0)

main()
img2video()