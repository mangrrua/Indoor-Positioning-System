from Forms.KNN import *
from Forms.NaiveBayes import *
from Forms.RandomForest import *
from Forms.SVC import *
from Forms.DecisionTree import *
from Source.use_algorithms import AlgorithmOperation
import Source.distance_algorithms as dist_alg
import json

#Checks status of imported files to enable grpPrepareData and grpPreprocessing
flagTrain=False
flagTest=False

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(700, 794)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TabWidget.sizePolicy().hasHeightForWidth())
        TabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        TabWidget.setFont(font)
        TabWidget.setAutoFillBackground(False)
        TabWidget.setStyleSheet("QWidget{\n"
"\n"
"background-color:#fcfdff;\n"
"\n"
"}")
        self.tabPreProcess = QtWidgets.QWidget()
        self.tabPreProcess.setAutoFillBackground(False)
        self.tabPreProcess.setObjectName("tabPreProcess")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tabPreProcess)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.btnImportTest = QtWidgets.QPushButton(self.tabPreProcess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnImportTest.sizePolicy().hasHeightForWidth())
        self.btnImportTest.setSizePolicy(sizePolicy)
        self.btnImportTest.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnImportTest.setFont(font)
        self.btnImportTest.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnImportTest.setAutoFillBackground(False)
        self.btnImportTest.setStyleSheet("QPushButton {\n"
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
        icon.addPixmap(QtGui.QPixmap(":/Icons/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnImportTest.setIcon(icon)
        self.btnImportTest.setIconSize(QtCore.QSize(24, 24))
        self.btnImportTest.setObjectName("btnImportTest")
        self.gridLayout_7.addWidget(self.btnImportTest, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem, 0, 0, 1, 1)
        self.btnImportTrain = QtWidgets.QPushButton(self.tabPreProcess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnImportTrain.sizePolicy().hasHeightForWidth())
        self.btnImportTrain.setSizePolicy(sizePolicy)
        self.btnImportTrain.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnImportTrain.setFont(font)
        self.btnImportTrain.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnImportTrain.setAutoFillBackground(False)
        self.btnImportTrain.setStyleSheet("QPushButton {\n"
"    background-color:#dbc7c7;\n"
"    color: #4c4c4c;\n"
"    border: 2px #efe3e3;\n"
"    border-style: outset;\n"
"    border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover {background-color:#f9e3e3;}\n"
"")
        self.btnImportTrain.setIcon(icon)
        self.btnImportTrain.setIconSize(QtCore.QSize(24, 24))
        self.btnImportTrain.setObjectName("btnImportTrain")
        self.gridLayout_7.addWidget(self.btnImportTrain, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 107, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem1, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem2, 2, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_7)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.grpBoxPreprocessing = QtWidgets.QGroupBox(self.tabPreProcess)
        self.grpBoxPreprocessing.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpBoxPreprocessing.sizePolicy().hasHeightForWidth())
        self.grpBoxPreprocessing.setSizePolicy(sizePolicy)
        self.grpBoxPreprocessing.setMaximumSize(QtCore.QSize(600, 600))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.grpBoxPreprocessing.setFont(font)
        self.grpBoxPreprocessing.setStyleSheet("QGroupBox::title { \n"
"    background-color: transparent;\n"
"     subcontrol-position: top left; /* position at the top left*/ \n"
"     padding:2 13px;\n"
" }\n"
"\n"
"QGroupBox{\n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
"    background-color:#f7f7f7;\n"
"\n"
"} ")
        self.grpBoxPreprocessing.setAlignment(QtCore.Qt.AlignCenter)
        self.grpBoxPreprocessing.setFlat(False)
        self.grpBoxPreprocessing.setObjectName("grpBoxPreprocessing")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.grpBoxPreprocessing)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.btnApplyPreprocessing = QtWidgets.QPushButton(self.grpBoxPreprocessing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnApplyPreprocessing.sizePolicy().hasHeightForWidth())
        self.btnApplyPreprocessing.setSizePolicy(sizePolicy)
        self.btnApplyPreprocessing.setMinimumSize(QtCore.QSize(0, 40))
        self.btnApplyPreprocessing.setMaximumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnApplyPreprocessing.setFont(font)
        self.btnApplyPreprocessing.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnApplyPreprocessing.setStyleSheet("QPushButton {\n"
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
        icon1.addPixmap(QtGui.QPixmap(":/Icons/apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnApplyPreprocessing.setIcon(icon1)
        self.btnApplyPreprocessing.setIconSize(QtCore.QSize(15, 15))
        self.btnApplyPreprocessing.setObjectName("btnApplyPreprocessing")
        self.gridLayout_10.addWidget(self.btnApplyPreprocessing, 0, 1, 1, 1)
        self.comboBoxPreProcessing = QtWidgets.QComboBox(self.grpBoxPreprocessing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxPreProcessing.sizePolicy().hasHeightForWidth())
        self.comboBoxPreProcessing.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxPreProcessing.setFont(font)
        self.comboBoxPreProcessing.setStyleSheet("QComboBox:item:selected\n"
"{\n"
"     background-color: grey;\n"
"}\n"
"")
        self.comboBoxPreProcessing.setObjectName("comboBoxPreProcessing")
        self.comboBoxPreProcessing.addItem("")
        self.comboBoxPreProcessing.addItem("")
        self.comboBoxPreProcessing.addItem("")
        self.comboBoxPreProcessing.addItem("")
        self.comboBoxPreProcessing.addItem("")
        self.comboBoxPreProcessing.setItemText(4, "")
        self.gridLayout_10.addWidget(self.comboBoxPreProcessing, 0, 0, 1, 1)
        self.horizontalLayout_16.addLayout(self.gridLayout_10)
        self.gridLayout_6.addWidget(self.grpBoxPreprocessing, 3, 0, 1, 1)
        self.grpBoxPrepareData = QtWidgets.QGroupBox(self.tabPreProcess)
        self.grpBoxPrepareData.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpBoxPrepareData.sizePolicy().hasHeightForWidth())
        self.grpBoxPrepareData.setSizePolicy(sizePolicy)
        self.grpBoxPrepareData.setMaximumSize(QtCore.QSize(600, 600))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.grpBoxPrepareData.setFont(font)
        self.grpBoxPrepareData.setStyleSheet("QGroupBox::title { \n"
"    background-color: transparent;\n"
"     subcontrol-position: top left; /* position at the top left*/ \n"
"     padding:2 13px;\n"
" }\n"
"\n"
"QGroupBox{\n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
"    background-color:#f7f7f7;\n"
"\n"
"} ")
        self.grpBoxPrepareData.setAlignment(QtCore.Qt.AlignCenter)
        self.grpBoxPrepareData.setFlat(False)
        self.grpBoxPrepareData.setObjectName("grpBoxPrepareData")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.grpBoxPrepareData)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.btnApplyPrepareData = QtWidgets.QPushButton(self.grpBoxPrepareData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnApplyPrepareData.sizePolicy().hasHeightForWidth())
        self.btnApplyPrepareData.setSizePolicy(sizePolicy)
        self.btnApplyPrepareData.setMinimumSize(QtCore.QSize(0, 40))
        self.btnApplyPrepareData.setMaximumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnApplyPrepareData.setFont(font)
        self.btnApplyPrepareData.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnApplyPrepareData.setStyleSheet("QPushButton {\n"
"    background-color:#dbc7c7;\n"
"    color: #4c4c4c;\n"
"    border: 2px #efe3e3;\n"
"    border-style: outset;\n"
"    border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover {background-color:#f9e3e3;}\n"
"")
        self.btnApplyPrepareData.setIcon(icon1)
        self.btnApplyPrepareData.setIconSize(QtCore.QSize(15, 15))
        self.btnApplyPrepareData.setObjectName("btnApplyPrepareData")
        self.gridLayout_9.addWidget(self.btnApplyPrepareData, 0, 1, 1, 1)
        self.comboBoxPrepareData = QtWidgets.QComboBox(self.grpBoxPrepareData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxPrepareData.sizePolicy().hasHeightForWidth())
        self.comboBoxPrepareData.setSizePolicy(sizePolicy)
        self.comboBoxPrepareData.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxPrepareData.setFont(font)
        self.comboBoxPrepareData.setStyleSheet("QComboBox:item:selected\n"
"{\n"
"     background-color: grey;\n"
"}\n"
"")
        self.comboBoxPrepareData.setObjectName("comboBoxPrepareData")
        self.comboBoxPrepareData.addItem("")
        self.comboBoxPrepareData.addItem("")
        self.comboBoxPrepareData.addItem("")
        self.gridLayout_9.addWidget(self.comboBoxPrepareData, 0, 0, 1, 1)
        self.horizontalLayout_15.addLayout(self.gridLayout_9)
        self.gridLayout_6.addWidget(self.grpBoxPrepareData, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 65, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem3, 2, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.textBrowserTrainSample = QtWidgets.QTextBrowser(self.tabPreProcess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowserTrainSample.sizePolicy().hasHeightForWidth())
        self.textBrowserTrainSample.setSizePolicy(sizePolicy)
        self.textBrowserTrainSample.setMinimumSize(QtCore.QSize(300, 0))
        self.textBrowserTrainSample.setStyleSheet("QTextBrowser{\n"
"background-color: #fffcfc;\n"
"border:2px #c6c6c6;\n"
"border-style:solid;\n"
"border-radius:5px;\n"
"}")
        self.textBrowserTrainSample.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textBrowserTrainSample.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowserTrainSample.setObjectName("textBrowserTrainSample")
        self.gridLayout_8.addWidget(self.textBrowserTrainSample, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tabPreProcess)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"\n"
"background-color:#f7f7f7;\n"
"}")
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(1)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_8.addItem(spacerItem4, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_8)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        TabWidget.addTab(self.tabPreProcess, "")
        self.tabClassifier = QtWidgets.QWidget()
        self.tabClassifier.setAutoFillBackground(False)
        self.tabClassifier.setObjectName("tabClassifier")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tabClassifier)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(self.tabClassifier)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"\n"
"background-color:#f7f7f7;\n"
"}")
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBoxAlgorithms = QtWidgets.QComboBox(self.tabClassifier)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBoxAlgorithms.setFont(font)
        self.comboBoxAlgorithms.setStyleSheet("QComboBox:item:selected\n"
"{\n"
"     background-color: grey;\n"
"}\n"
"")
        self.comboBoxAlgorithms.setObjectName("comboBoxAlgorithms")
        self.comboBoxAlgorithms.addItem("")
        self.comboBoxAlgorithms.addItem("")
        self.comboBoxAlgorithms.addItem("")
        self.comboBoxAlgorithms.addItem("")
        self.comboBoxAlgorithms.addItem("")
        self.comboBoxAlgorithms.addItem("")
        self.verticalLayout_3.addWidget(self.comboBoxAlgorithms)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.btnApplyAlgorithm = QtWidgets.QPushButton(self.tabClassifier)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnApplyAlgorithm.sizePolicy().hasHeightForWidth())
        self.btnApplyAlgorithm.setSizePolicy(sizePolicy)
        self.btnApplyAlgorithm.setMinimumSize(QtCore.QSize(0, 40))
        self.btnApplyAlgorithm.setMaximumSize(QtCore.QSize(350, 200))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnApplyAlgorithm.setFont(font)
        self.btnApplyAlgorithm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnApplyAlgorithm.setStyleSheet("QPushButton {\n"
"    background-color:#dbc7c7;\n"
"    color: #4c4c4c;\n"
"    border: 2px #efe3e3;\n"
"    border-style: outset;\n"
"    border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover {background-color:#f9e3e3;}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/runalgorithm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnApplyAlgorithm.setIcon(icon2)
        self.btnApplyAlgorithm.setIconSize(QtCore.QSize(24, 24))
        self.btnApplyAlgorithm.setObjectName("btnApplyAlgorithm")
        self.horizontalLayout_7.addWidget(self.btnApplyAlgorithm)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem10)
        self.label_3 = QtWidgets.QLabel(self.tabClassifier)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"\n"
