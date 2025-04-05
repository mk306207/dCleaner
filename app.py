import os
import macOS
import Windows
from PyQt5.QtWidgets import QApplication


if os.name == "posix":
    if __name__ in "__main__":
        app = QApplication([])
        macApp = macOS.HomeMacOS()
        macApp.show()
        app.exec_()
    macOS.mac()
elif os.name == "nt":
    Windows.win()
else:
    print("unsupported os!")
