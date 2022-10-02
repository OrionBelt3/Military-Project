# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowTask5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow5(object):
    def setupUi(self, MainWindow5):
        MainWindow5.setObjectName("MainWindow5")
        MainWindow5.resize(1601, 1253)
        MainWindow5.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow5)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow5.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow5)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1601, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow5.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow5)
        self.statusbar.setObjectName("statusbar")
        MainWindow5.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setIconSize(QtCore.QSize(47, 42))
        self.toolBar.setObjectName("toolBar")
        MainWindow5.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionNewFile = QtWidgets.QAction(MainWindow5)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/iconePack/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewFile.setIcon(icon)
        self.actionNewFile.setObjectName("actionNewFile")
        self.actionOpenFile = QtWidgets.QAction(MainWindow5)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/iconePack/write.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenFile.setIcon(icon1)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.actionSaveFile = QtWidgets.QAction(MainWindow5)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/iconePack/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveFile.setIcon(icon2)
        self.actionSaveFile.setObjectName("actionSaveFile")
        self.actionSaveFileAs = QtWidgets.QAction(MainWindow5)
        self.actionSaveFileAs.setObjectName("actionSaveFileAs")
        self.actionForward = QtWidgets.QAction(MainWindow5)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/iconePack/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionForward.setIcon(icon3)
        self.actionForward.setObjectName("actionForward")
        self.actionBackward = QtWidgets.QAction(MainWindow5)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/iconePack/reply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBackward.setIcon(icon4)
        self.actionBackward.setObjectName("actionBackward")
        self.actionbtnAddNode = QtWidgets.QAction(MainWindow5)
        self.actionbtnAddNode.setCheckable(True)
        self.actionbtnAddNode.setChecked(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/iconePack/add-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnAddNode.setIcon(icon5)
        self.actionbtnAddNode.setObjectName("actionbtnAddNode")
        self.actionbtnRemoveNode = QtWidgets.QAction(MainWindow5)
        self.actionbtnRemoveNode.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/iconePack/cross_circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnRemoveNode.setIcon(icon6)
        self.actionbtnRemoveNode.setObjectName("actionbtnRemoveNode")
        self.actionbtnMoveNode = QtWidgets.QAction(MainWindow5)
        self.actionbtnMoveNode.setCheckable(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("resources/iconePack/axis_arrow_icon_138909.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnMoveNode.setIcon(icon7)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.actionbtnMoveNode.setFont(font)
        self.actionbtnMoveNode.setPriority(QtWidgets.QAction.NormalPriority)
        self.actionbtnMoveNode.setObjectName("actionbtnMoveNode")
        self.actionbtnConnectNode = QtWidgets.QAction(MainWindow5)
        self.actionbtnConnectNode.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("resources/iconePack/file_addArrow.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnConnectNode.setIcon(icon8)
        self.actionbtnConnectNode.setObjectName("actionbtnConnectNode")
        self.actionbtnInfo = QtWidgets.QAction(MainWindow5)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("resources/iconePack/attachment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnInfo.setIcon(icon9)
        self.actionbtnInfo.setObjectName("actionbtnInfo")
        self.actionbtnHome = QtWidgets.QAction(MainWindow5)
        self.actionbtnHome.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("resources/iconePack/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnHome.setIcon(icon10)
        self.actionbtnHome.setObjectName("actionbtnHome")
        self.actionbtnRemoveNodeConnection = QtWidgets.QAction(MainWindow5)
        self.actionbtnRemoveNodeConnection.setCheckable(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("resources/iconePack/arrowRightDel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnRemoveNodeConnection.setIcon(icon11)
        self.actionbtnRemoveNodeConnection.setObjectName("actionbtnRemoveNodeConnection")
        self.actionbtnZoomIn = QtWidgets.QAction(MainWindow5)
        self.actionbtnZoomIn.setCheckable(False)
        self.actionbtnZoomIn.setChecked(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("resources/iconePack/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnZoomIn.setIcon(icon12)
        self.actionbtnZoomIn.setAutoRepeat(True)
        self.actionbtnZoomIn.setObjectName("actionbtnZoomIn")
        self.actionbtnZoomOut = QtWidgets.QAction(MainWindow5)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("resources/iconePack/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnZoomOut.setIcon(icon13)
        self.actionbtnZoomOut.setObjectName("actionbtnZoomOut")
        self.actionHelpTask = QtWidgets.QAction(MainWindow5)
        self.actionHelpTask.setObjectName("actionHelpTask")
        self.actionHelpProgram = QtWidgets.QAction(MainWindow5)
        self.actionHelpProgram.setObjectName("actionHelpProgram")
        self.actionSetting = QtWidgets.QAction(MainWindow5)
        self.actionSetting.setObjectName("actionSetting")
        self.actionbtnCheck = QtWidgets.QAction(MainWindow5)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("resources/iconePack/check-mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnCheck.setIcon(icon14)
        self.actionbtnCheck.setObjectName("actionbtnCheck")
        self.actionbtnDottedConnectNode = QtWidgets.QAction(MainWindow5)
        self.actionbtnDottedConnectNode.setCheckable(True)
        self.actionbtnDottedConnectNode.setEnabled(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("resources/iconePack/arrowsDotted.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnDottedConnectNode.setIcon(icon15)
        self.actionbtnDottedConnectNode.setObjectName("actionbtnDottedConnectNode")
        self.menuFile.addAction(self.actionNewFile)
        self.menuFile.addAction(self.actionOpenFile)
        self.menuFile.addAction(self.actionSaveFile)
        self.menuFile.addAction(self.actionSaveFileAs)
        self.menuFile.addSeparator()
        self.menuHelp.addAction(self.actionHelpTask)
        self.menuHelp.addAction(self.actionHelpProgram)
        self.menuEdit.addAction(self.actionForward)
        self.menuEdit.addAction(self.actionBackward)
        self.menu.addAction(self.actionSetting)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.actionbtnAddNode)
        self.toolBar.addAction(self.actionbtnRemoveNode)
        self.toolBar.addAction(self.actionbtnRemoveNodeConnection)
        self.toolBar.addAction(self.actionbtnMoveNode)
        self.toolBar.addAction(self.actionbtnConnectNode)
        self.toolBar.addAction(self.actionbtnDottedConnectNode)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionbtnCheck)
        self.toolBar.addAction(self.actionbtnInfo)
        self.toolBar.addAction(self.actionbtnHome)
        self.toolBar.addAction(self.actionbtnZoomIn)
        self.toolBar.addAction(self.actionbtnZoomOut)

        self.retranslateUi(MainWindow5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow5)

    def retranslateUi(self, MainWindow5):
        _translate = QtCore.QCoreApplication.translate
        MainWindow5.setWindowTitle(_translate("MainWindow5", "Задание 3"))
        self.menuFile.setTitle(_translate("MainWindow5", "Файл"))
        self.menuHelp.setTitle(_translate("MainWindow5", "Справка"))
        self.menuEdit.setTitle(_translate("MainWindow5", "Редактор"))
        self.menu.setTitle(_translate("MainWindow5", "Настройки"))
        self.toolBar.setWindowTitle(_translate("MainWindow5", "toolBar"))
        self.actionNewFile.setText(_translate("MainWindow5", "Новый файл"))
        self.actionNewFile.setToolTip(_translate("MainWindow5", "Создать новый файл"))
        self.actionOpenFile.setText(_translate("MainWindow5", "Открыть файл"))
        self.actionSaveFile.setText(_translate("MainWindow5", "Сохранить"))
        self.actionSaveFileAs.setText(_translate("MainWindow5", "Сохранить как"))
        self.actionForward.setText(_translate("MainWindow5", "Вперед        Ctrl+Y"))
        self.actionBackward.setText(_translate("MainWindow5", "Назад          Ctrl+Z"))
        self.actionbtnAddNode.setText(_translate("MainWindow5", "btnAddNode"))
        self.actionbtnAddNode.setToolTip(_translate("MainWindow5", "Добавить узел"))
        self.actionbtnRemoveNode.setText(_translate("MainWindow5", "btnRemoveNode"))
        self.actionbtnRemoveNode.setToolTip(_translate("MainWindow5", "Удаление узла и связей"))
        self.actionbtnMoveNode.setText(_translate("MainWindow5", "btnMoveNode"))
        self.actionbtnMoveNode.setToolTip(_translate("MainWindow5", "Передвинуть элемент"))
        self.actionbtnConnectNode.setText(_translate("MainWindow5", "btnConnectNode"))
        self.actionbtnConnectNode.setToolTip(_translate("MainWindow5", "Соединить узлы"))
        self.actionbtnInfo.setText(_translate("MainWindow5", "btnInfo"))
        self.actionbtnInfo.setToolTip(_translate("MainWindow5", "Подсказка"))
        self.actionbtnHome.setText(_translate("MainWindow5", "btnHome"))
        self.actionbtnHome.setToolTip(_translate("MainWindow5", "Перейти к выбору заданий / В меню"))
        self.actionbtnRemoveNodeConnection.setText(_translate("MainWindow5", "btnRemoveNodeСonnection"))
        self.actionbtnRemoveNodeConnection.setToolTip(_translate("MainWindow5", "Удаление связей"))
        self.actionbtnZoomIn.setText(_translate("MainWindow5", "btnZoomIn"))
        self.actionbtnZoomIn.setToolTip(_translate("MainWindow5", "Увеличить изображение"))
        self.actionbtnZoomOut.setText(_translate("MainWindow5", "btnZoomOut"))
        self.actionbtnZoomOut.setToolTip(_translate("MainWindow5", "Уменьшить изображение"))
        self.actionHelpTask.setText(_translate("MainWindow5", "Справка по заданию"))
        self.actionHelpProgram.setText(_translate("MainWindow5", "Справка по программе "))
        self.actionSetting.setText(_translate("MainWindow5", "Настройки программы"))
        self.actionbtnCheck.setText(_translate("MainWindow5", "btnCheck"))
        self.actionbtnCheck.setToolTip(_translate("MainWindow5", "<html><head/><body><p>Проверить задание</p></body></html>"))
        self.actionbtnDottedConnectNode.setText(_translate("MainWindow5", "btnDottedConnectNode"))
        self.actionbtnDottedConnectNode.setToolTip(_translate("MainWindow5", "Перемещение пунктирной стрелки"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow5 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow5()
    ui.setupUi(MainWindow5)
    MainWindow5.show()
    sys.exit(app.exec_())

