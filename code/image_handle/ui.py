from typing import Optional
import cv2 as cv
import numpy as np

class CVUiHandler:
    def __init__(self,**kwargs):
        pass
    
    def create_window(self,name : str ='window'):
        cv.namedWindow(name)
        #three values that will be interpreted as blue, green, and red color components (in that order) from the [0, 255] range
        fill_val = np.array([255, 255, 255], np.uint8)

        def trackbar_callback(idx, value):
            fill_val[idx] = value

        cv.createTrackbar('R', name, 255, 255, lambda v: trackbar_callback(2, v))
        cv.createTrackbar('G', name, 255, 255, lambda v: trackbar_callback(1, v))
        cv.createTrackbar('B', name, 255, 255, lambda v: trackbar_callback(0, v))


        while True:
            image = np.full((500, 500, 3), fill_val)
            cv.imshow(name, image)
            key = cv.waitKey(3)
            if key == 27: 
                break
        cv.destroyAllWindows()
