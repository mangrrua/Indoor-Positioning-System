# --- DEFINE SKLEARN ALGORITHMS --- #

import time

from Source.mongodb_operations import Queries
from Source.sklearn_algorithms import MachineLearningAlgorithms
from Source.visualization import Visualization
from sklearn import preprocessing

# --- IMPORT FILES --- #
from Source.get_data import PrepareTheData


class AlgorithmOperation:
    ptd = PrepareTheData()
    alg = None

    train_X=None
    train_y=None

    test_X=None
    test_y=None

    a=None
    b=None

    vs=None

    receivedResult=""
    mongoDB=Queries()

    @staticmethod
    def CreateVisualization():
        AlgorithmOperation.vs=Visualization(AlgorithmOperation.train_X,
                                            AlgorithmOperation.train_y,
                                            AlgorithmOperation.test_X,
                                            AlgorithmOperation.test_y)

    @staticmethod
    def GetFeatures():
        return AlgorithmOperation.ptd.list_training_sender_bssid

    @staticmethod
    def ApplyAlgorithm(algorithm):
        time_start = time.time()
        AlgorithmOperation.alg = MachineLearningAlgorithms(AlgorithmOperation.train_X, AlgorithmOperation.train_y
                                        ,AlgorithmOperation.test_X, AlgorithmOperation.test_y, algorithm)

        AlgorithmOperation.alg.learn_model()
        AlgorithmOperation.alg.prediction()

        time_end = time.time()
        AlgorithmOperation.receivedResult = AlgorithmOperation.alg.result_prediction +\
                                            AlgorithmOperation.alg.result_main

        print("Total elapsed time: " + str(round((time_end - time_start), 4)) + " sn")

    @staticmethod
    def PreprocessingData(processType):

        if processType=="Normalization":
            AlgorithmOperation.train_X = preprocessing.normalize(AlgorithmOperation.train_X, norm='l2')
            AlgorithmOperation.test_X = preprocessing.normalize(AlgorithmOperation.test_X, norm='l2')
        elif processType=="Scale":
            AlgorithmOperation.train_X =preprocessing.scale(AlgorithmOperation.train_X)
            AlgorithmOperation.test_X =preprocessing.scale(AlgorithmOperation.test_X)
        elif processType=="Binarization":
            AlgorithmOperation.train_X =preprocessing.binarize(AlgorithmOperation.train_X)
            AlgorithmOperation.test_X =preprocessing.binarize(AlgorithmOperation.test_X)
        elif processType=="Polynomial Feature":
            poly=preprocessing.PolynomialFeatures(2)
            AlgorithmOperation.train_X = poly.fit_transform(AlgorithmOperation.train_X)
            AlgorithmOperation.test_X = poly.fit_transform(AlgorithmOperation.test_X)

    @staticmethod
    def ImportTestFile(testFilePath):
        test_file_name = testFilePath
        AlgorithmOperation.ptd.import_file_to_mongodb("test", test_file_name)

    @staticmethod
    def ImportTrainFile(trainFilePath):
        training_file_name = trainFilePath
        AlgorithmOperation.ptd.import_file_to_mongodb("training", training_file_name)

    @staticmethod
    def PrepareTestnTrainData(chosenType):
        AlgorithmOperation.train_X, AlgorithmOperation.train_y = AlgorithmOperation.ptd.get_training_data(chosenType)
        AlgorithmOperation.test_X, AlgorithmOperation.test_y = AlgorithmOperation.ptd.get_runtime_data(chosenType)

    @staticmethod
    def GetListOfDataID():
        totalNumberOfDataId= AlgorithmOperation.ptd.get_count_and_sender_bssid()

