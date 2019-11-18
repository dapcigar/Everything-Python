from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import json

app = QtWidgets.QApplication([])
dlg = uic.loadUi("List.ui")


def addItem():
    if not dlg.lineEdit.text() == "":
        dlg.lineEdit.setFocus()
        dlg.listWidget.addItem(dlg.lineEdit.text())

        show_Message("Successful", "Data Added")

    else:
        show_Message("Warning", "You must Enter a Value") #Display Message Box

    with open('data.json', 'r') as file:
        data = json.load(file)
    data["Items"].append(dlg.lineEdit.text()) #Edit an existing File

    with open('data.json', 'w') as file:  # Write to a file
        json.dump(data, file)

    dlg.lineEdit.setText("") # will Make the Textbox Empty once it execute.


def show_Message(title, message):
    QMessageBox.information(None, title, message)


def main():  # Using Json to Load file to the application
    with open('data.json', 'r') as file:
        data = json.load(file)
        for items in data["Items"]:
            dlg.listWidget.addItem(items)


if __name__ == "__main__":
    main()

dlg.pushButton.clicked.connect(addItem)
dlg.lineEdit.returnPressed.connect(addItem)

dlg.show()
app.exec()
