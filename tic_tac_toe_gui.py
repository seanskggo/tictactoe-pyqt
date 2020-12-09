#################################################################################
# Tic Tac Toe GUI 
# Created with PyQT5
# To run this GUI, ensure all modules in requirements.txt are installed
# For WSL, X11 Display Server needs to be configured with correct display port
# 
# Personal Project - 7/12/2020
#################################################################################

#################################################################################
# Imports
#################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from csv import reader
from minimax_algorithm import best_move
import sys

#################################################################################
# Globals
#################################################################################

# Restricts player's turn alternatingly
p1_turn = True
# Binary representation of game board
game_state = [
    None, None, None, 
    None, None, None,
    None, None, None
]
end_game_state = [
    2, 2, 2,
    2, 2, 2,
    2, 2, 2
]
# Game outcome strings
progress = "Game in progress..."
p1_won = "Player 1 won!"
p2_won = "Player 2 won!"
draw = "It's a draw..."

#################################################################################
# Classes
#################################################################################

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
        # Set up display state for Tic Tac Toe
        self.set_dimensions()
        self.set_labels()
        # update label and window descriptions
        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def set_labels(self):
        ''' Sets labels for game status display ''' 
        # Create label reading "game status"
        self.label = QtWidgets.QLabel(window)
        self.label.setGeometry(QtCore.QRect(110, 330, 81, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        # Add text box to show game outcome
        self.plainTextEdit = QtWidgets.QPlainTextEdit(window)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 350, 265, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")

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
        # Creating click conditions had to be done individually due to clicked.connect
        # behaviour with exec when using lambda and self
        # for i in range(0, 9):
        #     eval(f"self.pushButton_{i}").clicked.connect(lambda: self.clicked(i, True))
        self.pushButton_0.clicked.connect(lambda: self.clicked(0, True))
        self.pushButton_1.clicked.connect(lambda: self.clicked(1, True))
        self.pushButton_2.clicked.connect(lambda: self.clicked(2, True))
        self.pushButton_3.clicked.connect(lambda: self.clicked(3, True))
        self.pushButton_4.clicked.connect(lambda: self.clicked(4, True))
        self.pushButton_5.clicked.connect(lambda: self.clicked(5, True))
        self.pushButton_6.clicked.connect(lambda: self.clicked(6, True))
        self.pushButton_7.clicked.connect(lambda: self.clicked(7, True))
        self.pushButton_8.clicked.connect(lambda: self.clicked(8, True))
        self.pushButton_9.clicked.connect(self.reset)
        dim_file.close()

    def clicked(self, index, ai):
        ''' Clicking behaviour of each button. If the button/square was previously
        pressed, then do nothing. Otherwise, display a circle of a cross depending on
        the player turn
        '''
        global p1_turn, game_state
        if game_state[index] is not None:
            return
        if p1_turn:
            exec(f'self.pushButton_{index}.setStyleSheet("background-image : url(circle.png);")')
        else:
            exec(f'self.pushButton_{index}.setStyleSheet("background-image : url(cross.png);")')
        game_state[index] = p1_turn
        self.check_outcome()
        p1_turn = True if p1_turn is False else False
        if ai: 
            self.AI_turn()

    def AI_turn(self):
        ''' Generate and play move from tic tac toe AI'''
        # If game state is terminal, simply return
        if game_state.count(2) > 0:
            return
        self.clicked(best_move(game_state, p1_turn), False)

    def check_outcome(self):
        ''' Check if the game state is drawn or won by a player '''
        global game_state
        _translate = QtCore.QCoreApplication.translate
        if game_state.count(None) == 0:
            self.plainTextEdit.setPlainText(_translate("window", draw))
            game_state = end_game_state
        # Conditions to determine a win/loss: hard coding is more concise with 3x3
        condition = [
            (game_state[0], game_state[1], game_state[2]),
            (game_state[3], game_state[4], game_state[5]),
            (game_state[6], game_state[7], game_state[8]),
            (game_state[0], game_state[3], game_state[6]),
            (game_state[1], game_state[4], game_state[7]),
            (game_state[2], game_state[5], game_state[8]),
            (game_state[0], game_state[4], game_state[8]),
            (game_state[2], game_state[4], game_state[6])
        ]
        # Check using the conditions
        for check in condition:
            if check == (True, True, True):
                self.plainTextEdit.setPlainText(_translate("window", p1_won))
                game_state = end_game_state
            elif check == (False, False, False):
                self.plainTextEdit.setPlainText(_translate("window", p2_won))
                game_state = end_game_state

    def reset(self):
        ''' Resets the game board '''
        global game_state
        game_state = [
            None, None, None, 
            None, None, None,
            None, None, None
        ]
        for index in range(0, 10):
            exec(f'self.pushButton_{index}.setStyleSheet("")')
        _translate = QtCore.QCoreApplication.translate
        self.plainTextEdit.setPlainText(_translate("window", progress))

    def retranslateUi(self, window):
        ''' Updates the starting state/description of buttons and window '''
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Tic Tac Toe"))
        self.pushButton_9.setText(_translate("window", "Reset"))
        self.label.setText(_translate("window", "Game Status"))
        self.plainTextEdit.setPlainText(_translate("window", progress))

class images(object):
    ''' Class for compressing the image files: circle.png and cross.png.
    This was implemented so that the user can add any image online to 
    personalise the UI.
    '''
    def compress(self, image):
        ''' Resizes the input image to 83x83 ''' 
        img = Image.open(image)
        img = img.resize((83, 83))
        img.save(image) 

#################################################################################
# Main
#################################################################################

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