"background-color:#f7f7f7;\n"
"}")
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.textBrowserResult = QtWidgets.QTextBrowser(self.tabClassifier)
        self.textBrowserResult.setStyleSheet("QTextBrowser{\n"
"background-color: #fffcfc;\n"
"border:2px #c6c6c6;\n"
"border-style:solid;\n"
"border-radius:5px;\n"
"}")
        self.textBrowserResult.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textBrowserResult.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowserResult.setReadOnly(True)
        self.textBrowserResult.setObjectName("textBrowserResult")
        self.verticalLayout_2.addWidget(self.textBrowserResult)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        TabWidget.addTab(self.tabClassifier, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"\n"
"background-color:#f7f7f7;\n"
"}")
        self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.textBrowserStatistics = QtWidgets.QTextBrowser(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowserStatistics.sizePolicy().hasHeightForWidth())
        self.textBrowserStatistics.setSizePolicy(sizePolicy)
        self.textBrowserStatistics.setMaximumSize(QtCore.QSize(600, 600))
        self.textBrowserStatistics.setStyleSheet("QTextBrowser{\n"
"background-color: #fffcfc;\n"
"border:2px #c6c6c6;\n"
"border-style:solid;\n"
"border-radius:5px;\n"
"}")
        self.textBrowserStatistics.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textBrowserStatistics.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowserStatistics.setReadOnly(True)
        self.textBrowserStatistics.setObjectName("textBrowserStatistics")
        self.gridLayout_4.addWidget(self.textBrowserStatistics, 1, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_4)
        self.gridLayout_5.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"\n"
