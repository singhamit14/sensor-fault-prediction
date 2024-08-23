from sensor.exception import SensorException
from sensor.logger import logging
from sensor.utils import dump_csv_to_mongo
import sys


# def test_exception():
#     try:
#         logging.info("This is Error:- ")
#         a = 1 / 0
#     except Exception as e:
#         raise SensorException(e, sys)


if __name__ == "__main__":
    file_path = "C:/Users/lenovo/Desktop/sensor-fault-prediction/EDA/aps_failure_dataset.csv"
    database_name = "sensordatabase"
    collection_name = "sensor"
    dump_csv_to_mongo(file_path,database_name,collection_name)























    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)