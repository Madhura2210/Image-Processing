

import cv2
import numpy as np
from Image_processing2 import Image_processing
img = np.zeros((512,512,3))
img[:,:,0]=225
import sys
#print("Sys module information ",sys.modules.keys())
if __name__=="__main__":
    obj = Image_processing(img)

    #cv2.namedWindow(winname="window")
    #cv2.setMouseCallback("window",obj.crop)
    #cv2.setMouseCallback("window",obj.draw)
    obj.capture_video()

    #while True:
        #cv2.imshow("window",img)
        #if cv2.waitKey(1) & 0XFF == ord('x'):
            #break

    #cv2.destroyAllWindows()









