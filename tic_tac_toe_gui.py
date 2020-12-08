#################################################################################
# Tic Tac Toe GUI 
# Created with PyQT5
# To run this GUI, ensure all modules in requirements.txt are installed with pip
# For WSL, X11 Display Server needs to be configured with correct display port
#################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from csv import reader
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
    def setupUi(self, window):
        ''' Creates the window for GUI and sets up all neccessary utilities '''
        # Compress all images
        images.compress(self, 'cross.png')
        images.compress(self, 'circle.png')
        # Set up window
        window.setObjectName("window")
        window.resize(306, 398)
        window.setToolTipDuration(-2)
        # Set up buttons for Tic Tac Toe
        self.set_dimensions()
        # Create label for display game status
        self.label = QtWidgets.QLabel(window)
        self.label.setGeometry(QtCore.QRect(110, 330, 81, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        # Add text box to show game outcome
        self.plainTextEdit = QtWidgets.QPlainTextEdit(window)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 350, 265, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        # update label and window descriptions
        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def set_dimensions(self):
        ''' Recursively reads csv file for dimensions. Sets the board buttons 
        accordingly 
        ''' 
        dim_file = open("dimensions.csv")
        csv_data = reader(dim_file, delimiter=',')
        next(csv_data)
        for index in range(0, 10):
            temp = list(next(csv_data))
            exec(f"self.pushButton_{index} = QtWidgets.QPushButton(window)")
            exec(f"self.pushButton_{index}.setObjectName('pushButton_{index}')")
            exec(f'''self.pushButton_{index}.setGeometry(\
                QtCore.QRect({temp[0]}, {temp[1]}, {temp[2]}, {temp[3]}))''')
        dim_file.close()

    def retranslateUi(self, window):
        ''' Updates the starting state/description of buttons and window '''
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Tic Tac Toe"))
        self.pushButton_9.setText(_translate("window", "Reset"))
        self.label.setText(_translate("window", "Game Status"))
        self.plainTextEdit.setPlainText(_translate("window", "Game in progress..."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
