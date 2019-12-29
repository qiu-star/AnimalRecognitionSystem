# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UPDATEGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(819, 565)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(730, 460, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(360, 10, 251, 61))
        self.label.setStyleSheet("font: 16pt \"方正颜宋简体\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 80, 31, 21))
        self.label_2.setStyleSheet("font: 9pt \"方正颜宋简体\";\n"
"color: rgb(85, 85, 85);")
        self.label_2.setObjectName("label_2")
        self.PList = QtWidgets.QListView(Dialog)
        self.PList.setGeometry(QtCore.QRect(80, 120, 256, 331))
        self.PList.setObjectName("PList")
        self.listView_2 = QtWidgets.QListView(Dialog)
        self.listView_2.setGeometry(QtCore.QRect(460, 120, 256, 331))
        self.listView_2.setObjectName("listView_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(560, 80, 31, 21))
        self.label_3.setStyleSheet("font: 9pt \"方正颜宋简体\";\n"
"color: rgb(85, 85, 85);")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 480, 131, 41))
        self.pushButton.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.pushButton.clicked.connect(Dialog.delete)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "规则库"))
        self.label_2.setText(_translate("Dialog", "P"))
        self.label_3.setText(_translate("Dialog", "Q"))
        self.pushButton.setText(_translate("Dialog", "删除"))
