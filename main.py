import sys
from PyQt5 import QtWidgets, QtGui
from System import Ui_Form
from ADDGUI import Ui_Dialog
from UPDATEGUI import Ui_Dialog2
from PyQt5.QtCore import QStringListModel

class MainGUI(QtWidgets.QWidget, Ui_Form):

    def __init__(self):
        super(MainGUI, self).__init__()
        self.setupUi(self)
        self.__read_file__()
        slm = QStringListModel()
        self.__s__ = set()
        for plist in self.__P__:
            for p in plist:
                self.__s__.add(p)
        self.__s__ = list(self.__s__)
        slm.setStringList(self.__s__)
        self.listView.setModel(slm)
        self.listView.clicked.connect(self.select)

    def __read_file__(self):
        self.__P__ = []
        self.__Q__ = []
        with open("P.txt", 'r', encoding='utf-8') as f:
            while True:
                lines = f.readline().split('\n')[0]
                if not lines:
                    break
                self.__P__.append(lines.split('/'))
        with open("Q.txt", 'r', encoding='utf-8') as f:
            while True:
                lines = f.readline().split('\n')[0]
                if not lines:
                    break
                self.__Q__.append(lines)

    def start(self):
        str = self.fact.toPlainText().split('\n')
        self.__DB__ = str
        self.__read_file__()
        self.procedure.setText("----开始识别----")
        self.procedure.append('采用正向推理的方法')
        self.inference()
        self.procedure.append('----识别完成----')
        self.result.setText(self.__result__)

    def is_include_in_DB(self, p):
        for i in p:
            if i not in self.__DB__:
                return False
        return True

    def inference(self):
        self.__result__ = '无法识别'
        flag = False
        for i, p in enumerate(self.__P__):
            if self.is_include_in_DB(p):
                self.__DB__.append(self.__Q__[i])
                self.__result__ = self.__Q__[i]
                self.procedure.append('%s -> %s' % (p, self.__Q__[i]))
                flag = True
        if flag:
            pix = QtGui.QPixmap(self.__result__+".jpg")
            print(self.__result__+".jpg")
            self.label_5.setPixmap(pix)

    def add(self):
        pass

    def select(self, qModelIndex):
        self.fact.append(self.__s__[qModelIndex.row()])


class AddGUI(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(AddGUI, self).__init__()
        self.setupUi(self)

    def accept(self):
        DB = self.textEdit.toPlainText().split('\n')
        P = []
        Q = []
        for d in DB:
            d = d.split('>')
            P.append(d[0])
            Q.append(d[1])
        self.write(P,Q)
        self.close()

    def write(self, P, Q):
        with open("Q.txt", 'a+', encoding='utf-8') as f:
            for q in Q:
                f.write("\n"+q)
        with open("P.txt", 'a+', encoding='utf-8') as f:
            for p in P:
                f.write("\n"+p)

class UpdateGui(QtWidgets.QDialog, Ui_Dialog2):
    def __init__(self):
        super(UpdateGui, self).__init__()
        self.setupUi(self)
        self.__read_file__()
        self.slm1 = QStringListModel()
        self.slm1.setStringList(self.__P__)
        self.PList.setModel(self.slm1)
        self.slm2 = QStringListModel()
        self.slm2.setStringList(self.__Q__)
        self.listView_2.setModel(self.slm2)

    def accept(self):
        self.__P__ = self.slm1.stringList()
        self.__Q__ = self.slm2.stringList()
        self.write(self.__P__, self.__Q__)
        self.close()

    def delete(self):
        select = self.PList.currentIndex().row()
        self.__P__.pop(select)
        self.__Q__.pop(select)
        slm1 = QStringListModel()
        slm1.setStringList(self.__P__)
        self.PList.setModel(slm1)
        slm2 = QStringListModel()
        slm2.setStringList(self.__Q__)
        self.listView_2.setModel(slm2)

    def write(self, P, Q):
        with open("Q.txt", 'w', encoding='utf-8') as f:
            for q in Q:
                f.write("\n"+q)
        with open("P.txt", 'w', encoding='utf-8') as f:
            for p in P:
                f.write("\n"+p)

    def __read_file__(self):
        self.__P__ = []
        self.__Q__ = []
        with open("P.txt", 'r', encoding='utf-8') as f:
            while True:
                lines = f.readline().split('\n')[0]
                if not lines:
                    break
                self.__P__.append(lines)
        with open("Q.txt", 'r', encoding='utf-8') as f:
            while True:
                lines = f.readline().split('\n')[0]
                if not lines:
                    break
                self.__Q__.append(lines)

    def write(self, P, Q):
        with open("Q.txt", 'a+', encoding='utf-8') as f:
            for q in Q:
                f.write("\n"+q)
        with open("P.txt", 'a+', encoding='utf-8') as f:
            for p in P:
                f.write("\n"+p)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainGUI = MainGUI()
    child1 = AddGUI()
    btn = mainGUI.pushButton
    btn.clicked.connect(child1.show)
    child2 = UpdateGui()
    btn2 = mainGUI.update
    btn2.clicked.connect(child2.show)
    mainGUI.show()
    sys.exit(app.exec())