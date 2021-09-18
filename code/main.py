
from cli import CustomCli
from cv import CVHandler
import cv2 as cv
import sys
import argparse
import logging

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    cli = CustomCli(parser)
    params = cli._get_params()
    if [*params.keys()] == ['command','path']:
        COMMAND_ACTIONS = {
            0: CVHandler
        }

        object = COMMAND_ACTIONS[params['command']]
        if object.__name__ == 'CVHandler':
            object = object((params['path']))
            CV_ACTIONS = {
                '0': object.read_image ,
                '1': object.resize_image,
                'q': sys.exit,
                '3':object.save_img_as
            }
            action = ''
            print("Insira uma ação, opções permitidas:\n-1:exit\n0:read_image\n1:resize_image)\n")
            while action != 'q':
                action = input()
                action_base = action[0]
                try:
                    # CV_ACTIONS[action_base](**dict(map(lambda x: x,list(action[1:]))))
                    CV_ACTIONS[action_base]()

                except KeyError:
                    sys.exit('Opção inválida,programa fechando..')
                except TypeError as tp:
                    logging.error(f"{tp}")
