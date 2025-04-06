import os
import getpass
from PyQt5.QtWidgets import QWidget,QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton, QToolBar, QButtonGroup, QCheckBox
def mac():
    print("mac")
    current_user = getpass.getuser()
    os.chdir(f'/Users/{current_user}/Desktop/')
    print(os.getcwd())

class HomeMacOS(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.button = QPushButton("Clean!")
        self.radioButton1 = QCheckBox("Images")
        self.radioButton2 = QCheckBox("Apps")
        self.radioButton3 = QCheckBox("PDF")

        self.buttonsBar = QToolBar()
        self.master = QHBoxLayout()
        myScreen = QVBoxLayout()

        self.buttonsBar.addWidget(self.radioButton1)
        self.buttonsBar.addWidget(self.radioButton2)
        self.buttonsBar.addWidget(self.radioButton3)

        myScreen.addWidget(self.buttonsBar)
        myScreen.addWidget(self.button)
        self.master.addLayout(myScreen,100)
        self.setLayout(self.master)

    def settings(self):
        pass

    def buttonClick(self):
        pass

    def resetApp(self):
        pass
    
    def Clean(self):
        pass