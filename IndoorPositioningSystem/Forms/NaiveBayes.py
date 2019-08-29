from PyQt5 import QtCore, QtGui, QtWidgets
from sklearn.naive_bayes import GaussianNB

from Source.use_algorithms import AlgorithmOperation


class Ui_FormSetNaiveBayesParam(object):
    def setupUi(self, FormSetNaiveBayesParam):
        FormSetNaiveBayesParam.setObjectName("FormSetNaiveBayesParam")
        FormSetNaiveBayesParam.resize(352, 150)
        FormSetNaiveBayesParam.setStyleSheet("QMainWindow{\n"
"\n"
"background-color:#fcfdff;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(FormSetNaiveBayesParam)
        self.centralwidget.setStyleSheet("QWidget{\n"
"\n"
"background-color:#fcfdff;\n"
"\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel{\n"
"\n"
"background-color:#f7f7f7;\n"
"}")
        self.label_10.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setIndent(15)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txtPriors = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPriors.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtPriors.setObjectName("txtPriors")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtPriors)
        self.btnSetParamNavB = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSetParamNavB.sizePolicy().hasHeightForWidth())
        self.btnSetParamNavB.setSizePolicy(sizePolicy)
        self.btnSetParamNavB.setMinimumSize(QtCore.QSize(120, 30))
        self.btnSetParamNavB.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSetParamNavB.setFont(font)
        self.btnSetParamNavB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSetParamNavB.setAutoFillBackground(False)
        self.btnSetParamNavB.setStyleSheet("QPushButton {\n"
"    background-color:#dbc7c7;\n"
"    color: #4c4c4c;\n"
"    border: 2px #efe3e3;\n"
"    border-style: outset;\n"
"    border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover {background-color:#f9e3e3;}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSetParamNavB.setIcon(icon)
        self.btnSetParamNavB.setIconSize(QtCore.QSize(20, 18))
        self.btnSetParamNavB.setObjectName("btnSetParamNavB")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btnSetParamNavB)
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setMinimumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnCancel.setFont(font)
        self.btnCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancel.setStyleSheet("QPushButton {\n"
"    background-color:#dbc7c7;\n"
"    color: #4c4c4c;\n"
"    border: 2px #efe3e3;\n"
"    border-style: outset;\n"
"    border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover {background-color:#f9e3e3;}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon1)
        self.btnCancel.setIconSize(QtCore.QSize(12, 12))
        self.btnCancel.setObjectName("btnCancel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.btnCancel)
        self.horizontalLayout_15.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        self.horizontalLayout.addLayout(self.verticalLayout_8)

        #button operations
        self.btnCancel.clicked.connect(FormSetNaiveBayesParam.close)
        self.btnSetParamNavB.clicked.connect(lambda : self.btnNaiveBayesClicked(self.txtPriors.text(),FormSetNaiveBayesParam))


        FormSetNaiveBayesParam.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormSetNaiveBayesParam)
        self.statusbar.setObjectName("statusbar")
        FormSetNaiveBayesParam.setStatusBar(self.statusbar)

        self.retranslateUi(FormSetNaiveBayesParam)
        QtCore.QMetaObject.connectSlotsByName(FormSetNaiveBayesParam)

    def retranslateUi(self, FormSetNaiveBayesParam):
        _translate = QtCore.QCoreApplication.translate
        FormSetNaiveBayesParam.setWindowTitle(_translate("FormSetNaiveBayesParam", "Naive Bayes"))
        self.label_10.setText(_translate("FormSetNaiveBayesParam", "Set or Use Default Parameter"))
        self.label_4.setText(_translate("FormSetNaiveBayesParam", "priors:"))
        self.txtPriors.setText(_translate("FormSetNaiveBayesParam", "None"))
        self.txtPriors.setText(_translate("FormSetNaiveBayesParam", "None"))
        self.btnSetParamNavB.setText(_translate("FormSetNaiveBayesParam", "Set && Run"))
        self.btnCancel.setText(_translate("FormSetNaiveBayesParam", "Cancel"))

    def btnNaiveBayesClicked(self,priors,FormSetNaiveBayesParam):

        if priors.upper() == "NONE":
            priors=None
        self.algorithm=GaussianNB(priors=priors)
        AlgorithmOperation.ApplyAlgorithm(self.algorithm)
        self.messageBox(FormSetNaiveBayesParam)

    def messageBox(self,FormSetNaiveBayesParam):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Algorithm Succesfully Set and Run")
        msg.setWindowTitle("Information")
        msg.setDetailedText(str(self.algorithm))
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()
        FormSetNaiveBayesParam.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormSetNaiveBayesParam = QtWidgets.QMainWindow()
    ui = Ui_FormSetNaiveBayesParam()
    ui.setupUi(FormSetNaiveBayesParam)
    FormSetNaiveBayesParam.show()
    sys.exit(app.exec_())

