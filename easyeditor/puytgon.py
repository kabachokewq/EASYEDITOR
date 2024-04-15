import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox,QFileDialog,QAction)
from PyQt5.QtGui import QKeySequence
from PIL import Image, ImageFilter
app =QApplication([])
win = QWidget()
win.resize(600,300)
win.setWindowTitle("Easy Editor")


lb_image= QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()

btn_left = QPushButton("Ліво")
btn_right = QPushButton("Право")
btn_flip =QPushButton('Відзеркалити')
btn_sharp = QPushButton('Різкість')

btn_sharp.setStyleSheet('''
    QPushButton {
        background-color: red;
    }
    QPushButton:hover {
        background-color: purple;
    }
''')

btn_dir.setStyleSheet('''
    QPushButton {
        background-color: pink;
    }
    QPushButton:hover {
        background-color: darkpink;
    }
''')

btn_flip.setStyleSheet('''
    QPushButton {
        background-color: yellow;
    }
    QPushButton:hover {
        background-color: darkyellow;
    }
''')


btn_left.setStyleSheet('''
    QPushButton {
        background-color: green;
    }
    QPushButton:hover {
        background-color: darkgreen;
    }
''')

btn_right.setStyleSheet('''
    QPushButton {
        background-color: pink;
    }
    QPushButton:hover {
        background-color: darkpink;
    }
''')

row = QHBoxLayout()

row.addWidget(btn_left)
row.addWidget(btn_right)
row.addWidget(btn_flip)
row.addWidget(btn_sharp)


col1=QVBoxLayout()
col2=QVBoxLayout()


col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image)
col2.addLayout(row)

main_layout = QHBoxLayout()
main_layout.addLayout(col1)
main_layout.addLayout(col2)
win.setLayout(main_layout)
class Image():
    def __init__(self):
        self.filename = None
        self.original = None
        self.newphoto = None
        self.dir = "MainPhoto/"

    def do_bw(self):
        self.newphoto = self.newphoto.convert("")
win.show()
app.exec_()

