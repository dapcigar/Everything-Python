from PyQt5 import QtWidgets, uic


def Convert():
    dlg.lineEdit_2.setText(str(float(dlg.lineEdit.text()) * 1.23))


app = QtWidgets.QApplication([])
dlg = uic.loadUi("test.ui")

dlg.lineEdit.setFocus() #Focus the Cusor on the Textbox
dlg.lineEdit.setPlaceholderText("Euros") #Set a place holder in case of Label
dlg.lineEdit_2.setPlaceholderText("Dollars")
dlg.pushButton.clicked.connect(Convert) #Call Action Button with the Method to Trigger

dlg.lineEdit.returnPressed.connect(Convert) #Call the Convert Method by pressing Enter Button
dlg.lineEdit_2.setReadOnly(True) # Make it impossible to Edit an output by setting it to read only

dlg.show()
app.exec()
