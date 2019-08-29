from PyQt5 import QtCore, QtGui, QtWidgets
from sklearn.svm import SVC

from Source.use_algorithms import AlgorithmOperation


class Ui_FormSetParamSVC(object):
    def setupUi(self, FormSetParamSVC):
        FormSetParamSVC.setObjectName("FormSetParamSVC")
        FormSetParamSVC.resize(362, 285)
        FormSetParamSVC.setStyleSheet("QMainWindow{\n"
"\n"
"background-color:#fcfdff;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(FormSetParamSVC)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
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
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setIndent(15)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.txtKernel = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtKernel.setFont(font)
        self.txtKernel.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtKernel.setObjectName("txtKernel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtKernel)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setIndent(15)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.txtGamma = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtGamma.setFont(font)
        self.txtGamma.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtGamma.setObjectName("txtGamma")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtGamma)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setIndent(15)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.txtTol = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtTol.setFont(font)
        self.txtTol.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtTol.setObjectName("txtTol")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtTol)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setIndent(15)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.txtVerbose = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtVerbose.setFont(font)
        self.txtVerbose.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtVerbose.setObjectName("txtVerbose")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtVerbose)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtRandomState = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtRandomState.setFont(font)
        self.txtRandomState.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtRandomState.setObjectName("txtRandomState")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtRandomState)
        self.btnSetParamSVC = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetParamSVC.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnSetParamSVC.setFont(font)
        self.btnSetParamSVC.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSetParamSVC.setStyleSheet("QPushButton {\n"
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
        self.btnSetParamSVC.setIcon(icon)
        self.btnSetParamSVC.setIconSize(QtCore.QSize(18, 18))
        self.btnSetParamSVC.setObjectName("btnSetParamSVC")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.btnSetParamSVC)
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
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.btnCancel)
        self.horizontalLayout_15.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        FormSetParamSVC.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormSetParamSVC)
        self.statusbar.setObjectName("statusbar")
        FormSetParamSVC.setStatusBar(self.statusbar)
        #button operations
        self.btnCancel.clicked.connect(FormSetParamSVC.close)
        self.btnSetParamSVC.clicked.connect(lambda:self.btnSVCClicked(self.txtKernel.text(),
                                                                       self.txtGamma.text(),
                                                                       self.txtTol.text(),
                                                                       self.txtVerbose.text(),
                                                                       self.txtRandomState.text(),
                                                                      FormSetParamSVC))
        self.retranslateUi(FormSetParamSVC)
        QtCore.QMetaObject.connectSlotsByName(FormSetParamSVC)

    def retranslateUi(self, FormSetParamSVC):
        _translate = QtCore.QCoreApplication.translate
        FormSetParamSVC.setWindowTitle(_translate("FormSetParamSVC", "SVC"))
        self.label_10.setText(_translate("FormSetParamSVC", "Set or Use Default Parameter"))
        self.label_5.setText(_translate("FormSetParamSVC", "kernel :"))
        self.txtKernel.setText(_translate("FormSetParamSVC", "rbf"))
        self.label_6.setText(_translate("FormSetParamSVC", "gamma :"))
        self.txtGamma.setText(_translate("FormSetParamSVC", "auto"))
        self.label_7.setText(_translate("FormSetParamSVC", "tol :"))
        self.txtTol.setText(_translate("FormSetParamSVC", "0.001"))
        self.label_8.setText(_translate("FormSetParamSVC", "verbose :"))
        self.txtVerbose.setText(_translate("FormSetParamSVC", "False"))
        self.label_3.setText(_translate("FormSetParamSVC", "random_state :"))
        self.txtRandomState.setText(_translate("FormSetParamSVC", "None"))
        self.btnSetParamSVC.setText(_translate("FormSetParamSVC", "Set && Run"))
        self.btnCancel.setText(_translate("FormSetParamSVC", "Cancel"))

    def btnSVCClicked(self,kernel,gamma, tol, verbose, random_state,FormSetParamSVC):

        if random_state.upper() =="NONE":
            random_state=None
        self.algorithm = SVC(kernel=kernel,gamma=gamma,tol=float(tol),verbose=bool(verbose),random_state=random_state)
        AlgorithmOperation.ApplyAlgorithm(self.algorithm)
        self.messageBox(FormSetParamSVC)

    def btnCancelClicked(self):
        FormSetParamSVC.close()

    def messageBox(self,FormSetParamSVC):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Algorithm Succesfully Set and Run")
        msg.setWindowTitle("Information")
        msg.setDetailedText(str(self.algorithm))
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()
        FormSetParamSVC.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormSetParamSVC = QtWidgets.QMainWindow()
    ui = Ui_FormSetParamSVC()
    ui.setupUi(FormSetParamSVC)
    FormSetParamSVC.show()
    sys.exit(app.exec_())

