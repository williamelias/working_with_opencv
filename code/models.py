from typing import BinaryIO


import datetime

# from numpy.core.fromnumeric import shape 

class Image:
    _binary: BinaryIO = None 
    _name: str = ''
    _created_date: datetime.date
    _updated_date: datetime.date 
    _original_path: str 
    _original_shape: dict
    _custom_shape: dict
    _dtype: str

    def __init__(self,name='',shape={},path='') -> None:
        self._set_name(name)
        self._set_original_shape(shape)
        self._set_original_path(path)

    def _set_original_shape(self,shape):
        self.original_shape = shape

    def _set_original_path(self,path):
        self.original_path = path

    def _set_name(self,name=''):
        self._name = name
    
    def get_original_shape(self):
        return self.original_shape

    def get_original_path(self):
        return self.original_path


    def set_binary(self,binary_data):
        self._binary = binary_data


    def set_dtype(self,dtype):
        self._dtype = dtype


    def set_shape(self,shape):
        self._shape = shape


    def __str__(self):
        return f'string da classe: {self._name}-{self._binary}'
