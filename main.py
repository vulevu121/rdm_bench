from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton,QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
#import Shared
import sys

import design1


class ExampleApp(QMainWindow, design1.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
##        icon = QIcon()
##        icon.addPixmap(QPixmap("icon.png"))
##        self.pushButton.setIcon(icon)
##        self.pushButton.clicked.connect(self.print_text)


##    def print_text(self):
##        soc = 10
##        self.label.setText("The SOC is {}".format(soc))
##        print('SOC:', soc)
        
		
def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()
	
if __name__ == '__main__':
    main()
