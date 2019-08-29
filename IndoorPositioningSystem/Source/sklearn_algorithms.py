from scipy.spatial import distance
import numpy as np
import time


class MachineLearningAlgorithms:

    def __init__(self, train_X, train_y, test_X, test_y, algorithm):

        # define algorithm
        self.algorithm = algorithm

        # training data and (x, y, z) labels,
        self.train_X = train_X
        self.train_y = train_y

        # test(runtime) data and (x, y, z) labels,
        self.test_X = test_X
        self.test_y = test_y

        # for learn and prediction time
        self.learn_time = 0
        self.prediction_time = 0

        self.result_prediction=""
        self.result_main=""

    def learn_model(self):

        start_time_learn = time.time()

        # learn model
        self.algorithm.fit(self.train_X, self.train_y)

        end_time_learn = time.time()
        self.learn_time = (end_time_learn - start_time_learn)
        print("Model learned")

    def prediction(self):

        start_time_prediction = time.time()
        # predict localization for test(runtime) data
        predictions = self.algorithm.predict(self.test_X)

        end_time_prediction = time.time()
        self.prediction_time = (end_time_prediction - start_time_prediction)

        # initialize localization result array
        localization_result = np.zeros(len(self.test_y))

        # dictionary for keeping estimated and actual location (x, y, z)
        est_loc = {}
        act_loc = {}

        index = 0
        for i in range(len(self.test_y)):

            # assignment estimated location
            est_loc["est_x"] = float(predictions[i].split(",")[0])
            est_loc["est_y"] = float(predictions[i].split(",")[1])
            est_loc["est_z"] = float(predictions[i].split(",")[2])

            # assignment actual location
            act_loc["act_x"] = float(self.test_y[i].split(",")[0])
            act_loc["act_y"] = float(self.test_y[i].split(",")[1])
            act_loc["act_z"] = float(self.test_y[i].split(",")[2])

            # find the localization error between the estimated and actual location
            localization_result[i] = self.get_localization_error(est_loc, act_loc)

            # print estimated, actual location and localization error each data
            print("Data " + str(i + 1))
            print("Estimated location (x, y, z): " + "(" +
                  str(round(est_loc["est_x"], 2)) + ", " +
                  str(round(est_loc["est_y"], 2)) + ", " +
                  str(round(est_loc["est_z"], 2)) + ")"
                  )
            print("Actual location (x, y, z): " + "(" +
                  str(round(act_loc["act_x"], 2)) + ", " +
                  str(round(act_loc["act_y"], 2)) + ", " +
                  str(round(act_loc["act_z"], 2)) + ")"
                  )
            print("Localization error: " + str(round(localization_result[i], 3)))
            print("")

            self.result_prediction += "Data " + str(i + 1) + "\n" + "Estimated location (x, y, z): " + "(" + \
                                  str(round(est_loc["est_x"], 2)) + ", " + \
                                  str(round(est_loc["est_y"], 2)) + ", " + \
                                  str(round(est_loc["est_z"], 2)) + ")" + "\n" + "Actual location (x, y, z): " + "(" + \
                                  str(round(act_loc["act_x"], 2)) + ", " + \
                                  str(round(act_loc["act_y"], 2)) + ", " + \
                                  str(round(act_loc["act_z"], 2)) + ")" + "\nLocalization error: " + str(
                round(localization_result[i], 3)) + "\n\n"
            index += 1

        # print localization and algorithm results
        self.print_results(localization_result)

    # find min, max, average and median error and print this values
    def print_results(self, localization_result):

        print("--------- Results --------- ")
        print("Minimum localization error: ", round(np.amin(localization_result), 3))
        print("Maximum localization error: ", round(np.amax(localization_result), 3))
        print("Average localization error: ", round(np.average(localization_result), 3))
        print("Median  localization error: ", round(np.median(localization_result), 3))
        print("")

        acc = self.accuracy_locations(localization_result)

        print("Accuracy for zero to one: " + "%" + str(acc["zto"]))
        print("Accuracy for one to two: " + "%" + str(acc["ott"]))
        print("Accuracy for two to opss: " + "%" + str(acc["tto"]))

        # algorithm properties and learning-prediction time
        print("")
        print("-> Classifier= " + str(self.algorithm))
        print("")
        print("-> Algorithm learning time: " + str(round(self.learn_time, 4)))
        print("-> Algorithm prediction time: " + str(round(self.prediction_time, 4)))
        print("")

        self.result_main = "\n--------- Results --------- "
        self.result_main += "\n" + "Minimum localization error: " + str(round(np.amin(localization_result), 3))
        self.result_main += "\n" + "Maximum localization error: " + str(round(np.amax(localization_result), 3))
        self.result_main += "\n" + "Average localization error: " + str(round(np.average(localization_result), 3))
        self.result_main += "\n" + "Median  localization error: " + str(round(np.median(localization_result), 3))
        self.result_main += "\n\n" + "Accuracy for zero to one: " + "%" + str(acc["zto"])
        self.result_main += "\n" + "Accuracy for one to two: " + "%" + str(acc["ott"])
        self.result_main += "\n" + "Accuracy for two to opss: " + "%" + str(acc["tto"])

        self.result_main += ""
        self.result_main += "\n\n" + "-> Classifier= " + str(self.algorithm)
        self.result_main += ""
        self.result_main += "\n" + "-> Algorithm learning time: " + str(round(self.learn_time, 4))
        self.result_main += "\n" + "-> Algorithm prediction time: " + str(round(self.prediction_time, 4))
        self.result_main += ""

    # find localization error
    def get_localization_error(self, estimated_loc, actual_loc):

        loc_err_est = [0] * 3
        loc_err_act = [0] * 3

        loc_err_est[0] = estimated_loc["est_x"]
        loc_err_est[1] = estimated_loc["est_y"]
        loc_err_est[2] = estimated_loc["est_z"]

        loc_err_act[0] = actual_loc["act_x"]
        loc_err_act[1] = actual_loc["act_y"]
        loc_err_act[2] = actual_loc["act_z"]

        return distance.euclidean(loc_err_est, loc_err_act)

    def accuracy_locations(self, loc_error):

        zero_to_one_accuracy = 0
        one_to_two_accuracy = 0
        two_to_opss_accuracy = 0

        for i in range(len(self.test_y)):
            if loc_error[i] <= 1:
                zero_to_one_accuracy += 1
            elif (loc_error[i] > 1) and (loc_error[i] <= 2):
                one_to_two_accuracy += 1
            else:
                two_to_opss_accuracy += 1

        accuracies = {}

        accuracies["zto"] = round((zero_to_one_accuracy * 100) / len(self.test_y), 2)
        accuracies["ott"] = round((one_to_two_accuracy * 100) / len(self.test_y), 2)
        accuracies["tto"] = round((two_to_opss_accuracy * 100) / len(self.test_y), 2)

        return accuracies
