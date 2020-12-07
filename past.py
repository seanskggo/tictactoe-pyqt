# Tic Tac Toe GUI 
# Created with PyQT5
# To run this GUI, ensure all modules in requirements.txt are installed with pip
# For WSL, X11 Display Server needs to be configured

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
import sys

class images(object):
    ''' Class for compressing the image files: circle.png and cross.png.
    This was implemented so that the user can add any image online to 
    personalise the UI.
    '''
    def compress(self, image):
        img = Image.open(image)
        img = img.resize((83, 83))
        img.save(image) 

class Ui_window(object):
    ''' Creates the window for GUI and sets up all neccessary utilities '''
    def setupUi(self, window):
        # Compress all images
        images.compress(self, 'cross.png')
        images.compress(self, 'circle.png')
        window.setObjectName("window")
        window.resize(400, 400)
        window.setToolTipDuration(-2)
        self.pushButton = QtWidgets.QPushButton(window)
        self.pushButton.setGeometry(QtCore.QRect(160, 160, 85, 85))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)
        # when button pushed:
        self.pushButton.clicked.connect(self.button_pushed)
        self.pushButton.setStyleSheet("background-image : url(circle.png);") 
    
    def button_pushed(self):
        self.pushButton.setStyleSheet("background-image : url(cross.png);") 
    
    def button_pushed2(self):
        return

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Tic Tac Toe"))

# Main function to run the GUI
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
