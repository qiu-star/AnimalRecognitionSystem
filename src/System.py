# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'System.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1392, 593)
        self.fact = QtWidgets.QTextEdit(Form)
        self.fact.setGeometry(QtCore.QRect(380, 160, 241, 321))
        self.fact.setStyleSheet("font: 12pt \"方正颜宋简体\";")
        self.fact.setObjectName("fact")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(570, 10, 371, 81))
        self.label.setStyleSheet("font: 36pt \"字酷堂清楷体\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(440, 110, 121, 31))
        self.label_2.setStyleSheet("font: 16pt \"方正颜宋简体\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(860, 110, 121, 31))
        self.label_3.setStyleSheet("font: 16pt \"方正颜宋简体\";")
        self.label_3.setObjectName("label_3")
        self.procedure = QtWidgets.QTextEdit(Form)
        self.procedure.setGeometry(QtCore.QRect(800, 160, 241, 321))
        self.procedure.setStyleSheet("font: 12pt \"方正颜宋简体\";")
        self.procedure.setObjectName("procedure")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(1180, 110, 121, 31))
        self.label_4.setStyleSheet("font: 16pt \"方正颜宋简体\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(1110, 160, 251, 311))
        self.label_5.setStyleSheet("image: url(:/pic/01.JPG);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.startBtn = QtWidgets.QPushButton(Form)
        self.startBtn.setGeometry(QtCore.QRect(640, 300, 141, 41))
        self.startBtn.setStyleSheet("font: 16pt \"方正颜宋简体\";")
        self.startBtn.setObjectName("startBtn")
        self.result = QtWidgets.QLabel(Form)
        self.result.setGeometry(QtCore.QRect(1190, 500, 251, 81))
        self.result.setStyleSheet("font: 16pt \"方正颜宋简体\";")
        self.result.setText("")
        self.result.setObjectName("result")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(340, 520, 151, 41))
        self.pushButton.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(70, 110, 181, 31))
        self.label_6.setStyleSheet("font: 16pt \"方正颜宋简体\";")
        self.label_6.setObjectName("label_6")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(30, 160, 256, 321))
        self.listView.setStyleSheet("font: 10pt \"方正颜宋简体\";")
        self.listView.setObjectName("listView")
        self.startBtn_2 = QtWidgets.QPushButton(Form)
        self.startBtn_2.setGeometry(QtCore.QRect(290, 290, 81, 41))
        self.startBtn_2.setStyleSheet("font: 16pt \"方正颜宋简体\";")
        self.startBtn_2.setObjectName("startBtn_2")
        self.update = QtWidgets.QPushButton(Form)
        self.update.setGeometry(QtCore.QRect(610, 520, 171, 41))
        self.update.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.update.setObjectName("update")

        self.retranslateUi(Form)
        self.startBtn.clicked.connect(Form.start)
        self.pushButton.clicked.connect(Form.add)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "动物识别系统"))
        self.label_2.setText(_translate("Form", "已选事实"))
        self.label_3.setText(_translate("Form", "推理过程"))
        self.label_4.setText(_translate("Form", "识别结果"))
        self.startBtn.setText(_translate("Form", "开始推理"))
        self.pushButton.setText(_translate("Form", "添加规则"))
        self.label_6.setText(_translate("Form", "选择动物特征"))
        self.startBtn_2.setText(_translate("Form", "选择"))
        self.update.setText(_translate("Form", "删除/修改规则"))
import image_rc
