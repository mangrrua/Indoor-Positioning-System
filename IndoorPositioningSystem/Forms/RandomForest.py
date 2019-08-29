from PyQt5 import QtCore, QtGui, QtWidgets
from sklearn.ensemble import RandomForestClassifier

from Source.use_algorithms import AlgorithmOperation


class Ui_FormSetRandomForestParam(object):
    def setupUi(self, FormSetRandomForestParam):
        FormSetRandomForestParam.setObjectName("FormSetRandomForestParam")
        FormSetRandomForestParam.resize(394, 404)
        FormSetRandomForestParam.setStyleSheet("QMainWindow{\n"
"\n"
"background-color:#fcfdff;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(FormSetRandomForestParam)
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
        self.txtN_Estimators = QtWidgets.QLineEdit(self.centralwidget)
        self.txtN_Estimators.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtN_Estimators.setObjectName("txtN_Estimators")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtN_Estimators)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setIndent(15)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.txtCriterion = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCriterion.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtCriterion.setObjectName("txtCriterion")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtCriterion)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setIndent(15)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.txtMaxDepth = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMaxDepth.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtMaxDepth.setObjectName("txtMaxDepth")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtMaxDepth)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setIndent(15)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.txtMinSamplesSplit = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMinSamplesSplit.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtMinSamplesSplit.setObjectName("txtMinSamplesSplit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtMinSamplesSplit)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setIndent(15)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.txtMinSamplesLeaf = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMinSamplesLeaf.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtMinSamplesLeaf.setObjectName("txtMinSamplesLeaf")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtMinSamplesLeaf)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setIndent(15)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.txtMinWeightFractionLeaf = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMinWeightFractionLeaf.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtMinWeightFractionLeaf.setObjectName("txtMinWeightFractionLeaf")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtMinWeightFractionLeaf)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtMinImpurityDcs = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMinImpurityDcs.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtMinImpurityDcs.setObjectName("txtMinImpurityDcs")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txtMinImpurityDcs)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtN_Jobs = QtWidgets.QLineEdit(self.centralwidget)
        self.txtN_Jobs.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtN_Jobs.setObjectName("txtN_Jobs")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.txtN_Jobs)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtRandomState = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRandomState.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtRandomState.setObjectName("txtRandomState")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.txtRandomState)
        self.btnSetParamRandomForest = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSetParamRandomForest.sizePolicy().hasHeightForWidth())
        self.btnSetParamRandomForest.setSizePolicy(sizePolicy)
        self.btnSetParamRandomForest.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnSetParamRandomForest.setFont(font)
        self.btnSetParamRandomForest.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSetParamRandomForest.setStyleSheet("QPushButton {\n"
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
        self.btnSetParamRandomForest.setIcon(icon)
        self.btnSetParamRandomForest.setIconSize(QtCore.QSize(18, 18))
        self.btnSetParamRandomForest.setObjectName("btnSetParamRandomForest")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.btnSetParamRandomForest)
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
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.btnCancel)
        self.horizontalLayout_15.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        FormSetRandomForestParam.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormSetRandomForestParam)
        self.statusbar.setObjectName("statusbar")
        FormSetRandomForestParam.setStatusBar(self.statusbar)

        #button operations
        self.btnCancel.clicked.connect(FormSetRandomForestParam.close)
        self.btnSetParamRandomForest.clicked.connect(lambda:self.btnRandomForestClicked(self.txtN_Estimators.text(),
                                                                                        self.txtCriterion.text(),
                                                                                        self.txtMaxDepth.text(),
                                                                                        self.txtMinSamplesSplit.text(),
                                                                                        self.txtMinSamplesLeaf.text(),
                                                                                        self.txtMinWeightFractionLeaf.text(),
                                                                                        self.txtMinImpurityDcs.text(),
                                                                                        self.txtN_Jobs.text(),
                                                                                        self.txtRandomState.text(),
                                                                                        FormSetRandomForestParam))

        self.retranslateUi(FormSetRandomForestParam)
        QtCore.QMetaObject.connectSlotsByName(FormSetRandomForestParam)

    def retranslateUi(self, FormSetRandomForestParam):
        _translate = QtCore.QCoreApplication.translate
        FormSetRandomForestParam.setWindowTitle(_translate("FormSetRandomForestParam", "Random Forest"))
        self.label_10.setText(_translate("FormSetRandomForestParam", "Set or Use Default Parameter"))
        self.label_4.setText(_translate("FormSetRandomForestParam", "n_estimators :"))
        self.txtN_Estimators.setText(_translate("FormSetRandomForestParam", "10"))
        self.label_5.setText(_translate("FormSetRandomForestParam", "criterion :"))
        self.txtCriterion.setText(_translate("FormSetRandomForestParam", "gini"))
        self.label_6.setText(_translate("FormSetRandomForestParam", "max_depth :"))
        self.txtMaxDepth.setText(_translate("FormSetRandomForestParam", "None"))
        self.label_7.setText(_translate("FormSetRandomForestParam", "min_samples_split :"))
        self.txtMinSamplesSplit.setText(_translate("FormSetRandomForestParam", "2"))
        self.label_8.setText(_translate("FormSetRandomForestParam", "min_samples_leaf :"))
        self.txtMinSamplesLeaf.setText(_translate("FormSetRandomForestParam", "1"))
        self.label_9.setText(_translate("FormSetRandomForestParam", "min_weight_fraction_leaf :"))
        self.txtMinWeightFractionLeaf.setText(_translate("FormSetRandomForestParam", "0.0"))
        self.label.setText(_translate("FormSetRandomForestParam", "min_impurity_decrease :"))
        self.txtMinImpurityDcs.setText(_translate("FormSetRandomForestParam", "0.0"))
        self.label_2.setText(_translate("FormSetRandomForestParam", "n_jobs :"))
        self.txtN_Jobs.setText(_translate("FormSetRandomForestParam", "1"))
        self.label_3.setText(_translate("FormSetRandomForestParam", "random_state :"))
        self.txtRandomState.setText(_translate("FormSetRandomForestParam", "None"))
        self.btnSetParamRandomForest.setText(_translate("FormSetRandomForestParam", "Set && Run"))
        self.btnCancel.setText(_translate("FormSetRandomForestParam", "Cancel"))

    def btnRandomForestClicked(self,n_estimators,criterion,max_depth,min_samples_split,min_samples_leaf,
                               min_weight_fraction_leaf,min_impurity_decrease,n_jobs,random_state,FormSetRandomForestParam):

        if random_state.upper()=="NONE":
            random_state=None
        if max_depth.upper()=="NONE":
            max_depth=None

        self.algorithm= RandomForestClassifier(int(n_estimators),criterion,max_depth,
                                               int(min_samples_split),int(min_samples_leaf),
                                               float(min_weight_fraction_leaf),
                                               min_impurity_decrease=float(min_impurity_decrease),
                                               n_jobs=int(n_jobs),random_state=random_state)
        AlgorithmOperation.ApplyAlgorithm(self.algorithm)
        self.messageBox(FormSetRandomForestParam)

    def messageBox(self,FormSetRandomForestParam):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Algorithm Succesfully Set and Run")
        msg.setWindowTitle("Information")
        msg.setDetailedText(str(self.algorithm))
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()
        FormSetRandomForestParam.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormSetRandomForestParam = QtWidgets.QMainWindow()
    ui = Ui_FormSetRandomForestParam()
    ui.setupUi(FormSetRandomForestParam)
    FormSetRandomForestParam.show()
    sys.exit(app.exec_())

