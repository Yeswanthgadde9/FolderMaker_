import sys
import os
import json
from PySide2.QtWidgets import *
from PySide2.QtCore import *


class Folder(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Make My Folder")
        self.setGeometry(550, 400, 350, 200)
        self.ui()

    def ui(self):
        self.maindesign()
        self.layouts()

    def maindesign(self):
        self.shot = QLabel("Shot Name:")
        self.shot_input = QLineEdit()
        self.path = QLabel("Path:")
        self.path_input = QLineEdit()
        self.create = QPushButton("Create")
        self.create.clicked.connect(self.make_my_folder)
        self.cancel = QPushButton("Cancel")
        self.cancel.clicked.connect(self.cancel_func)

    def layouts(self):
        self.mainlayout = QVBoxLayout()
        self.toplayout = QFormLayout()
        self.bottomlayout = QHBoxLayout()

        self.mainlayout.addLayout(self.toplayout)
        self.mainlayout.addLayout(self.bottomlayout)

        self.toplayout.addRow(self.shot, self.shot_input)
        self.toplayout.addRow(self.path, self.path_input)

        self.bottomlayout.setAlignment(Qt.AlignCenter)
        self.bottomlayout.addWidget(self.create, alignment=Qt.AlignCenter)
        self.bottomlayout.addWidget(self.cancel, alignment=Qt.AlignCenter)
        self.setLayout(self.mainlayout)

    def make_my_folder(self):
        input_path = self.path_input.text()
        shot = self.shot_input.text()
        path = os.path.join(input_path, shot)
        json_path = ('{}/foldernames.json'.format(os.path.dirname(__file__)))
        with open(json_path) as f:
            data = json.load(f)
            if not os.path.exists(path):
                for folder in data["folders"].values():
                    for i in folder.values():
                        os.makedirs(os.path.join(path, str(i)))
                self.close()
                nuke.message("Folders Created")
            else:
                nuke.message("Folder Already Exists")
                self.close()


    def cancel_func(self):
        self.close()


def main():
    main.object = Folder()
    main.object.show()
