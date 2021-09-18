
from cli import CustomCli
from image_handle.basic import CVHandler
from image_handle.ui import CVUiHandler
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
            '0': CVHandler,
            '1': CVUiHandler
        }
        object = COMMAND_ACTIONS[params['command']]
        print(object)
        if object.__name__ == 'CVHandler':
            object = object((params['path']))
            CV_ACTIONS = {
                '0': object.read_image ,
                '1': object.resize_image,
                'q': sys.exit,
                '3':object.save_img_as,
                '4':object.save_img_as
            }
            action = ''
            print("Insira uma ação, opções permitidas:\nq:exit\n0:read_image\n1:resize_image\n")
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

        elif object.__name__ == 'CVUiHandler':
            object = object()
            CV_ACTIONS = {
                '0': object.create_window ,
                'q': sys.exit,
            }
            action = ''
            print("Insira uma ação, opções permitidas:\nq:exit\n0:create_window\n")
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
