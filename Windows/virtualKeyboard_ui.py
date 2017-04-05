# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'virtualKeyboard.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VirtualKeyboard(object):
    def setupUi(self, VirtualKeyboard):
        VirtualKeyboard.setObjectName("VirtualKeyboard")
        VirtualKeyboard.resize(800, 430)
        VirtualKeyboard.setStyleSheet("QDialog\n"
"{\n"
"    border: 1px solid #76797C;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(VirtualKeyboard)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, 11, -1)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.clearBtn = TouchButton(VirtualKeyboard)
        self.clearBtn.setMinimumSize(QtCore.QSize(80, 48))
        self.clearBtn.setMaximumSize(QtCore.QSize(80, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.clearBtn.setFont(font)
        self.clearBtn.setObjectName("clearBtn")
        self.horizontalLayout_5.addWidget(self.clearBtn)
        self.spaceBarBtn = TouchButton(VirtualKeyboard)
        self.spaceBarBtn.setMinimumSize(QtCore.QSize(300, 48))
        self.spaceBarBtn.setMaximumSize(QtCore.QSize(300, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.spaceBarBtn.setFont(font)
        self.spaceBarBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spaceBarBtn.setAutoRepeat(True)
        self.spaceBarBtn.setObjectName("spaceBarBtn")
        self.horizontalLayout_5.addWidget(self.spaceBarBtn)
        self.leftBtn = TouchButton(VirtualKeyboard)
        self.leftBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.leftBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.leftBtn.setFont(font)
        self.leftBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.leftBtn.setAutoRepeat(True)
        self.leftBtn.setObjectName("leftBtn")
        self.horizontalLayout_5.addWidget(self.leftBtn)
        self.rightBtn = TouchButton(VirtualKeyboard)
        self.rightBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.rightBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.rightBtn.setFont(font)
        self.rightBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rightBtn.setAutoRepeat(True)
        self.rightBtn.setObjectName("rightBtn")
        self.horizontalLayout_5.addWidget(self.rightBtn)
        self.confirmBtn = TouchButton(VirtualKeyboard)
        self.confirmBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.confirmBtn.setMaximumSize(QtCore.QSize(48, 48))
        self.confirmBtn.setStyleSheet("background-color: transparent;\n"
"border: 0;")
        self.confirmBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/GreenCheckIcon_Finished.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.confirmBtn.setIcon(icon)
        self.confirmBtn.setIconSize(QtCore.QSize(48, 48))
        self.confirmBtn.setObjectName("confirmBtn")
        self.horizontalLayout_5.addWidget(self.confirmBtn)
        self.cancelBtn = TouchButton(VirtualKeyboard)
        self.cancelBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.cancelBtn.setMaximumSize(QtCore.QSize(48, 48))
        self.cancelBtn.setStyleSheet("background-color: transparent;\n"
"border: 0;")
        self.cancelBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/Icons/RedCancelIcon_Finished.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelBtn.setIcon(icon1)
        self.cancelBtn.setIconSize(QtCore.QSize(48, 48))
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_5.addWidget(self.cancelBtn)
        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(VirtualKeyboard)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QWidget\n"
"{\n"
"    border: 1px solid #76797C;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.leftShiftBtn = TouchButton(VirtualKeyboard)
        self.leftShiftBtn.setMinimumSize(QtCore.QSize(108, 48))
        self.leftShiftBtn.setMaximumSize(QtCore.QSize(108, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.leftShiftBtn.setFont(font)
        self.leftShiftBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.leftShiftBtn.setCheckable(True)
        self.leftShiftBtn.setAutoDefault(False)
        self.leftShiftBtn.setObjectName("leftShiftBtn")
        self.horizontalLayout_4.addWidget(self.leftShiftBtn)
        self.zBtn = TouchButton(VirtualKeyboard)
        self.zBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.zBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.zBtn.setFont(font)
        self.zBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zBtn.setAutoRepeat(True)
        self.zBtn.setObjectName("zBtn")
        self.horizontalLayout_4.addWidget(self.zBtn)
        self.xBtn = TouchButton(VirtualKeyboard)
        self.xBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.xBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.xBtn.setFont(font)
        self.xBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.xBtn.setAutoRepeat(True)
        self.xBtn.setObjectName("xBtn")
        self.horizontalLayout_4.addWidget(self.xBtn)
        self.cBtn = TouchButton(VirtualKeyboard)
        self.cBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.cBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.cBtn.setFont(font)
        self.cBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cBtn.setAutoRepeat(True)
        self.cBtn.setObjectName("cBtn")
        self.horizontalLayout_4.addWidget(self.cBtn)
        self.vBtn = TouchButton(VirtualKeyboard)
        self.vBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.vBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.vBtn.setFont(font)
        self.vBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.vBtn.setAutoRepeat(True)
        self.vBtn.setObjectName("vBtn")
        self.horizontalLayout_4.addWidget(self.vBtn)
        self.bBtn = TouchButton(VirtualKeyboard)
        self.bBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.bBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.bBtn.setFont(font)
        self.bBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bBtn.setAutoRepeat(True)
        self.bBtn.setObjectName("bBtn")
        self.horizontalLayout_4.addWidget(self.bBtn)
        self.nBtn = TouchButton(VirtualKeyboard)
        self.nBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.nBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.nBtn.setFont(font)
        self.nBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.nBtn.setAutoRepeat(True)
        self.nBtn.setObjectName("nBtn")
        self.horizontalLayout_4.addWidget(self.nBtn)
        self.mBtn = TouchButton(VirtualKeyboard)
        self.mBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.mBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.mBtn.setFont(font)
        self.mBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mBtn.setAutoRepeat(True)
        self.mBtn.setObjectName("mBtn")
        self.horizontalLayout_4.addWidget(self.mBtn)
        self.commaBtn = TouchButton(VirtualKeyboard)
        self.commaBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.commaBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.commaBtn.setFont(font)
        self.commaBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.commaBtn.setAutoRepeat(True)
        self.commaBtn.setObjectName("commaBtn")
        self.horizontalLayout_4.addWidget(self.commaBtn)
        self.periodBtn = TouchButton(VirtualKeyboard)
        self.periodBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.periodBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.periodBtn.setFont(font)
        self.periodBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.periodBtn.setAutoRepeat(True)
        self.periodBtn.setObjectName("periodBtn")
        self.horizontalLayout_4.addWidget(self.periodBtn)
        self.forwardSlashBtn = TouchButton(VirtualKeyboard)
        self.forwardSlashBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.forwardSlashBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.forwardSlashBtn.setFont(font)
        self.forwardSlashBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.forwardSlashBtn.setAutoRepeat(True)
        self.forwardSlashBtn.setObjectName("forwardSlashBtn")
        self.horizontalLayout_4.addWidget(self.forwardSlashBtn)
        self.rightShiftBtn = TouchButton(VirtualKeyboard)
        self.rightShiftBtn.setMinimumSize(QtCore.QSize(125, 48))
        self.rightShiftBtn.setMaximumSize(QtCore.QSize(125, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.rightShiftBtn.setFont(font)
        self.rightShiftBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rightShiftBtn.setCheckable(True)
        self.rightShiftBtn.setChecked(False)
        self.rightShiftBtn.setAutoDefault(False)
        self.rightShiftBtn.setObjectName("rightShiftBtn")
        self.horizontalLayout_4.addWidget(self.rightShiftBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.tabBtn = TouchButton(VirtualKeyboard)
        self.tabBtn.setMinimumSize(QtCore.QSize(66, 48))
        self.tabBtn.setMaximumSize(QtCore.QSize(66, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.tabBtn.setFont(font)
        self.tabBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabBtn.setAutoRepeat(True)
        self.tabBtn.setObjectName("tabBtn")
        self.horizontalLayout_2.addWidget(self.tabBtn)
        self.qBtn = TouchButton(VirtualKeyboard)
        self.qBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.qBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.qBtn.setFont(font)
        self.qBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.qBtn.setAutoRepeat(True)
        self.qBtn.setObjectName("qBtn")
        self.horizontalLayout_2.addWidget(self.qBtn)
        self.wBtn = TouchButton(VirtualKeyboard)
        self.wBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.wBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.wBtn.setFont(font)
        self.wBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.wBtn.setAutoRepeat(True)
        self.wBtn.setObjectName("wBtn")
        self.horizontalLayout_2.addWidget(self.wBtn)
        self.eBtn = TouchButton(VirtualKeyboard)
        self.eBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.eBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.eBtn.setFont(font)
        self.eBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.eBtn.setAutoRepeat(True)
        self.eBtn.setObjectName("eBtn")
        self.horizontalLayout_2.addWidget(self.eBtn)
        self.rBtn = TouchButton(VirtualKeyboard)
        self.rBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.rBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.rBtn.setFont(font)
        self.rBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rBtn.setAutoRepeat(True)
        self.rBtn.setObjectName("rBtn")
        self.horizontalLayout_2.addWidget(self.rBtn)
        self.tBtn = TouchButton(VirtualKeyboard)
        self.tBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.tBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.tBtn.setFont(font)
        self.tBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tBtn.setAutoRepeat(True)
        self.tBtn.setObjectName("tBtn")
        self.horizontalLayout_2.addWidget(self.tBtn)
        self.yBtn = TouchButton(VirtualKeyboard)
        self.yBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.yBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.yBtn.setFont(font)
        self.yBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.yBtn.setAutoRepeat(True)
        self.yBtn.setObjectName("yBtn")
        self.horizontalLayout_2.addWidget(self.yBtn)
        self.uBtn = TouchButton(VirtualKeyboard)
        self.uBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.uBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.uBtn.setFont(font)
        self.uBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.uBtn.setAutoRepeat(True)
        self.uBtn.setObjectName("uBtn")
        self.horizontalLayout_2.addWidget(self.uBtn)
        self.iBtn = TouchButton(VirtualKeyboard)
        self.iBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.iBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.iBtn.setFont(font)
        self.iBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.iBtn.setAutoRepeat(True)
        self.iBtn.setObjectName("iBtn")
        self.horizontalLayout_2.addWidget(self.iBtn)
        self.oBtn = TouchButton(VirtualKeyboard)
        self.oBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.oBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.oBtn.setFont(font)
        self.oBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.oBtn.setAutoRepeat(True)
        self.oBtn.setObjectName("oBtn")
        self.horizontalLayout_2.addWidget(self.oBtn)
        self.pBtn = TouchButton(VirtualKeyboard)
        self.pBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.pBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.pBtn.setFont(font)
        self.pBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pBtn.setAutoRepeat(True)
        self.pBtn.setObjectName("pBtn")
        self.horizontalLayout_2.addWidget(self.pBtn)
        self.leftBraceBtn = TouchButton(VirtualKeyboard)
        self.leftBraceBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.leftBraceBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.leftBraceBtn.setFont(font)
        self.leftBraceBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.leftBraceBtn.setAutoRepeat(True)
        self.leftBraceBtn.setObjectName("leftBraceBtn")
        self.horizontalLayout_2.addWidget(self.leftBraceBtn)
        self.rightBraceBtn = TouchButton(VirtualKeyboard)
        self.rightBraceBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.rightBraceBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.rightBraceBtn.setFont(font)
        self.rightBraceBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rightBraceBtn.setAutoRepeat(True)
        self.rightBraceBtn.setObjectName("rightBraceBtn")
        self.horizontalLayout_2.addWidget(self.rightBraceBtn)
        self.backSlashBtn = TouchButton(VirtualKeyboard)
        self.backSlashBtn.setMinimumSize(QtCore.QSize(59, 48))
        self.backSlashBtn.setMaximumSize(QtCore.QSize(59, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.backSlashBtn.setFont(font)
        self.backSlashBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.backSlashBtn.setAutoRepeat(True)
        self.backSlashBtn.setObjectName("backSlashBtn")
        self.horizontalLayout_2.addWidget(self.backSlashBtn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.tildeBtn = TouchButton(VirtualKeyboard)
        self.tildeBtn.setMinimumSize(QtCore.QSize(36, 48))
        self.tildeBtn.setMaximumSize(QtCore.QSize(36, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.tildeBtn.setFont(font)
        self.tildeBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tildeBtn.setAutoRepeat(True)
        self.tildeBtn.setObjectName("tildeBtn")
        self.horizontalLayout.addWidget(self.tildeBtn)
        self.oneBtn = TouchButton(VirtualKeyboard)
        self.oneBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.oneBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.oneBtn.setFont(font)
        self.oneBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.oneBtn.setAutoRepeat(True)
        self.oneBtn.setObjectName("oneBtn")
        self.horizontalLayout.addWidget(self.oneBtn)
        self.twoBtn = TouchButton(VirtualKeyboard)
        self.twoBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.twoBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.twoBtn.setFont(font)
        self.twoBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.twoBtn.setAutoRepeat(True)
        self.twoBtn.setObjectName("twoBtn")
        self.horizontalLayout.addWidget(self.twoBtn)
        self.threeBtn = TouchButton(VirtualKeyboard)
        self.threeBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.threeBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.threeBtn.setFont(font)
        self.threeBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.threeBtn.setAutoRepeat(True)
        self.threeBtn.setObjectName("threeBtn")
        self.horizontalLayout.addWidget(self.threeBtn)
        self.fourBtn = TouchButton(VirtualKeyboard)
        self.fourBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.fourBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.fourBtn.setFont(font)
        self.fourBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fourBtn.setAutoRepeat(True)
        self.fourBtn.setObjectName("fourBtn")
        self.horizontalLayout.addWidget(self.fourBtn)
        self.fiveBtn = TouchButton(VirtualKeyboard)
        self.fiveBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.fiveBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.fiveBtn.setFont(font)
        self.fiveBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fiveBtn.setAutoRepeat(True)
        self.fiveBtn.setObjectName("fiveBtn")
        self.horizontalLayout.addWidget(self.fiveBtn)
        self.sixBtn = TouchButton(VirtualKeyboard)
        self.sixBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.sixBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.sixBtn.setFont(font)
        self.sixBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sixBtn.setAutoRepeat(True)
        self.sixBtn.setObjectName("sixBtn")
        self.horizontalLayout.addWidget(self.sixBtn)
        self.sevenBtn = TouchButton(VirtualKeyboard)
        self.sevenBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.sevenBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.sevenBtn.setFont(font)
        self.sevenBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sevenBtn.setAutoRepeat(True)
        self.sevenBtn.setObjectName("sevenBtn")
        self.horizontalLayout.addWidget(self.sevenBtn)
        self.eightBtn = TouchButton(VirtualKeyboard)
        self.eightBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.eightBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.eightBtn.setFont(font)
        self.eightBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.eightBtn.setAutoRepeat(True)
        self.eightBtn.setObjectName("eightBtn")
        self.horizontalLayout.addWidget(self.eightBtn)
        self.nineBtn = TouchButton(VirtualKeyboard)
        self.nineBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.nineBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.nineBtn.setFont(font)
        self.nineBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.nineBtn.setAutoRepeat(True)
        self.nineBtn.setObjectName("nineBtn")
        self.horizontalLayout.addWidget(self.nineBtn)
        self.zeroBtn = TouchButton(VirtualKeyboard)
        self.zeroBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.zeroBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.zeroBtn.setFont(font)
        self.zeroBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zeroBtn.setAutoRepeat(True)
        self.zeroBtn.setObjectName("zeroBtn")
        self.horizontalLayout.addWidget(self.zeroBtn)
        self.minusBtn = TouchButton(VirtualKeyboard)
        self.minusBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.minusBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.minusBtn.setFont(font)
        self.minusBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.minusBtn.setAutoRepeat(True)
        self.minusBtn.setObjectName("minusBtn")
        self.horizontalLayout.addWidget(self.minusBtn)
        self.equalBtn = TouchButton(VirtualKeyboard)
        self.equalBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.equalBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.equalBtn.setFont(font)
        self.equalBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.equalBtn.setAutoRepeat(True)
        self.equalBtn.setObjectName("equalBtn")
        self.horizontalLayout.addWidget(self.equalBtn)
        self.backspaceBtn = TouchButton(VirtualKeyboard)
        self.backspaceBtn.setMinimumSize(QtCore.QSize(88, 48))
        self.backspaceBtn.setMaximumSize(QtCore.QSize(88, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.backspaceBtn.setFont(font)
        self.backspaceBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.backspaceBtn.setAutoRepeat(True)
        self.backspaceBtn.setObjectName("backspaceBtn")
        self.horizontalLayout.addWidget(self.backspaceBtn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.capsBtn = TouchButton(VirtualKeyboard)
        self.capsBtn.setMinimumSize(QtCore.QSize(80, 48))
        self.capsBtn.setMaximumSize(QtCore.QSize(80, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.capsBtn.setFont(font)
        self.capsBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.capsBtn.setCheckable(True)
        self.capsBtn.setObjectName("capsBtn")
        self.horizontalLayout_3.addWidget(self.capsBtn)
        self.aBtn = TouchButton(VirtualKeyboard)
        self.aBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.aBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.aBtn.setFont(font)
        self.aBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.aBtn.setAutoRepeat(True)
        self.aBtn.setObjectName("aBtn")
        self.horizontalLayout_3.addWidget(self.aBtn)
        self.sBtn = TouchButton(VirtualKeyboard)
        self.sBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.sBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.sBtn.setFont(font)
        self.sBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sBtn.setAutoRepeat(True)
        self.sBtn.setObjectName("sBtn")
        self.horizontalLayout_3.addWidget(self.sBtn)
        self.dBtn = TouchButton(VirtualKeyboard)
        self.dBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.dBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.dBtn.setFont(font)
        self.dBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dBtn.setAutoRepeat(True)
        self.dBtn.setObjectName("dBtn")
        self.horizontalLayout_3.addWidget(self.dBtn)
        self.fBtn = TouchButton(VirtualKeyboard)
        self.fBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.fBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.fBtn.setFont(font)
        self.fBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fBtn.setAutoRepeat(True)
        self.fBtn.setObjectName("fBtn")
        self.horizontalLayout_3.addWidget(self.fBtn)
        self.gBtn = TouchButton(VirtualKeyboard)
        self.gBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.gBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.gBtn.setFont(font)
        self.gBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gBtn.setAutoRepeat(True)
        self.gBtn.setObjectName("gBtn")
        self.horizontalLayout_3.addWidget(self.gBtn)
        self.hBtn = TouchButton(VirtualKeyboard)
        self.hBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.hBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.hBtn.setFont(font)
        self.hBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.hBtn.setAutoRepeat(True)
        self.hBtn.setObjectName("hBtn")
        self.horizontalLayout_3.addWidget(self.hBtn)
        self.jBtn = TouchButton(VirtualKeyboard)
        self.jBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.jBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.jBtn.setFont(font)
        self.jBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.jBtn.setAutoRepeat(True)
        self.jBtn.setObjectName("jBtn")
        self.horizontalLayout_3.addWidget(self.jBtn)
        self.kBtn = TouchButton(VirtualKeyboard)
        self.kBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.kBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.kBtn.setFont(font)
        self.kBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.kBtn.setAutoRepeat(True)
        self.kBtn.setObjectName("kBtn")
        self.horizontalLayout_3.addWidget(self.kBtn)
        self.lBtn = TouchButton(VirtualKeyboard)
        self.lBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.lBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.lBtn.setFont(font)
        self.lBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lBtn.setAutoRepeat(True)
        self.lBtn.setObjectName("lBtn")
        self.horizontalLayout_3.addWidget(self.lBtn)
        self.semicolonBtn = TouchButton(VirtualKeyboard)
        self.semicolonBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.semicolonBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.semicolonBtn.setFont(font)
        self.semicolonBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.semicolonBtn.setAutoRepeat(True)
        self.semicolonBtn.setObjectName("semicolonBtn")
        self.horizontalLayout_3.addWidget(self.semicolonBtn)
        self.quoteBtn = TouchButton(VirtualKeyboard)
        self.quoteBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.quoteBtn.setMaximumSize(QtCore.QSize(48, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.quoteBtn.setFont(font)
        self.quoteBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.quoteBtn.setAutoRepeat(True)
        self.quoteBtn.setObjectName("quoteBtn")
        self.horizontalLayout_3.addWidget(self.quoteBtn)
        self.enterBtn = TouchButton(VirtualKeyboard)
        self.enterBtn.setMinimumSize(QtCore.QSize(100, 48))
        self.enterBtn.setMaximumSize(QtCore.QSize(100, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.enterBtn.setFont(font)
        self.enterBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.enterBtn.setObjectName("enterBtn")
        self.horizontalLayout_3.addWidget(self.enterBtn)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.suggestionsListView = QtWidgets.QListView(VirtualKeyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.suggestionsListView.sizePolicy().hasHeightForWidth())
        self.suggestionsListView.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.suggestionsListView.setFont(font)
        self.suggestionsListView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.suggestionsListView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.suggestionsListView.setObjectName("suggestionsListView")
        self.gridLayout.addWidget(self.suggestionsListView, 1, 0, 1, 1)

        self.retranslateUi(VirtualKeyboard)
        QtCore.QMetaObject.connectSlotsByName(VirtualKeyboard)

    def retranslateUi(self, VirtualKeyboard):
        _translate = QtCore.QCoreApplication.translate
        VirtualKeyboard.setWindowTitle(_translate("VirtualKeyboard", "Form"))
        self.clearBtn.setText(_translate("VirtualKeyboard", "Clear"))
        self.spaceBarBtn.setText(_translate("VirtualKeyboard", "Space Bar"))
        self.leftBtn.setText(_translate("VirtualKeyboard", "←"))
        self.rightBtn.setText(_translate("VirtualKeyboard", "→"))
        self.leftShiftBtn.setText(_translate("VirtualKeyboard", "Shift"))
        self.zBtn.setText(_translate("VirtualKeyboard", "z"))
        self.xBtn.setText(_translate("VirtualKeyboard", "x"))
        self.cBtn.setText(_translate("VirtualKeyboard", "c"))
        self.vBtn.setText(_translate("VirtualKeyboard", "v"))
        self.bBtn.setText(_translate("VirtualKeyboard", "b"))
        self.nBtn.setText(_translate("VirtualKeyboard", "n"))
        self.mBtn.setText(_translate("VirtualKeyboard", "m"))
        self.commaBtn.setText(_translate("VirtualKeyboard", ","))
        self.periodBtn.setText(_translate("VirtualKeyboard", "."))
        self.forwardSlashBtn.setText(_translate("VirtualKeyboard", "/"))
        self.rightShiftBtn.setText(_translate("VirtualKeyboard", "Shift"))
        self.tabBtn.setText(_translate("VirtualKeyboard", "Tab"))
        self.qBtn.setText(_translate("VirtualKeyboard", "q"))
        self.wBtn.setText(_translate("VirtualKeyboard", "w"))
        self.eBtn.setText(_translate("VirtualKeyboard", "e"))
        self.rBtn.setText(_translate("VirtualKeyboard", "r"))
        self.tBtn.setText(_translate("VirtualKeyboard", "t"))
        self.yBtn.setText(_translate("VirtualKeyboard", "y"))
        self.uBtn.setText(_translate("VirtualKeyboard", "u"))
        self.iBtn.setText(_translate("VirtualKeyboard", "i"))
        self.oBtn.setText(_translate("VirtualKeyboard", "o"))
        self.pBtn.setText(_translate("VirtualKeyboard", "p"))
        self.leftBraceBtn.setText(_translate("VirtualKeyboard", "["))
        self.rightBraceBtn.setText(_translate("VirtualKeyboard", "]"))
        self.backSlashBtn.setText(_translate("VirtualKeyboard", "\\"))
        self.tildeBtn.setText(_translate("VirtualKeyboard", "`"))
        self.oneBtn.setText(_translate("VirtualKeyboard", "1"))
        self.twoBtn.setText(_translate("VirtualKeyboard", "2"))
        self.threeBtn.setText(_translate("VirtualKeyboard", "3"))
        self.fourBtn.setText(_translate("VirtualKeyboard", "4"))
        self.fiveBtn.setText(_translate("VirtualKeyboard", "5"))
        self.sixBtn.setText(_translate("VirtualKeyboard", "6"))
        self.sevenBtn.setText(_translate("VirtualKeyboard", "7"))
        self.eightBtn.setText(_translate("VirtualKeyboard", "8"))
        self.nineBtn.setText(_translate("VirtualKeyboard", "9"))
        self.zeroBtn.setText(_translate("VirtualKeyboard", "0"))
        self.minusBtn.setText(_translate("VirtualKeyboard", "-"))
        self.equalBtn.setText(_translate("VirtualKeyboard", "="))
        self.backspaceBtn.setText(_translate("VirtualKeyboard", "Bksp"))
        self.capsBtn.setText(_translate("VirtualKeyboard", "Caps"))
        self.aBtn.setText(_translate("VirtualKeyboard", "a"))
        self.sBtn.setText(_translate("VirtualKeyboard", "s"))
        self.dBtn.setText(_translate("VirtualKeyboard", "d"))
        self.fBtn.setText(_translate("VirtualKeyboard", "f"))
        self.gBtn.setText(_translate("VirtualKeyboard", "g"))
        self.hBtn.setText(_translate("VirtualKeyboard", "h"))
        self.jBtn.setText(_translate("VirtualKeyboard", "j"))
        self.kBtn.setText(_translate("VirtualKeyboard", "k"))
        self.lBtn.setText(_translate("VirtualKeyboard", "l"))
        self.semicolonBtn.setText(_translate("VirtualKeyboard", ";"))
        self.quoteBtn.setText(_translate("VirtualKeyboard", "\'"))
        self.enterBtn.setText(_translate("VirtualKeyboard", "Enter"))

from Widgets.touchButton import TouchButton
import Resource_BY_rc
import style_rc
