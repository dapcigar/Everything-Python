from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

from sqlhelper import *

app = QtWidgets.QApplication([])
dlg = uic.loadUi("DBview.ui")

helper = SqliteHelper("test.db")


def loadData():
    users = helper.select("SELECT * FROM users")
    # print(users)
    for row_count, user in enumerate(users):
        dlg.tableWidget.insertRow(row_count)

        # Load the Data
        for column_number, data in enumerate(user):
            cell = QtWidgets.QTableWidgetItem(str(data))
            dlg.tableWidget.setItem(row_count, column_number, cell)


# Clear Data so table can refresh
def clearData():
    dlg.tableWidget.clearSelection()
    while dlg.tableWidget.rowCount() > 0:
        dlg.tableWidget.removeRow(0)
        dlg.tableWidget.clearSelection()


def addUser():
    name = dlg.lineEdit.text()
    date = dlg.lineEdit_Date.text()
    admin = dlg.checkBox.isChecked()
    a = 0
    if admin:
        a = 1
    # Create a Tupule to hold the insert Data

    if name.strip(" ") != "" and date.strip(" ") != "":
        user = (name, int(date), admin)
        helper.insert("INSERT INTO users (name, year, admin) VALUES(?,?,?)", user)
        show_Message("Success", "Data Added Successfully")
        refresh()

        # Clear Textbox once Data is inserted
        dlg.lineEdit.setText("")
        dlg.lineEdit_Date.setText("")
    else:
        show_Message("Error", "Please Input Data")


# Method to Create message box
def show_Message(title, message):
    QMessageBox.information(None, title, message)


def SelectionChanged():
    selected_Row = getSelectedRowId()
    selected_User = getSelectedUserId()
    name = dlg.tableWidget.item(getSelectedRowId(), 1).text()
    date = dlg.tableWidget.item(getSelectedRowId(), 2).text()
    admin = dlg.tableWidget.item(getSelectedRowId(), 3).text()
    if admin == 1:
        dlg.checkBox.setChecked(True)
    else:
        dlg.checkBox.setChecked(False)

    dlg.lineEdit.setText(name)
    dlg.lineEdit_Date.setText(date)


# This return the index of the data in the table. Note that index sart from zero
def getSelectedRowId():
    return dlg.tableWidget.currentRow()


def getSelectedUserId():
    return dlg.tableWidget.item(getSelectedRowId(), 0).text()


# Update user method
def updateUser():
    id_update = getSelectedUserId()
    print(id_update)
    name = dlg.lineEdit.text()
    date = dlg.lineEdit_Date.text()
    admin = dlg.checkBox.isChecked()
    a = 0
    if admin:
        a = 1
    # Create a Tupule to hold the insert Data

    if name.strip(" ") != "" and date.strip(" ") != "":
        user = (name, int(date), admin)
        helper.edit("UPDATE users SET name=?, year=?, admin=? WHERE id =" + id_update, user)
        show_Message("Success", "Data Added Successfully")
        refresh()
        dlg.lineEdit.setText("")
        dlg.lineEdit_Date.setText("")


# Remove user Method
def deleteUser():
    id_delete = getSelectedUserId()
    helper.delete("DELETE FROM users WHERE id =" + id_delete)
    refresh()


def refresh():  # Reloads the Table
    clearData()
    loadData()


dlg.pushButton.clicked.connect(addUser)  # Add user button
dlg.tableWidget.itemSelectionChanged.connect(SelectionChanged)
dlg.pushButton_update.clicked.connect(updateUser)  # Update user button
dlg.pushButton_Del.clicked.connect(deleteUser)  # Delete user button

loadData()
dlg.show()
app.exec()