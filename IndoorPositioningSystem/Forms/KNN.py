from Source.use_algorithms import AlgorithmOperation
from sklearn.neighbors import KNeighborsClassifier

from Forms.MainForm import *


class Ui_FormSetKNNParam(object):
    def setupUi(self, FormSetKNNParam):
        FormSetKNNParam.setObjectName("FormSetKNNParam")
        FormSetKNNParam.resize(352, 309)
        FormSetKNNParam.setStyleSheet("QMainWindow{\n"
"\n"
"background-color:#fcfdff;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(FormSetKNNParam)
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
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setIndent(15)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txtN_Neighbors = QtWidgets.QLineEdit(self.centralwidget)
        self.txtN_Neighbors.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtN_Neighbors.setObjectName("txtN_Neighbors")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtN_Neighbors)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setIndent(15)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.txtWeights = QtWidgets.QLineEdit(self.centralwidget)
        self.txtWeights.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtWeights.setObjectName("txtWeights")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtWeights)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setIndent(15)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.txtLeafSize = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLeafSize.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtLeafSize.setObjectName("txtLeafSize")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtLeafSize)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setIndent(15)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.txtP = QtWidgets.QLineEdit(self.centralwidget)
        self.txtP.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtP.setObjectName("txtP")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtP)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setIndent(15)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.txtMetric = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMetric.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtMetric.setObjectName("txtMetric")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtMetric)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setIndent(15)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.txtN_Jobs = QtWidgets.QLineEdit(self.centralwidget)
        self.txtN_Jobs.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtN_Jobs.setObjectName("txtN_Jobs")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtN_Jobs)
        self.btnSetParamKNN = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSetParamKNN.sizePolicy().hasHeightForWidth())
        self.btnSetParamKNN.setSizePolicy(sizePolicy)
        self.btnSetParamKNN.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnSetParamKNN.setFont(font)
        self.btnSetParamKNN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSetParamKNN.setStyleSheet("QPushButton {\n"
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
        self.btnSetParamKNN.setIcon(icon)
        self.btnSetParamKNN.setIconSize(QtCore.QSize(18, 18))
        self.btnSetParamKNN.setObjectName("btnSetParamKNN")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.btnSetParamKNN)
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
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.btnCancel)
        self.horizontalLayout_15.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        FormSetKNNParam.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormSetKNNParam)
        self.statusbar.setObjectName("statusbar")
        FormSetKNNParam.setStatusBar(self.statusbar)


        #button operations

        self.btnSetParamKNN.clicked.connect(lambda:self.btnKNNClicked(self.txtN_Neighbors.text(),
                                                                      self.txtWeights.text(),
                                                                      self.txtLeafSize.text(),
                                                                      self.txtP.text(),
                                                                      self.txtMetric.text(),
                                                                      self.txtN_Jobs.text(),
                                                                      FormSetKNNParam))
        self.btnCancel.clicked.connect(FormSetKNNParam.close)

        self.retranslateUi(FormSetKNNParam)
        QtCore.QMetaObject.connectSlotsByName(FormSetKNNParam)


    def retranslateUi(self, FormSetKNNParam):
        _translate = QtCore.QCoreApplication.translate
        FormSetKNNParam.setWindowTitle(_translate("FormSetKNNParam", "K-Nearest Neighbors"))
        self.label_10.setText(_translate("FormSetKNNParam", "Set or Use Default Parameter"))
        self.label_4.setText(_translate("FormSetKNNParam", "n_Neighbors:"))
        self.txtN_Neighbors.setText(_translate("FormSetKNNParam", "5"))
        self.label_5.setText(_translate("FormSetKNNParam", "weights :"))
        self.txtWeights.setText(_translate("FormSetKNNParam", "uniform"))
        self.label_6.setText(_translate("FormSetKNNParam", "leaf_size :"))
        self.txtLeafSize.setText(_translate("FormSetKNNParam", "30"))
        self.label_7.setText(_translate("FormSetKNNParam", "p :"))
        self.txtP.setText(_translate("FormSetKNNParam", "2"))
        self.label_8.setText(_translate("FormSetKNNParam", "metric"))
        self.txtMetric.setText(_translate("FormSetKNNParam", "minkowski"))
        self.label_9.setText(_translate("FormSetKNNParam", "n_jobs :"))
        self.txtN_Jobs.setText(_translate("FormSetKNNParam", "1"))
        self.btnSetParamKNN.setText(_translate("FormSetKNNParam", "Set && Run"))
        self.btnCancel.setText(_translate("FormSetKNNParam", "Cancel"))

    def btnKNNClicked(self,k,weights,leaf_size,p,metric,n_jobs,FormSetKNNParam):

        self.algorithm = KNeighborsClassifier(int(k),weights,leaf_size=int(leaf_size),p=int(p)
                                              ,metric=metric,metric_params=None,n_jobs=int(n_jobs))
        AlgorithmOperation.ApplyAlgorithm(self.algorithm)

        self.messageBox(FormSetKNNParam)


    def messageBox(self,FormSetKNNParam):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Algorithm Succesfully Set and Run")
        msg.setWindowTitle("Information")
        msg.setDetailedText(str(self.algorithm))
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()
        FormSetKNNParam.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormSetKNNParam = QtWidgets.QMainWindow()
    ui = Ui_FormSetKNNParam()
    ui.setupUi(FormSetKNNParam)
    FormSetKNNParam.show()
    sys.exit(app.exec_())

