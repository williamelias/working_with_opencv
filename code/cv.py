from typing import Optional
import cv2 as cv
from models import Image
import sys 
import datetime


class CVHandler:
    def __init__(self,path):
        self.path = path
        self._image = None
        self.img = None
    
    def _set_image(self,image:Image):
        self._image = image

    def read_image(self):

        # if self.path is None:
        img = cv.imread(self.path)
        self.img = img
        assert img is not None
        ord_args = {
            'path':self.path,
            'shape': img.shape,
        }

        image = Image(name='image_name',**ord_args)
        image.set_dtype(img.dtype)
        
        self._set_image(image)

    
    def get_image(self):
        if self.img is None:
            self.read_image()
        return self.img

    def resize_image(self):
        #first for all , need read image

        image = self.get_image()
        resized_img = cv.resize(image, (128, 256))
        print('resized to 128x256 image shape:', resized_img.shape)

    def reflect_image(self):
        #first for all , need read image

        img = self.get_image()
        img_flip_along_x = cv.flip(img, 0)
    
    def flip_vertical_y(self):
        #first for all , need read image

        img = self.get_image()
        img_flip_along_y = cv.flip(img, 1)
    
    def flip_simultaneously(self):
        #first for all , need read image
        img = self.get_image()
        img_flip = cv.flip(img, -1)

    def save_img_as(self,type='PNG'):
        img = self.get_image()
        
        path_new_image = 'code/media/imgs/{}_.{}'

        third_argument = {
            'PNG':  [cv.IMWRITE_PNG_COMPRESSION, 10],
            'JPG':  [cv.IMWRITE_JPEG_QUALITY, 0]
        }

        now = datetime.datetime.now().date()

        print(path_new_image.format(now,type.lower()))
        print(img.shape)
        cv.imwrite(path_new_image.format(now,type.lower()),img,third_argument[type])
        
        saved_img = cv.imread(path_new_image.format(now,type.lower()))
        assert saved_img.all() == img.all()

        self.show_image(saved_img)

    def show_image(self,img):
        orig_size = img.shape[0:2]
        cv.imshow("Original image", img)
        cv.waitKey(2000)