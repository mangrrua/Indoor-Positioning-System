import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from Source.mongodb_operations import Queries


class Visualization:

    def __init__(self, train_X, train_y, test_X, test_y):

        self.train_X = train_X
        self.train_y = train_y

        self.test_X = test_X
        self.test_y = test_y

        self.mo = Queries()

    def prepare_data_sets(self):

        y_train = np.array([0] * (len(self.train_y)))
        unique_train_y = np.unique(self.train_y)

        index = 0
        number_of_label = 0
        for t_data in self.train_y:
            for u_data in unique_train_y:
                if t_data == u_data:
                    y_train[index] = number_of_label
                    number_of_label += 1
            index += 1

        return y_train

    def scatter_visualize(self, first, second):

        y_train = self.prepare_data_sets()

        # plt.scatter(x=self.train_X[:, first], y=self.train_X[:, second], c=y_train)
        plt.scatter(x=self.train_X[:, first],color='red', y=self.train_X[:, second])
        plt.title("Scatter Visualization")
        plt.ylabel("Features: " + str(first))
        plt.xlabel("Features: " + str(second))
        plt.show()

    def hist_visualize(self, index):

        fig = plt.figure()

        ax = fig.add_subplot(1, 1, 1)
        ax.hist(self.train_X[:, index])

        plt.title("Hist Visualization")
        plt.xlabel("Features: " + str(index))
        plt.ylabel("Number of location")
        plt.show()

    def bar_chart_rssi_values(self, data_id, s_bssid):

        rssi_value = {}
        number_of_rssi = {}

        index = 0
        for i in self.mo.visualization_number_of_rssi_values(s_bssid,data_id):
            rssi_value[index] = i["_id"]["rssi"]
            number_of_rssi[index] = i["size"]
            index += 1

        rssi_value = np.array(list(rssi_value.values()))
        number_of_rssi = np.array(list(number_of_rssi.values()))

        plt.figure(figsize=(12, 8))

        pd_number_of_rssi = pd.Series.from_array(number_of_rssi)

        ax = pd_number_of_rssi.plot(kind='bar')
        ax.set_title("Data id: " + str(data_id) + "\n" + "Sender Bssid: " + s_bssid)
        ax.set_xlabel("RSSI Values in dBm")
        ax.set_ylabel("Number of RSSI values")
        ax.set_xticklabels(rssi_value)

        rects = ax.patches

        for rect, label in zip(rects, number_of_rssi):
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')

        plt.show()

    def line_average_rssi_values(self, data_id):

        sender_bssid = {}
        avg_rssi_values = {}

        index = 0
        for i in self.mo.get_rssi_value_for_train(data_id):
            sender_bssid[index] = i["_id"]
            avg_rssi_values[index] = i["avg_rssi_value"]
            index += 1

        sender_bssid = np.array(list(sender_bssid.values()))
        avg_rssi_values = np.array(list(avg_rssi_values.values()))

        count = len(sender_bssid)

        x = [0] * count
        v = 0
        for i in range(1, count + 1):
            x[v] = i
            v += 1

        plt.plot(x, avg_rssi_values, marker='o', linestyle='--', color='red')
        plt.title("For data id " + str(data_id))
        plt.xlabel("Sender Bssid")
        plt.ylabel("Average values of RSSI")
        plt.subplots_adjust(bottom=0.30)

        fig_manager = plt.get_current_fig_manager()
        fig_manager.resize(*fig_manager.window.maxsize())

        plt.xticks(x, sender_bssid, rotation='vertical')
        plt.show()

    def bar_chart_rssi_values_statistics(self, data_id, s_bssid):

        rssi_value = {}
        number_of_rssi = {}
        info = {}

        index = 0
        for i in self.mo.visualization_number_of_rssi_values_statistics(data_id,s_bssid):
            rssi_value[index] = i["_id"]["rssi"]
            number_of_rssi[index] = i["size"]
            for k in i["info"]:
                info["avg_rssi"] = k["avg_rssi"]
                info["min_rssi"] = k["min_rssi"]
                info["max_rssi"] = k["max_rssi"]
                for l in k["location"]:
                    info["room_label"] = l["room_label"]
                    info["coordinate_x"] = l["coordinate_x"]
                    info["coordinate_y"] = l["coordinate_y"]
                    info["coordinate_z"] = l["coordinate_z"]
            index += 1

        rssi_value = np.array(list(rssi_value.values()))
        number_of_rssi = np.array(list(number_of_rssi.values()))

        plt.figure(figsize=(12, 8))

        pd_number_of_rssi = pd.Series.from_array(number_of_rssi)

        ax = pd_number_of_rssi.plot(kind='bar')
        ax.set_title("Data id: " + str(data_id) + "\n" + "Sender Bssid: " + s_bssid)
        ax.set_xlabel("RSSI Values in dBm")
        ax.set_ylabel("Number of RSSI values")
        ax.set_xticklabels(rssi_value)

        rects = ax.patches

        for rect, label in zip(rects, number_of_rssi):
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')

        plt.show()

        return info

