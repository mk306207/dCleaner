import os
import getpass
from PyQt5.QtWidgets import QWidget,QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton, QToolBar, QButtonGroup, QCheckBox, QGroupBox
def mac():
    print("mac")
    current_user = getpass.getuser()
    os.chdir(f'/Users/{current_user}/Desktop/')
    print(os.getcwd())

class HomeMacOS(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings()
    
    def initUI(self):
        self.button = QPushButton("Clean!")
        self.applyButton = QPushButton("Apply!")
        
        self.radioButton1 = QCheckBox("Images")
        self.radioButton2 = QCheckBox("Apps")
        self.radioButton3 = QCheckBox("PDF")

        checkboxColumn = QWidget()
        checkboxLayout = QHBoxLayout()
        checkboxLayout.addWidget(self.radioButton1)
        checkboxLayout.addWidget(self.radioButton2)
        checkboxLayout.addWidget(self.radioButton3)
        checkboxColumn.setLayout(checkboxLayout)

        self.master = QHBoxLayout()
        myScreen = QVBoxLayout()

        myScreen.addWidget(checkboxColumn)
        myScreen.addWidget(self.applyButton)
        myScreen.addWidget(self.button)
        self.master.addLayout(myScreen,100)
        self.setLayout(self.master)

        self.setStyleSheet("""
            QWidget{
                background-color: #656664;        
            }
            QCheckBox{
                background-color: #ffffff;
                color: #000000;
            }
                           """)

    def settings(self):
        self.setWindowTitle("dCleaner")
        self.setGeometry(550,250,300,300)
        pass

    def buttonClick(self):
        pass

    def resetApp(self):
        pass
    
    def Clean(self):
        pass