# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task2CheckForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_task2CheckForm(object):
    def setupUi(self, task2CheckForm):
        task2CheckForm.setObjectName("task2CheckForm")
        task2CheckForm.resize(458, 368)
        self.gridLayout = QtWidgets.QGridLayout(task2CheckForm)
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton = QtWidgets.QToolButton(task2CheckForm)
        self.toolButton.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/iconePack/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("resources/iconePack/crossRed.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton.setIcon(icon)
        self.toolButton.setCheckable(True)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 2, 1, 1)
        self.labelNodesCount = QtWidgets.QLabel(task2CheckForm)
        self.labelNodesCount.setObjectName("labelNodesCount")
        self.gridLayout.addWidget(self.labelNodesCount, 1, 0, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(task2CheckForm)
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setCheckable(True)
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout.addWidget(self.toolButton_3, 2, 2, 1, 1)
        self.labelSoClose = QtWidgets.QLabel(task2CheckForm)
        self.labelSoClose.setObjectName("labelSoClose")
        self.gridLayout.addWidget(self.labelSoClose, 0, 0, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(task2CheckForm)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setCheckable(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout.addWidget(self.toolButton_2, 1, 2, 1, 1)
        self.labelConnectionsCount = QtWidgets.QLabel(task2CheckForm)
        self.labelConnectionsCount.setObjectName("labelConnectionsCount")
        self.gridLayout.addWidget(self.labelConnectionsCount, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(task2CheckForm)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)
        self.labelConnectionCross = QtWidgets.QLabel(task2CheckForm)
        self.labelConnectionCross.setObjectName("labelConnectionCross")
        self.gridLayout.addWidget(self.labelConnectionCross, 3, 0, 1, 1)
        self.toolButton_4 = QtWidgets.QToolButton(task2CheckForm)
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setCheckable(True)
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout.addWidget(self.toolButton_4, 3, 2, 1, 1)

        self.retranslateUi(task2CheckForm)
        QtCore.QMetaObject.connectSlotsByName(task2CheckForm)

    def retranslateUi(self, task2CheckForm):
        _translate = QtCore.QCoreApplication.translate
        task2CheckForm.setWindowTitle(_translate("task2CheckForm", "Проверка"))
        self.toolButton.setText(_translate("task2CheckForm", "..."))
        self.labelNodesCount.setText(_translate("task2CheckForm", "Верное количество вершин"))
        self.toolButton_3.setText(_translate("task2CheckForm", "..."))
        self.labelSoClose.setText(_translate("task2CheckForm", "Вершины на достаточном расстоянии"))
        self.toolButton_2.setText(_translate("task2CheckForm", "..."))
        self.labelConnectionsCount.setText(_translate("task2CheckForm", "Верное количество связей"))
        self.pushButton.setText(_translate("task2CheckForm", "Закрыть"))
        self.labelConnectionCross.setText(_translate("task2CheckForm", "Связи не пересекаются"))
        self.toolButton_4.setText(_translate("task2CheckForm", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    task2CheckForm = QtWidgets.QWidget()
    ui = Ui_task2CheckForm()
    ui.setupUi(task2CheckForm)
    task2CheckForm.show()
    sys.exit(app.exec_())
