from PyQt5 import QtCore, QtGui, QtWidgets
from sklearn import tree

# for preparing algorithm
from Source.use_algorithms import AlgorithmOperation


class Ui_FormSetParamDecisionTree(object):
    def setupUi(self, FormSetParamDecisionTree):
        FormSetParamDecisionTree.setObjectName("FormSetParamDecisionTree")
        FormSetParamDecisionTree.resize(403, 339)
        FormSetParamDecisionTree.setAutoFillBackground(True)
        FormSetParamDecisionTree.setStyleSheet("QMainWindow{\n"
"\n"
"background-color:#fcfdff;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(FormSetParamDecisionTree)
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
        self.txtCriterion = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCriterion.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtCriterion.setObjectName("txtCriterion")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtCriterion)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setIndent(15)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.txtMaxDepth = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMaxDepth.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtMaxDepth.setObjectName("txtMaxDepth")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtMaxDepth)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setIndent(15)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.txtMinSamplesSplit = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMinSamplesSplit.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtMinSamplesSplit.setObjectName("txtMinSamplesSplit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtMinSamplesSplit)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setIndent(15)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.txtMinSamplesLeaf = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMinSamplesLeaf.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtMinSamplesLeaf.setObjectName("txtMinSamplesLeaf")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtMinSamplesLeaf)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setIndent(15)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.txtMinWeightFractionLeaf = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMinWeightFractionLeaf.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtMinWeightFractionLeaf.setObjectName("txtMinWeightFractionLeaf")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtMinWeightFractionLeaf)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtRandomState = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRandomState.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtRandomState.setObjectName("txtRandomState")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtRandomState)
        self.btnSetParamDecisionTree = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSetParamDecisionTree.sizePolicy().hasHeightForWidth())
        self.btnSetParamDecisionTree.setSizePolicy(sizePolicy)
        self.btnSetParamDecisionTree.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnSetParamDecisionTree.setFont(font)
        self.btnSetParamDecisionTree.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSetParamDecisionTree.setStyleSheet("QPushButton {\n"
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
        self.btnSetParamDecisionTree.setIcon(icon)
        self.btnSetParamDecisionTree.setIconSize(QtCore.QSize(18, 18))
        self.btnSetParamDecisionTree.setObjectName("btnSetParamDecisionTree")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.btnSetParamDecisionTree)
        self.txtMaxLeafNodes = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMaxLeafNodes.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 249, 249);\n"
"}")
        self.txtMaxLeafNodes.setObjectName("txtMaxLeafNodes")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txtMaxLeafNodes)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label)
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
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.btnCancel)
        self.horizontalLayout_15.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        FormSetParamDecisionTree.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormSetParamDecisionTree)
        self.statusbar.setObjectName("statusbar")
        FormSetParamDecisionTree.setStatusBar(self.statusbar)

        #button operations

        self.btnSetParamDecisionTree.clicked.connect(lambda:self.btnSetAndRunClicked(self.txtCriterion.text(),
                                                                                     self.txtMaxDepth.text(),
                                                                                     self.txtMinSamplesSplit.text(),
                                                                                     self.txtMinSamplesLeaf.text(),
                                                                                     self.txtMinWeightFractionLeaf.text(),
                                                                                     self.txtRandomState.text(),
                                                                                     self.txtMaxLeafNodes.text(),
                                                                                     FormSetParamDecisionTree))
        self.btnCancel.clicked.connect(FormSetParamDecisionTree.close)

        self.retranslateUi(FormSetParamDecisionTree)
        QtCore.QMetaObject.connectSlotsByName(FormSetParamDecisionTree)

    def retranslateUi(self, FormSetParamDecisionTree):
        _translate = QtCore.QCoreApplication.translate
        FormSetParamDecisionTree.setWindowTitle(_translate("FormSetParamDecisionTree", "Decision Tree"))
        self.label_10.setText(_translate("FormSetParamDecisionTree", "Set or Use Default Parameter"))
        self.label_5.setText(_translate("FormSetParamDecisionTree", "criterion :"))
        self.txtCriterion.setText(_translate("FormSetParamDecisionTree", "gini"))
        self.label_6.setText(_translate("FormSetParamDecisionTree", "max_depth :"))
        self.txtMaxDepth.setText(_translate("FormSetParamDecisionTree", "None"))
        self.label_7.setText(_translate("FormSetParamDecisionTree", "min_samples_split :"))
        self.txtMinSamplesSplit.setText(_translate("FormSetParamDecisionTree", "2"))
        self.label_8.setText(_translate("FormSetParamDecisionTree", "min_samples_leaf :"))
        self.txtMinSamplesLeaf.setText(_translate("FormSetParamDecisionTree", "1"))
        self.label_9.setText(_translate("FormSetParamDecisionTree", "min_weight_fraction_leaf :"))
        self.txtMinWeightFractionLeaf.setText(_translate("FormSetParamDecisionTree", "0.0"))
        self.label_3.setText(_translate("FormSetParamDecisionTree", "random_state :"))
        self.txtRandomState.setText(_translate("FormSetParamDecisionTree", "None"))
        self.btnSetParamDecisionTree.setText(_translate("FormSetParamDecisionTree", "Set && Run"))
        self.txtMaxLeafNodes.setText(_translate("FormSetParamDecisionTree", "None"))
        self.label.setText(_translate("FormSetParamDecisionTree", "max_leaf_nodes :"))
        self.btnCancel.setText(_translate("FormSetParamDecisionTree", "Cancel"))

    def btnSetAndRunClicked(self,criterion,max_depth,min_samples_split,
                            min_samples_leaf,min_weight_fraction_leaf,
                            random_state,max_leaf_nodes,FormSetParamDecisionTree):

            if max_leaf_nodes.upper() == "NONE":
                max_leaf_nodes = None
            if max_depth.upper() == "NONE":
                max_depth=None
            if random_state.upper() == "NONE":
                random_state=None

            self.algorithm = tree.DecisionTreeClassifier(criterion, max_depth=max_depth
                                                    , min_samples_split=int(min_samples_split)
                                                    , min_samples_leaf=int(min_samples_leaf)
                                                    , min_weight_fraction_leaf=float(min_weight_fraction_leaf)
                                                    , random_state=random_state, max_leaf_nodes=max_leaf_nodes)

            AlgorithmOperation.ApplyAlgorithm(self.algorithm)
            self.messageBox(FormSetParamDecisionTree)


    def messageBox(self,FormSetParamDecisionTree):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Algorithm Succesfully Set and Run")
        msg.setWindowTitle("Information")
        msg.setDetailedText(str(self.algorithm))
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()
        FormSetParamDecisionTree.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormSetParamDecisionTree = QtWidgets.QMainWindow()
    ui = Ui_FormSetParamDecisionTree()
    ui.setupUi(FormSetParamDecisionTree)
    FormSetParamDecisionTree.show()
    sys.exit(app.exec_())

