import os
import getpass
from PyQt5.QtWidgets import QWidget
def mac():
    print("mac")
    current_user = getpass.getuser()
    os.chdir(f'/Users/{current_user}/Desktop/')
    print(os.getcwd())

class HomeMacOS(QWidget):
    def __init__(self):
        super().__init__()
    
    def initUI(self):
        pass

    def settings(self):
        pass

    def buttonClick(self):
        pass

    def resetApp(self):
        pass
    
    def Clean(self):
        pass