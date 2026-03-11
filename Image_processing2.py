# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import numpy as np

class Image_processing:
    def __init__(self,img):
        self.down_x = 0
        self.down_y = 0
        self.up_x = 0
        self.up_y = 0
        self.img=img

    #Draw shapes on an image
    def draw(self,event,x,y,flag,params):

        #img = params
        if event == cv2.EVENT_LBUTTONDOWN:
            self.down_y=y
            self.down_x =x
        elif event ==cv2.EVENT_LBUTTONUP:
            cv2.rectangle(self.img,pt1=(self.down_x,self.down_y),pt2=(x,y),color=(255,0,0),thickness=2)
        print("pt2 x is ",x)
        print("pt2 y is ",y)
        print("pt1 x is ",self.down_x)
        print("pt1 y is ",self.down_y)

    #Crop images and save them
    def crop(self,event,x,y,flag,params):

        if event == 1:
            self.down_x=x
            self.down_y=y
            flag = True
        #elif event == 0:
            #if flag == True:
                #cv2.rectangle(self.img,pt1=(self.down_x,self.down_y),pt2=(x,y),color=(0,0,255),thickness=1)
        elif event == 4:
            flag = False
            self.up_x=x
            self.up_y=y
            cv2.rectangle(self.img,pt1=(self.down_x,self.down_y),pt2=(x,y),color=(255,255,0),thickness=1)
            #cropping
            img_crop = self.img[self.down_y:self.up_y,self.down_x:self.up_x] # opencv works differently, y comes before x
            print()
            print("down x ",self.down_x)
            print("down y ", self.down_y)
            print("up x ", self.up_x)
            print("up y ", self.up_y)
            cv2.imshow("window_crop", img_crop)
            cv2.waitKey(0) #worked even without
        print("x ", x)
        print("y ", y)
    def capture_video(self):
        vid = cv2.VideoCapture(0)
        #creating writer object (screen recording object)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

        while True:
            ret, frame = vid.read()
            #screen recording code start:
            out.write(frame)
            vid_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow("window",vid_gray)

            if cv2.waitKey(1) & 0XFF==ord('x'):
                break
        out.release()# release object of writing.
        cv2.destroyAllWindows()









# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
