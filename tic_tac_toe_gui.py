# Tic Tac Toe GUI 
# Created with PyQT5
# To run this GUI, ensure all modules in requirements.txt are installed with pip
# For WSL, X11 Display Server needs to be configured

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class images(object):
''' Class for compressing the image files: circle.png and cross.png.
This was implemented so that the user can add any image online to 
personalise the UI.
'''
    def compress(self, image):
        pass

class Ui_window(object):
    # 
    def setupUi(self, window):
        # 
        window.setObjectName("window")
        window.resize(400, 389)
        window.setToolTipDuration(-2)
        self.pushButton = QtWidgets.QPushButton(window)
        self.pushButton.setGeometry(QtCore.QRect(160, 160, 75, 61))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)
        # when button pushed:
        self.pushButton.clicked.connect(self.button_pushed)
        self.pushButton.setStyleSheet("background-image : url(cross.png);") 
    
    def button_pushed(self):
        print("yoyo wassup homieee")

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Tic Tac Toe"))
        self.pushButton.setText(_translate("window", "press me!"))

# Main function to run the GUI
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
