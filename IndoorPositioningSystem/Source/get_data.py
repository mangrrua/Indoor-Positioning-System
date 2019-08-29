import numpy as np

from Source.mongodb_operations import Queries


class PrepareTheData:

    def __init__(self):

        self.M_Operations = Queries()

        # mac address set to list
        self.list_training_sender_bssid = []

        self.train_X = np.array([])
        self.train_y = []

        self.test_X = np.array([])
        self.test_y = []

        self.count = 0

    def get_count_and_sender_bssid(self):
        return self.count, self.list_training_sender_bssid

    def import_file_to_mongodb(self, data_set_type, file_path):
        # self.M_Operations.remove_all_collection()
        self.M_Operations.import_data_from_file(data_set_type, file_path)

    def get_training_data(self, rssi_type):

        # self.M_Operations.remove_documents_result_training()

        self.list_training_sender_bssid = self.M_Operations.get_unique_sender_bssid()  # get uniqe sender_bssid from train data
        self.list_training_sender_bssid.sort()

        x_train_data = self.M_Operations.get_training_data()  # get all train data
        self.count = x_train_data.count()  # find train data size

        self.train_X = np.zeros((self.count, len(self.list_training_sender_bssid)))
        self.train_y = [0] * self.count

        data_rssi_values = {}
        i = 0
        for data in x_train_data:

            # prepare each row data
            row_data = np.zeros(len(self.list_training_sender_bssid))
            row_data[row_data == 0] = -100

            room_label = data["raw_measurement"][1]["receiver_location"]["room_label"]  # get room label from each data
            coordinate_x = float(data["raw_measurement"][1]["receiver_location"]["coordinate_x"])  # get coordinate_x from each data
            coordinate_y = float(data["raw_measurement"][1]["receiver_location"]["coordinate_y"])  # get coordinate_y from each data
            coordinate_z = float(data["raw_measurement"][1]["receiver_location"]["coordinate_z"])  # get coordinate_z from each data

            label = str(coordinate_x) + "," + str(coordinate_y) + "," + str(coordinate_z)  # set label each data (dataType= 'string') -> (20.33,1.68,12.37)

            average_rssi_values = self.M_Operations.get_rssi_value_for_train(data["data_id"])  # get average rssi values from mongodb operations

            if rssi_type == "Average":
                for dt in average_rssi_values:
                    row_data[self.list_training_sender_bssid.index(dt["_id"])] = dt["avg_rssi_value"]
            elif rssi_type == "Maximum":
                for dt in average_rssi_values:
                    row_data[self.list_training_sender_bssid.index(dt["_id"])] = dt["max_rssi_value"]
            elif rssi_type == "Minimum":
                for dt in average_rssi_values:
                    row_data[self.list_training_sender_bssid.index(dt["_id"])] = dt["min_rssi_value"]

            # all uniqe sender_bssid convert list to dict for insert mongodb
            for _sbssid in self.list_training_sender_bssid:
                data_rssi_values[_sbssid] = row_data[self.list_training_sender_bssid.index(_sbssid)]

            self.train_X[i, :] = row_data  # assign rowData to train_X (2D numpy array)
            self.train_y[i] = label  # assign label to train_y (1D numpy array)

            # data insert to mongodb
            self.M_Operations.insert_train_data(data_rssi_values, room_label, label)

            i += 1

        return self.train_X, self.train_y

    def get_runtime_data(self, rssi_type):

        # self.M_Operations.remove_documents_result_test()

        y_test_data = self.M_Operations.get_test_data()
        count = y_test_data.count()

        # initialize test_X, and test_y arrays
        self.test_X = np.zeros((count, len(self.list_training_sender_bssid)))
        self.test_y = [0] * count

        data_rssi_values = {}
        i = 0
        for data in y_test_data:

            # prepare each row data
            row_data = np.zeros(len(self.list_training_sender_bssid))
            row_data[row_data == 0] = -100

            room_label = data["raw_measurement"][1]["receiver_location"]["room_label"]  # get room label from each data
            coordinate_x = float(data["raw_measurement"][1]["receiver_location"]["coordinate_x"])  # get coordinate_x from each data
            coordinate_y = float(data["raw_measurement"][1]["receiver_location"]["coordinate_y"])  # get coordinate_y from each data
            coordinate_z = float(data["raw_measurement"][1]["receiver_location"]["coordinate_z"])  # get coordinate_z from each data

            label = str(coordinate_x) + "," + str(coordinate_y) + "," + str(coordinate_z)  # set label each data (dataType= 'string') -> (20.33,1.68,12.37)

            average_rssi_values = self.M_Operations.get_rssi_value_for_test(data["data_id"])  # get average rssi values fot this data

            if rssi_type == "Average":
                for dt in average_rssi_values:
                    if dt["_id"] in self.list_training_sender_bssid:
                        row_data[self.list_training_sender_bssid.index(dt["_id"])] = dt["avg_rssi_value"]
            elif rssi_type == "Maximum":
                for dt in average_rssi_values:
                    if dt["_id"] in self.list_training_sender_bssid:
                        row_data[self.list_training_sender_bssid.index(dt["_id"])] = dt["max_rssi_value"]
            elif rssi_type == "Minimum":
                for dt in average_rssi_values:
                    if dt["_id"] in self.list_training_sender_bssid:
                        row_data[self.list_training_sender_bssid.index(dt["_id"])] = dt["min_rssi_value"]

            # all uniqe sender_bssid convert list to dict for insert mongodb
            for _sbssid in self.list_training_sender_bssid:
                data_rssi_values[_sbssid] = row_data[self.list_training_sender_bssid.index(_sbssid)]

            self.test_X[i, :] = row_data  # assign row_data to train_X (2D numpy array)
            self.test_y[i] = label  # assign label to train_y (1D numpy array)

            # data insert to mongodb
            self.M_Operations.insert_test_data(data_rssi_values, room_label, label)

            i += 1

        return self.test_X, self.test_y

    def get_sender_bssid_for_data_id(self, data_id):

        s_bssid = {}

        index = 0
        for i in self.M_Operations.visualization_get_sender_bssid_for_data_id(data_id):
            s_bssid[index] = i["_id"]
            index += 1

        s_bssid = np.array(list(s_bssid.values()))

        return s_bssid
