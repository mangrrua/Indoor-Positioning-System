from pymongo import MongoClient
import os


class Queries:

    # ------------------ DEFINE MONGODB CONNECTIONS ------------------ #
    def __init__(self):

        self.client = MongoClient("localhost", 27017)  # define Mongodb client

        database_name = "wifi_beacon_rssi_twist_big_macbook"  # database name

        self.db_id = self.client[database_name]  # define database from client

        self.col_train = self.db_id["training"]  # define train collection from database
        self.col_test = self.db_id["runtime"]  # define test collection from database

        self.col_result_train = self.db_id["result_training"]  # define result train collection from database
        self.col_result_test = self.db_id["result_test"]  # define result test collection from database
    # ----------------------------------------------------------------- #

    # ------------- RETURN DATA FROM MONGODB COLLECTIONS ------------- #
    def get_training_data(self):
        return self.col_train.find()  # return all train data

    def get_test_data(self):
        return self.col_test.find()  # return all test data

    def get_unique_sender_bssid(self):
        return self.col_train.distinct('raw_measurement.sender_bssid')  # return unique sender bssid from all training data
    # ----------------------------------------------------------------- #

    # -------------- REMOVE DOCUMENTS FOR EACH TEST FILE -------------- #
    def remove_documents_training(self):
        self.col_train.remove({})  # remove all documents from train collection for new data

    def remove_documents_test(self):
        self.col_test.remove({})  # remove all documents from test collection for new data

    def remove_documents_result_training(self):
        self.col_result_train.remove({})  # remove all documents from result train collection for new data

    def remove_documents_result_test(self):
        self.col_result_test.remove({})

    def remove_all_collection(self):
        self.col_train.drop()
        self.col_test.drop()
        self.col_result_train.drop()
        self.col_result_test.drop()
    # ----------------------------------------------------------------- #

    # ----------------- GET RSSI VALUES FOR EACH DATA ----------------- #
    def get_rssi_value_for_train(self, data_id):

        # get max, min and avg rssi values with mongodb aggregation query from each train data
        pipeline = [

            {
                "$match": {
                    "data_id": data_id  # find data with $match
                }
            },
            {
                "$unwind": "$raw_measurement"  # select inner array from each train data
            },
            {
                "$group": {
                    "_id": "$raw_measurement.sender_bssid",  # group by sender bssid
                    "avg_rssi_value": {"$avg": "$raw_measurement.rssi"},  # find avg rssi value for each sender_bssid
                    "max_rssi_value": {"$max": "$raw_measurement.rssi"},  # find max rssi value for each sender_bssid
                    "min_rssi_value": {"$min": "$raw_measurement.rssi"}   # find min rssi value for each sender_bssid
                }
            }
        ]

        return self.col_train.aggregate(pipeline)  # use aggregate query

    def get_rssi_value_for_test(self, data_id):

        # get max, min and avg rssi values with mongodb aggregation query from each test data
        pipeline = [

            {
                "$match": {
                    "data_id": data_id  # find data with $match
                }
            },
            {
                "$unwind": "$raw_measurement"  # select inner array from each train data
            },
            {
                "$group": {
                    "_id": "$raw_measurement.sender_bssid",  # group by sender bssid
                    "avg_rssi_value": {"$avg": "$raw_measurement.rssi"},  # find avg rssi value for each sender_bssid
                    "max_rssi_value": {"$max": "$raw_measurement.rssi"},  # find max rssi value for each sender_bssid
                    "min_rssi_value": {"$min": "$raw_measurement.rssi"}   # find min rssi value for each sender_bssid
                }
            }
        ]

        return self.col_test.aggregate(pipeline)  # use aggregate query
    # ------------------------------------------------------------------ #

    # --------------- INSERT RESULT VALUES FOR EACH DATA --------------- #
    def insert_train_data(self, data, room_label, coordinates):

        # create dict for insert mongodb
        data = {
            "raw_measurement": data,  # inner documents
            "room_label": room_label,
            "coordinates": coordinates
        }

        self.col_result_train.insert(data)  # insert data to result train collection

    def insert_test_data(self, data, room_label, coordinates):

        # create dict for insert mongodb
        data = {
            "raw_measurement": data,  # inner documents
            "room_label": room_label,
            "coordinates": coordinates
        }

        self.col_result_test.insert(data)  # insert data to result train collection

    # ----------------------------------------------------------------- #


    def import_data_from_file(self, data_set_type, file_path):

        self.col_result_train.drop()
        self.col_result_test.drop()
        try:
            if data_set_type == "training":
                self.col_train.drop()
                os.system(
                    'mongoimport --db wifi_beacon_rssi_twist_big_macbook --collection training --type json --file ' + file_path)
                # self.col_train.ensure_index({"data_id": 1})
            elif data_set_type == "test":
                self.col_test.drop()
                os.system(
                    'mongoimport --db wifi_beacon_rssi_twist_big_macbook --collection runtime --type json --file ' + file_path)
                # self.col_test.ensure_index({"data_id": 1})
        except:
            print("File type must be 'JSON' ")

    # --------------------- VISUALIZATION ----------------------------- #
    def visualization_number_of_rssi_values(self,sender_Bssid,id):

        pipeline = [
            {"$match": {"data_id":id}},
            {"$unwind": "$raw_measurement"},
            {
                "$group": {
                    "_id": "$raw_measurement.sender_bssid",
                    "rssi": {"$push": "$raw_measurement.rssi"}
                }
            },
            {"$match": {"_id": sender_Bssid}},
            {"$unwind": "$rssi"},
            {"$group": {
                "_id": {"sender_bssid": "$_id", "rssi": "$rssi"},
                "size": {"$sum": 1}
            }
            },
            {
                "$sort": {"_id.rssi": -1}
            }
        ]

        return self.col_train.aggregate(pipeline)

    # -----------------------VISUALIZATION---------------------------------- #

    def visualization_get_sender_bssid_for_data_id(self, data_id):

        pipeline = [
            {"$match": {"data_id": data_id}},
            {"$unwind": "$raw_measurement"},
            {
                "$group": {
                    "_id": "$raw_measurement.sender_bssid"
                }
            }]

        return self.col_train.aggregate(pipeline)

    # ---------------------------VISUALIZATION------------------------------- #
    def visualization_number_of_rssi_values_statistics(self,data_id,sender_bssid):
        pipeline = [
            {"$match": {"data_id": data_id}},
            {"$unwind": "$raw_measurement"},
            {
                "$group": {
                    "_id": "$raw_measurement.sender_bssid",
                    "max1": {"$max": "$raw_measurement.rssi"},
                    "min1": {"$min": "$raw_measurement.rssi"},
                    "avg1": {"$avg": "$raw_measurement.rssi"},
                    "rssi": {"$push": "$raw_measurement.rssi"},
                    "location": {"$addToSet": {
                        "room_label": "$raw_measurement.receiver_location.room_label",
                        "coordinate_x": "$raw_measurement.receiver_location.coordinate_x",
                        "coordinate_y": "$raw_measurement.receiver_location.coordinate_y",
                        "coordinate_z": "$raw_measurement.receiver_location.coordinate_z"
                    }}}
            },
            {"$match": {"_id": sender_bssid}},
            {"$unwind": "$rssi"},
            {"$group": {
                "_id": {"sender_bssid": "$_id", "rssi": "$rssi"},
                "size": {"$sum": 1},
                "info": {"$addToSet": {
                    "avg_rssi": "$avg1",
                    "max_rssi": "$max1",
                    "min_rssi": "$min1",
                    "location": "$location"
                }}}
            },
            {"$sort": {"_id.rssi": -1}}
        ]

        return self.col_train.aggregate(pipeline)



