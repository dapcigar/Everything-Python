from PyQts import QtWidgets, uic

app = QtWidgets.Qaplication([])
dlg = uic.loadUi("test.ui")

dlg.show()
app.exec()
