from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import SIGNAL, QObject
from ui import main
from LinkedList import *

LList = linked_list()


class FirstWindow(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(FirstWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("База данных компании")
        self.buttonSave.clicked.connect(self.saveListFromTree)
        self.buttonAddMember.clicked.connect(self.populate_treeWidget)
        self.buttonGetList.clicked.connect(self.getTreeFromFile)
        self.buttonChangeMember.clicked.connect(self.memberChange)
        self.buttonDel.clicked.connect(self.delMember)
        self.buttonInfo.clicked.connect(self.getInfo)
        self.buttonSortOklad.clicked.connect(self.setOkladSortedToFile)
        self.buttonSortName.clicked.connect(self.setNameSortedToFile)
        self.buttonSortAge.clicked.connect(self.setAgeSortedToFile)

    def populate_treeWidget(self):
        lastName = self.lastName_LE.text()
        IO = self.IO_LE.text()
        year = self.Year_LE.text()
        oklad = self.Oklad_LE.text()
        if not lastName or not IO:
            QtWidgets.QMessageBox.about(self, "Неверные данные!", "Заполните все поля!")
            return 0
        if not self.isInt(year) or not self.isInt(oklad):
            QtWidgets.QMessageBox.about(self, "Неверные данные!", "Введите числа в поля Оклад и Год рождения!")
            return 0
        new_member = node(lastName, IO, int(year), int(oklad))
        LList.append(new_member)

        item = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item.setText(0, new_member.getLastName())
        item.setText(1, new_member.getIO())
        item.setText(2, str(new_member.getYear()))
        item.setText(3, str(new_member.getOklad()))

        QtWidgets.QMessageBox.about(self, "Успешно!", "Сотрудник добавлен в таблицу!")

        self.clearLE()

    def get_subtree_nodes(self, tree_widget_item):
        nodes = []
        nodes.append(tree_widget_item)
        for i in range(tree_widget_item.childCount()):
            nodes.extend(self.get_subtree_nodes(tree_widget_item.child(i)))
        return nodes

    def memberChange(self):
        lastName = self.lastNameChange_LE.text()
        IO = self.IOChange_LE.text()
        year = self.YearChange_LE.text()
        oklad = self.OkladChange_LE.text()

        if not lastName or not IO:
            QtWidgets.QMessageBox.about(self, "Неверные данные!", "Заполните все поля!")
            return 0
        if not self.isInt(year) or not self.isInt(oklad):
            QtWidgets.QMessageBox.about(self, "Неверные данные!", "Введите числа в поля Оклад и Год рождения!")
            return 0

        new_member = node(lastName, IO, int(year), int(oklad))

        item = self.treeWidget.currentItem()
        index = self.treeWidget.currentIndex().row()
        item.setText(0, new_member.getLastName())
        item.setText(1, new_member.getIO())
        item.setText(2, str(new_member.getYear()))
        item.setText(3, str(new_member.getOklad()))

        LList.erase(index)
        LList.insert(index + 1, new_member)

        self.clearLE()

    def delMember(self):
        item = self.treeWidget.currentItem()
        index = self.treeWidget.currentIndex().row()
        print(index)
        LList.erase(index)

        self.saveListFromTree()
        self.getTreeFromFile()

    def saveListFromTree(self):
        with open('list000.txt', 'wb'):
            pass

        LList.printToFile()
        QtWidgets.QMessageBox.about(self, "Успешно!", "Таблица сохранена в файл!")

    def getInfo(self):
        item = self.treeWidget.currentItem()
        index = self.treeWidget.currentIndex().row()

        QtWidgets.QMessageBox.about(self, "Информация", "Фамилия: " + LList[index].getLastName() + "\n" +
                                    "Инициалы: " + LList[index].getIO() + "\n" +
                                    "Год рождения: " + str(LList[index].getYear()) + "\n" +
                                    "Оклад: " + str(LList[index].getOklad()))

    def getTreeFromFile(self):
        self.treeWidget.clear()
        f = open('list000.txt', 'r')
        line = f.readline()
        LList.__init__()
        while line:
            words = line.split()
            new_member = node(words[0], words[1], words[2], words[3])
            LList.append(new_member)

            item = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item.setText(0, new_member.getLastName())
            item.setText(1, new_member.getIO())
            item.setText(2, str(new_member.getYear()))
            item.setText(3, str(new_member.getOklad()))

            LList.display()

            line = f.readline()
        f.close()

    def setOkladSortedToFile(self):
        with open('list000.txt', 'wb'):
            pass

        LList.sortOklad()
        self.getTreeFromFile()

    def setNameSortedToFile(self):
        with open('list000.txt', 'wb'):
            pass

        LList.sortName()
        self.getTreeFromFile()

    def setAgeSortedToFile(self):
        with open('list000.txt', 'wb'):
            pass

        LList.sortAge()
        self.getTreeFromFile()

    def isInt(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def clearLE(self):
        self.lastName_LE.clear()
        self.IO_LE.clear()
        self.Year_LE.clear()
        self.Oklad_LE.clear()
        self.lastNameChange_LE.clear()
        self.IOChange_LE.clear()
        self.YearChange_LE.clear()
        self.OkladChange_LE.clear()
