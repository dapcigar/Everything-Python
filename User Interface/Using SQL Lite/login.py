from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from sqlhelper import *

app = QtWidgets.QApplication([])
dlg = uic.loadUi("Login.ui")

helper = SqliteHelper("test.db")


def login():
    username = dlg.lineEdit.text()
    password = dlg.lineEdit2.text()
    user = (username, password)

    t = helper.select(
        "SELECT * FROM login WHERE username = ? AND password =?", user)

    for col in t:
        if username == col[1] and password == col[2]:
            show_Message("Success", "Correct Information")
        else:
            show_Message("Error", "Invalid input")


def show_Message(title, message):
    QMessageBox.information(None, title, message)


dlg.btn_login.clicked.connect(login)

dlg.show()
app.exec()