"background-color:#f7f7f7;\n"
"}")
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.grpBoxChartType = QtWidgets.QGroupBox(self.tab)
        self.grpBoxChartType.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpBoxChartType.sizePolicy().hasHeightForWidth())
        self.grpBoxChartType.setSizePolicy(sizePolicy)
        self.grpBoxChartType.setMaximumSize(QtCore.QSize(415, 400))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.grpBoxChartType.setFont(font)
        self.grpBoxChartType.setStyleSheet("QGroupBox::title { \n"
"    background-color: transparent;\n"
"     subcontrol-position: top left; /* position at the top left*/ \n"
"     padding:2 13px;\n"
" }\n"
"\n"
"QGroupBox{\n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
"    background-color:#f7f7f7;\n"
"\n"
"} ")
        self.grpBoxChartType.setAlignment(QtCore.Qt.AlignCenter)
        self.grpBoxChartType.setFlat(False)
        self.grpBoxChartType.setObjectName("grpBoxChartType")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.grpBoxChartType)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem11 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem11)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem12 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.comboBoxChartType = QtWidgets.QComboBox(self.grpBoxChartType)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxChartType.sizePolicy().hasHeightForWidth())
        self.comboBoxChartType.setSizePolicy(sizePolicy)
        self.comboBoxChartType.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxChartType.setFont(font)
        self.comboBoxChartType.setStyleSheet("QComboBox:item:selected\n"
"{\n"
"     background-color: grey;\n"
"}\n"
"")
        self.comboBoxChartType.setObjectName("comboBoxChartType")
        self.comboBoxChartType.addItem("")
        self.comboBoxChartType.addItem("")
        self.comboBoxChartType.addItem("")
        self.comboBoxChartType.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBoxChartType, 0, QtCore.Qt.AlignLeft)
        self.label_7 = QtWidgets.QLabel(self.grpBoxChartType)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(32, 32))
        self.label_7.setMaximumSize(QtCore.QSize(32, 32))
        self.label_7.setStyleSheet("QLabel{\n"
"background-color: transparent\n"
"\n"
"}")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/Icons/statistics.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.gridLayout_3.addWidget(self.grpBoxChartType, 1, 0, 1, 1)
        self.verticalLayout_12.addLayout(self.gridLayout_3)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem13)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.grpBoxSenderBSSID = QtWidgets.QGroupBox(self.tab)
        self.grpBoxSenderBSSID.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpBoxSenderBSSID.sizePolicy().hasHeightForWidth())
        self.grpBoxSenderBSSID.setSizePolicy(sizePolicy)
        self.grpBoxSenderBSSID.setMinimumSize(QtCore.QSize(0, 130))
        self.grpBoxSenderBSSID.setMaximumSize(QtCore.QSize(200, 600))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.grpBoxSenderBSSID.setFont(font)
        self.grpBoxSenderBSSID.setStyleSheet("QGroupBox::title { \n"
"    background-color: transparent;\n"
"     subcontrol-position: top left; /* position at the top left*/ \n"
"     padding:2 13px;\n"
" }\n"
"\n"
"QGroupBox{\n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
"    background-color:#f7f7f7;\n"
"\n"
"} ")
        self.grpBoxSenderBSSID.setAlignment(QtCore.Qt.AlignCenter)
        self.grpBoxSenderBSSID.setFlat(False)
        self.grpBoxSenderBSSID.setObjectName("grpBoxSenderBSSID")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.grpBoxSenderBSSID)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem14 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_10.addItem(spacerItem14)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.listWidgetBSSID = QtWidgets.QListWidget(self.grpBoxSenderBSSID)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetBSSID.sizePolicy().hasHeightForWidth())
        self.listWidgetBSSID.setSizePolicy(sizePolicy)
        self.listWidgetBSSID.setMinimumSize(QtCore.QSize(0, 100))
        self.listWidgetBSSID.setMaximumSize(QtCore.QSize(150, 50))
        self.listWidgetBSSID.setSizeIncrement(QtCore.QSize(0, 0))
        self.listWidgetBSSID.setBaseSize(QtCore.QSize(0, 0))
        self.listWidgetBSSID.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidgetBSSID.setStyleSheet("QListWidget{\n"
"background-color: #fffcfc;\n"
"border:2px #c6c6c6;\n"
"border-style:solid;\n"
"border-radius:5px;\n"
"}")
        self.listWidgetBSSID.setObjectName("listWidgetBSSID")
        self.horizontalLayout_9.addWidget(self.listWidgetBSSID, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10 = QtWidgets.QLabel(self.grpBoxSenderBSSID)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(32, 32))
        self.label_10.setMaximumSize(QtCore.QSize(32, 32))
        self.label_10.setStyleSheet("QLabel{\n"
"background-color: transparent\n"
"\n"
"}")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../Icons/wireless-router.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.gridLayout.addWidget(self.grpBoxSenderBSSID, 0, 1, 1, 1)
        self.grpBoxDataID = QtWidgets.QGroupBox(self.tab)
        self.grpBoxDataID.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpBoxDataID.sizePolicy().hasHeightForWidth())
        self.grpBoxDataID.setSizePolicy(sizePolicy)
        self.grpBoxDataID.setMinimumSize(QtCore.QSize(0, 130))
        self.grpBoxDataID.setMaximumSize(QtCore.QSize(200, 600))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.grpBoxDataID.setFont(font)
        self.grpBoxDataID.setStyleSheet("QGroupBox::title { \n"
"    background-color: transparent;\n"
"     subcontrol-position: top left; /* position at the top left*/ \n"
"     padding:2 13px;\n"
" }\n"
"\n"
"QGroupBox{\n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
"    background-color:#f7f7f7;\n"
"\n"
"} ")
        self.grpBoxDataID.setAlignment(QtCore.Qt.AlignCenter)
        self.grpBoxDataID.setFlat(False)
        self.grpBoxDataID.setObjectName("grpBoxDataID")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.grpBoxDataID)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem15 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem15)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.listWidgetDataID = QtWidgets.QListWidget(self.grpBoxDataID)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetDataID.sizePolicy().hasHeightForWidth())
        self.listWidgetDataID.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidgetDataID.setSizePolicy(sizePolicy)
        self.listWidgetDataID.setMinimumSize(QtCore.QSize(0, 100))
        self.listWidgetDataID.setMaximumSize(QtCore.QSize(150, 50))
        self.listWidgetDataID.setStyleSheet("QListWidget{\n"
"background-color: #fffcfc;\n"
"border:2px #c6c6c6;\n"
"border-style:solid;\n"
"border-radius:5px;\n"
"}")
        self.listWidgetDataID.setObjectName("listWidgetDataID")
        self.horizontalLayout_10.addWidget(self.listWidgetDataID, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_11 = QtWidgets.QLabel(self.grpBoxDataID)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(32, 32))
        self.label_11.setMaximumSize(QtCore.QSize(32, 32))
        self.label_11.setStyleSheet("QLabel{\n"
"background-color: transparent\n"
"\n"
"}")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/Icons/id.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.verticalLayout_11.addLayout(self.horizontalLayout_10)
        self.gridLayout.addWidget(self.grpBoxDataID, 0, 0, 1, 1)
        self.verticalLayout_12.addLayout(self.gridLayout)
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem16)
        self.grpBoxPickFeature = QtWidgets.QGroupBox(self.tab)
        self.grpBoxPickFeature.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpBoxPickFeature.sizePolicy().hasHeightForWidth())
        self.grpBoxPickFeature.setSizePolicy(sizePolicy)
        self.grpBoxPickFeature.setMinimumSize(QtCore.QSize(0, 130))
        self.grpBoxPickFeature.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.grpBoxPickFeature.setFont(font)
        self.grpBoxPickFeature.setStyleSheet("QGroupBox::title { \n"
"    background-color: transparent;\n"
"     subcontrol-position: top left; /* position at the top left*/ \n"
"     padding:2 13px;\n"
" }\n"
"\n"
"QGroupBox{\n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
"    background-color:#f7f7f7;\n"
"\n"
"} ")
        self.grpBoxPickFeature.setAlignment(QtCore.Qt.AlignCenter)
        self.grpBoxPickFeature.setFlat(False)
        self.grpBoxPickFeature.setObjectName("grpBoxPickFeature")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.grpBoxPickFeature)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        spacerItem17 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_16.addItem(spacerItem17)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.grpBoxPickFeature)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{\n"
"\n"
"background-color:#f7f7f7;\n"
"}")
        self.label_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.grpBoxPickFeature)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{\n"
"\n"
"background-color:#f7f7f7;\n"
"}")
        self.label_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.listWidgetFeature1 = QtWidgets.QListWidget(self.grpBoxPickFeature)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetFeature1.sizePolicy().hasHeightForWidth())
        self.listWidgetFeature1.setSizePolicy(sizePolicy)
        self.listWidgetFeature1.setMinimumSize(QtCore.QSize(0, 100))
        self.listWidgetFeature1.setMaximumSize(QtCore.QSize(16777215, 80))
        self.listWidgetFeature1.setSizeIncrement(QtCore.QSize(150, 50))
        self.listWidgetFeature1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidgetFeature1.setStyleSheet("QListWidget{\n"
"background-color: #fffcfc;\n"
"border:2px #c6c6c6;\n"
"border-style:solid;\n"
"border-radius:5px;\n"
"}")
        self.listWidgetFeature1.setObjectName("listWidgetFeature1")
        self.gridLayout_2.addWidget(self.listWidgetFeature1, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.listWidgetFeature2 = QtWidgets.QListWidget(self.grpBoxPickFeature)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetFeature2.sizePolicy().hasHeightForWidth())
        self.listWidgetFeature2.setSizePolicy(sizePolicy)
        self.listWidgetFeature2.setMinimumSize(QtCore.QSize(0, 100))
        self.listWidgetFeature2.setMaximumSize(QtCore.QSize(150, 50))
        self.listWidgetFeature2.setSizeIncrement(QtCore.QSize(0, 0))
        self.listWidgetFeature2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidgetFeature2.setStyleSheet("QListWidget{\n"
"background-color: #fffcfc;\n"
"border:2px #c6c6c6;\n"
"border-style:solid;\n"
"border-radius:5px;\n"
"}")
        self.listWidgetFeature2.setObjectName("listWidgetFeature2")
        self.gridLayout_2.addWidget(self.listWidgetFeature2, 1, 1, 1, 1, QtCore.Qt.AlignTop)
        self.verticalLayout_16.addLayout(self.gridLayout_2)
        self.verticalLayout_12.addWidget(self.grpBoxPickFeature, 0, QtCore.Qt.AlignHCenter)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem18)
        self.btnDrawChart = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDrawChart.sizePolicy().hasHeightForWidth())
        self.btnDrawChart.setSizePolicy(sizePolicy)
        self.btnDrawChart.setMinimumSize(QtCore.QSize(120, 50))
        self.btnDrawChart.setMaximumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnDrawChart.setFont(font)
        self.btnDrawChart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDrawChart.setStyleSheet("QPushButton {\n"
"    background-color:#dbc7c7;\n"
"    color: #4c4c4c;\n"
"    border: 2px #efe3e3;\n"
"    border-style: outset;\n"
"    border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover {background-color:#f9e3e3;}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/chart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDrawChart.setIcon(icon3)
        self.btnDrawChart.setIconSize(QtCore.QSize(20, 20))
        self.btnDrawChart.setObjectName("btnDrawChart")
        self.verticalLayout_12.addWidget(self.btnDrawChart, 0, QtCore.Qt.AlignHCenter)
        spacerItem19 = QtWidgets.QSpacerItem(20, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem19)
        self.gridLayout_5.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_5)
        TabWidget.addTab(self.tab, "")

        # button operation
        self.btnApplyAlgorithm.clicked.connect(self.ChosenAlgorithmFromCombobox)
        self.btnImportTrain.clicked.connect(self.btnImportTrainFileClicked)
        self.btnImportTest.clicked.connect(self.btnImportTestFileClicked)
        self.btnApplyPreprocessing.clicked.connect(self.btnApplyPreprocessingClicked)
        self.btnApplyPrepareData.clicked.connect(self.btnApplyPrepareDataClicked)
        self.btnDrawChart.clicked.connect(self.btnDrawChartClicked)
        self.listWidgetDataID.itemClicked.connect(self.SelectedIndexChangeListItem)

        # timer
        self.timerOfGrpEnable = QtCore.QTimer()
        self.timerOfGrpEnable.timeout.connect(self.TimerForGroupBox)

        # Widget Dictionary
        self.widgets = {'Scatter Chart (Two Features)': self.grpBoxPickFeature,
                        'Histogram (#of Location)': self.grpBoxSenderBSSID,
                        'Bar (#of RSSI Values)': self.grpBoxSenderBSSID,
                        'Line (Average RSSI Values)': self.grpBoxDataID}
        # Combobox Index Change
        self.comboBoxChartType.currentIndexChanged['QString'].connect(self.ChangeStatusOfGroupBox)

        # Current Tab Change
        TabWidget.currentChanged.connect(self.SelectedIndexChangeCombobox)

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "Indoor Positioning System"))
        self.btnImportTest.setText(_translate("TabWidget", "Upload\n"
"Test File"))
        self.btnImportTrain.setText(_translate("TabWidget", "Upload\n"
"Train File"))
        self.grpBoxPreprocessing.setTitle(_translate("TabWidget", "Preprocessing"))
        self.btnApplyPreprocessing.setText(_translate("TabWidget", "Apply"))
        self.comboBoxPreProcessing.setItemText(0, _translate("TabWidget", "Scale"))
        self.comboBoxPreProcessing.setItemText(1, _translate("TabWidget", "Normalization"))
        self.comboBoxPreProcessing.setItemText(2, _translate("TabWidget", "Binarization"))
        self.comboBoxPreProcessing.setItemText(3, _translate("TabWidget", "Polynomial Feature"))
        self.grpBoxPrepareData.setTitle(_translate("TabWidget", "Prepare Data"))
        self.btnApplyPrepareData.setText(_translate("TabWidget", "Apply"))
        self.comboBoxPrepareData.setItemText(0, _translate("TabWidget", "Average"))
        self.comboBoxPrepareData.setItemText(1, _translate("TabWidget", "Minimum"))
        self.comboBoxPrepareData.setItemText(2, _translate("TabWidget", "Maximum"))
        self.label.setText(_translate("TabWidget", "Features"))
        TabWidget.setTabText(TabWidget.indexOf(self.tabPreProcess), _translate("TabWidget", "Preprocessing"))
        self.label_2.setText(_translate("TabWidget", "Choose Algorithm"))
        self.comboBoxAlgorithms.setItemText(0, _translate("TabWidget", "KNN"))
        self.comboBoxAlgorithms.setItemText(1, _translate("TabWidget", "Naive Bayes"))
        self.comboBoxAlgorithms.setItemText(2, _translate("TabWidget", "Random Forest"))
        self.comboBoxAlgorithms.setItemText(3, _translate("TabWidget", "Decision Tree"))
        self.comboBoxAlgorithms.setItemText(4, _translate("TabWidget", "SVC"))
        self.comboBoxAlgorithms.setItemText(5, _translate("TabWidget", "Omega"))
        self.btnApplyAlgorithm.setText(_translate("TabWidget", "Apply Algorithm"))
        self.label_3.setText(_translate("TabWidget", "Result"))
        TabWidget.setTabText(TabWidget.indexOf(self.tabClassifier), _translate("TabWidget", "Classifier"))
        self.label_5.setText(_translate("TabWidget", "Statistics"))
        self.label_6.setText(_translate("TabWidget", "Operations"))
        self.grpBoxChartType.setTitle(_translate("TabWidget", "Select Chart Type"))
        self.comboBoxChartType.setItemText(0, _translate("TabWidget", "Scatter Chart (Two Features)"))
        self.comboBoxChartType.setItemText(1, _translate("TabWidget", "Histogram (#of Location)"))
        self.comboBoxChartType.setItemText(2, _translate("TabWidget", "Bar (#of RSSI Values)"))
        self.comboBoxChartType.setItemText(3, _translate("TabWidget", "Line (Average RSSI Values)"))
        self.grpBoxSenderBSSID.setTitle(_translate("TabWidget", "Select Sender_BSSID"))
        self.grpBoxDataID.setTitle(_translate("TabWidget", "Select Data_ID"))
        self.grpBoxPickFeature.setTitle(_translate("TabWidget", "Pick Two Features"))
        self.label_9.setText(_translate("TabWidget", "Feature_2 :"))
        self.label_8.setText(_translate("TabWidget", "Feature_1:"))
        self.btnDrawChart.setText(_translate("TabWidget", "Draw Chart"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Visiualization"))

    #---------UI Operation Function------------#
    def ChosenAlgorithmFromCombobox(self):

        if str(self.comboBoxAlgorithms.currentText()) == "KNN":
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_FormSetKNNParam()
            self.ui.setupUi(self.window)
            self.window.show()
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.PrintResult)
            self.timer.start(100)


        elif str(self.comboBoxAlgorithms.currentText()) == "Naive Bayes":
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_FormSetNaiveBayesParam()
            self.ui.setupUi(self.window)
            self.window.show()
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.PrintResult)
            self.timer.start(100)

        elif str(self.comboBoxAlgorithms.currentText()) == "Random Forest":
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_FormSetRandomForestParam()
            self.ui.setupUi(self.window)
            self.window.show()
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.PrintResult)
            self.timer.start(100)

        elif str(self.comboBoxAlgorithms.currentText()) == "Decision Tree":
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_FormSetParamDecisionTree()
            self.ui.setupUi(self.window)
            self.window.show()
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.PrintResult)
            self.timer.start(100)

        elif str(self.comboBoxAlgorithms.currentText()) == "SVC":
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_FormSetParamSVC()
            self.ui.setupUi(self.window)
            self.window.show()
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.PrintResult)
            self.timer.start(100)

        elif str(self.comboBoxAlgorithms.currentText()) == "Omega":
            dist_alg.nearest_tree_point_prediction(AlgorithmOperation.train_X,AlgorithmOperation.train_y,
                                                   AlgorithmOperation.test_X,AlgorithmOperation.test_y)
            self.textBrowserResult.setText( dist_alg.resultString)

    #--------Button Click Events---------------#
    def btnImportTrainFileClicked(self):

        self.fnameTrain = QtWidgets.QFileDialog.getOpenFileName(TabWidget, 'Open file',
                                                                filter="JSON files (*.json)")
        if self.fnameTrain!=('',''):
            AlgorithmOperation.ImportTrainFile(self.fnameTrain[0])
            self.MessageBox("Train File was uploaded successfully")
            global flagTrain
            flagTrain = True

            if not self.timerOfGrpEnable.isActive():
                self.timerOfGrpEnable.start(100)

    def btnImportTestFileClicked(self):
        self.fnameTest = QtWidgets.QFileDialog.getOpenFileName(TabWidget, 'Open file',
                                                               filter="JSON files (*.json)")
        if self.fnameTest != ('', ''):
            AlgorithmOperation.ImportTestFile(self.fnameTest[0])
            self.MessageBox("Test File was uploaded successfully")
            global flagTest
            flagTest = True
            if not self.timerOfGrpEnable.isActive():
                self.timerOfGrpEnable.start(100)

    def btnApplyPrepareDataClicked(self):
        AlgorithmOperation.PrepareTestnTrainData(self.comboBoxPrepareData.currentText())

        list_features = AlgorithmOperation.GetFeatures()
        self.MessageBox("Features were created")

        self.textBrowserTrainSample.clear()
        index = 0
        # Font
        f = QtGui.QFont()
        f.setBold(True)
        f.setWeight(60)
        f.setPointSize(10)
        self.textBrowserTrainSample.setFont(f)
        self.textBrowserTrainSample.append('{:20}'.format('Index') + "Feature")
        self.textBrowserTrainSample.append('{:-<40}'.format(''))
        for fdata in list_features:
            self.textBrowserTrainSample.append('{:20}'.format(str(index) + ":") + fdata)
            self.textBrowserTrainSample.append("")
            index += 1

    def btnApplyPreprocessingClicked(self):
        AlgorithmOperation.PreprocessingData(self.comboBoxPreProcessing.currentText())
        self.MessageBox("Preprocessing was succeed")

    def btnDrawChartClicked(self):
            currentText = self.comboBoxChartType.currentText()
            AlgorithmOperation.CreateVisualization()

            if currentText == "Bar (#of RSSI Values)":
                '''AlgorithmOperation.vs.bar_chart_rssi_values(self.listWidgetDataID.currentItem().text(),
                                                             self.listWidgetBSSID.currentItem().text())'''
                self.statistics = AlgorithmOperation.vs.bar_chart_rssi_values_statistics(
                    self.listWidgetDataID.currentItem().text(),
                    self.listWidgetBSSID.currentItem().text())

                self.statistics = json.dumps(self.statistics, indent=4)
                self.textBrowserStatistics.setText(self.statistics)
            elif currentText == "Line (Average RSSI Values)":
                AlgorithmOperation.vs.line_average_rssi_values(self.listWidgetDataID.currentItem().text())

            elif currentText == "Histogram (#of Location)":
                AlgorithmOperation.vs.hist_visualize(self.listWidgetBSSID.currentRow())

            elif currentText == "Scatter Chart (Two Features)":
                feature_1 = self.listWidgetFeature1.currentRow()
                feature_2 = self.listWidgetFeature2.currentRow()

                AlgorithmOperation.vs.scatter_visualize(feature_1, feature_2)

    def MessageBox(self, stringToPrint):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(stringToPrint)
        msg.setWindowTitle("Information")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()

    def TimerForGroupBox(self):
        if flagTrain == True and flagTest == True:
            self.grpBoxPreprocessing.setEnabled(True)
            self.grpBoxPrepareData.setEnabled(True)
            self.timerOfGrpEnable.stop()

            # Visiualization Tab Operations

    def PrintResult(self):
        self.textBrowserResult.setText(AlgorithmOperation.receivedResult)
        if (AlgorithmOperation.receivedResult != ""):
            self.timer.stop()
            AlgorithmOperation.receivedResult = ""

    def ChangeStatusOfGroupBox(self, currentIndex):
        # set enabled false of each groupbox
        self.grpBoxDataID.setEnabled(False)
        self.grpBoxSenderBSSID.setEnabled(False)
        self.grpBoxPickFeature.setEnabled(False)
        # clear comboboxes
        self.listWidgetBSSID.clear()
        self.listWidgetDataID.clear()
        self.listWidgetFeature1.clear()
        self.listWidgetFeature2.clear()

        data_id = []

        widget = self.widgets[currentIndex]
        widget.setEnabled(True)
        if currentIndex == "Bar (#of RSSI Values)":
            self.grpBoxDataID.setEnabled(True)
            for i in range(1, AlgorithmOperation.ptd.get_count_and_sender_bssid()[0] + 1):
                data_id.append(str(i))
            self.listWidgetDataID.addItems(data_id)

            self.listWidgetDataID.setCurrentRow(0)
            self.listWidgetBSSID.addItems(AlgorithmOperation.ptd.get_sender_bssid_for_data_id(
                self.listWidgetDataID.currentItem().text()))
            self.listWidgetBSSID.setCurrentRow(0)

        if currentIndex == "Histogram (#of Location)":
            self.listWidgetBSSID.addItems(AlgorithmOperation.ptd.get_count_and_sender_bssid()[1])
            self.listWidgetBSSID.setCurrentRow(0)

        elif currentIndex == "Scatter Chart (Two Features)":
            self.listWidgetFeature1.addItems(AlgorithmOperation.ptd.get_count_and_sender_bssid()[1])
            self.listWidgetFeature2.addItems(AlgorithmOperation.ptd.get_count_and_sender_bssid()[1])
            self.listWidgetFeature1.setCurrentRow(0)
            self.listWidgetFeature2.setCurrentRow(0)

        elif currentIndex == "Line (Average RSSI Values)":
            for i in range(1, AlgorithmOperation.ptd.get_count_and_sender_bssid()[0] + 1):
                data_id.append(str(i))
            self.listWidgetDataID.addItems(data_id)
            self.listWidgetDataID.setCurrentRow(0)

    def SelectedIndexChangeListItem(self):
        self.listWidgetBSSID.clear()
        self.listWidgetBSSID.addItems(AlgorithmOperation.ptd.get_sender_bssid_for_data_id(
            self.listWidgetDataID.currentItem().text()))

    def SelectedIndexChangeCombobox(self):
        self.comboBoxChartType.setCurrentIndex(1)
        self.comboBoxChartType.setCurrentIndex(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    TabWidget.setFixedSize(699, 642)
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())

