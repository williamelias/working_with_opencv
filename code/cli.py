
class CustomCli:
    def __init__(self,parser):
        self.parser = parser
        self._set_params()
    def _get_params(self):
        args = self.parser.parse_args()
        args = vars(args)
        return args
    def _set_params(self):
        self.parser.add_argument('--command', default=0, help='default command cli') 
        self.parser.add_argument('--path', default='code/media/imgs/img.png', help='Image path.')
