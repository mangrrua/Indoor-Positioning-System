from scipy.spatial import distance
import numpy as np

# hold string for result
resultString=""

def nearest_tree_point_prediction(train_X, train_y, test_X, test_y):
    resultString=""
    distances = {}
    est_loc = {}
    act_loc = {}
    result_loc_errors = np.zeros(len(test_y))

    index = 0
    for test_data in test_X:

        d_index = 0
        for train_data in train_X:
            dist_result = distance.euclidean(test_data, train_data)
            distances[d_index] = dist_result

            d_index += 1

        sorted_distances = sorted(distances.items(), key=lambda x: x[1])

        nearest_first_x = train_y[sorted_distances[0][0]].split(",")[0]
        nearest_second_x = train_y[sorted_distances[1][0]].split(",")[0]
        nearest_third_x = train_y[sorted_distances[2][0]].split(",")[0]

        nearest_first_y = train_y[sorted_distances[0][0]].split(",")[1]
        nearest_second_y = train_y[sorted_distances[1][0]].split(",")[1]
        nearest_third_y = train_y[sorted_distances[2][0]].split(",")[1]

        nearest_first_z = train_y[sorted_distances[0][0]].split(",")[2]

        est_loc["est_x"] = ((float(nearest_first_x) + float(nearest_second_x) + float(nearest_third_x)) / 3)
        est_loc["est_y"] = ((float(nearest_first_y) + float(nearest_second_y) + float(nearest_third_y)) / 3)
        est_loc["est_z"] = float(nearest_first_z)

        act_loc["act_x"] = float(test_y[index].split(",")[0])
        act_loc["act_y"] = float(test_y[index].split(",")[1])
        act_loc["act_z"] = float(test_y[index].split(",")[2])

        result_loc_errors[index] = get_localization_error(est_loc, act_loc)

        print("Data ", (index + 1))
        print("Estimated location (x, y, z): " + "(" +
              str(round(est_loc["est_x"], 2))
              + ", " +
              str(round(est_loc["est_y"], 2))
              + ", " +
              str(round(est_loc["est_z"], 2))
              + ")")

        print("Actual location (x, y, z): " + "(" +
              str(round(act_loc["act_x"], 2))
              + ", " +
              str(round(act_loc["act_y"], 2))
              + ", " +
              str(round(act_loc["act_z"], 2))
              + ")")

        print("Localization error: " + str(round(result_loc_errors[index], 3)))

        print("")

        global resultString
        resultString += "Data " + str(index + 1) + "\n" + "Estimated location (x, y, z): " + "(" + \
                                  str(round(est_loc["est_x"], 2)) + ", " + \
                                  str(round(est_loc["est_y"], 2)) + ", " + \
                                  str(round(est_loc["est_z"], 2)) + ")" + "\n" + "Actual location (x, y, z): " + "(" + \
                                  str(round(act_loc["act_x"], 2)) + ", " + \
                                  str(round(act_loc["act_y"], 2)) + ", " + \
                                  str(round(act_loc["act_z"], 2)) + ")" + "\nLocalization error: " + str(
            round(result_loc_errors[index], 3)) + "\n\n"
        index += 1

    print_results(result_loc_errors)
    acc = accuracy_locations(result_loc_errors, test_y)

    print("Accuracy for zero to one: " + "%" + str(acc["zto"]))
    print("Accuracy for one to two: " + "%" + str(acc["ott"]))
    print("Accuracy for two to opss: " + "%" + str(acc["tto"]))
    print("")

    resultString+= "\n\n" + "Accuracy for zero to one: " + "%" + str(acc["zto"])
    resultString+= "\n" + "Accuracy for one to two: " + "%" + str(acc["ott"])
    resultString+= "\n" + "Accuracy for two to opss: " + "%" + str(acc["tto"])




def print_results(localization_result):

        print("--------- Results --------- ")
        print("Minimum localization error: ", round(np.amin(localization_result), 3))
        print("Maximum localization error: ", round(np.amax(localization_result), 3))
        print("Average localization error: ", round(np.average(localization_result), 3))
        print("Median  localization error: ", round(np.median(localization_result), 3))
        print("")

        global resultString
        resultString+= "\n\n--------- Results --------- "
        resultString += "\n" + "Minimum localization error: " + str(round(np.amin(localization_result), 3))
        resultString += "\n" + "Maximum localization error: " + str(round(np.amax(localization_result), 3))
        resultString += "\n" + "Average localization error: " + str(round(np.average(localization_result), 3))
        resultString += "\n" + "Median  localization error: " + str(round(np.median(localization_result), 3))



def get_localization_error(est_locations, actual_locations):

    loc_err_est = [0] * 3
    loc_err_act = [0] * 3

    loc_err_est[0] = est_locations["est_x"]
    loc_err_est[1] = est_locations["est_y"]
    loc_err_est[2] = est_locations["est_z"]

    loc_err_act[0] = actual_locations["act_x"]
    loc_err_act[1] = actual_locations["act_y"]
    loc_err_act[2] = actual_locations["act_z"]

    return distance.euclidean(loc_err_est, loc_err_act)


def accuracy_locations(loc_error, test_y):

        zero_to_one_accuracy = 0
        one_to_two_accuracy = 0
        two_to_opss_accuracy = 0

        for i in range(len(test_y)):
            if loc_error[i] <= 1:
                zero_to_one_accuracy += 1
            elif (loc_error[i] > 1) and (loc_error[i] <= 2):
                one_to_two_accuracy += 1
            else:
                two_to_opss_accuracy += 1

        accuracies = {}

        accuracies["zto"] = round((zero_to_one_accuracy * 100) / len(test_y), 2)
        accuracies["ott"] = round((one_to_two_accuracy * 100) / len(test_y), 2)
        accuracies["tto"] = round((two_to_opss_accuracy * 100) / len(test_y), 2)

        return accuracies
