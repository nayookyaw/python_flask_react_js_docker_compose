from flask import request, jsonify

from Common.TextConstants import TextConstants
from Services.Logging.LoggingInfo import LoggingInfo

from DAO.Sensor.SensorRepository import SensorRepository

class SensorController:

    def get_sensor_count():
        total_count = SensorRepository.get_sensor_count()

        database_size = SensorRepository.get_database_size()

        res_data = {
            'total_count' : total_count['count'],
            'database_size' : float(database_size['database_size'])
        }
        
        return jsonify({ "status" : TextConstants.GET_SENSOR_COUNT_SUCCESS, "data" : res_data }), 200

    def get_sensor_list():

        offset = 0
        limit = 1

        sensor = SensorRepository.get_sensor_list(offset, limit)
        
        return jsonify({ "status" : TextConstants.GET_SENSOR_LIST_SUCCESS, "data" : sensor }), 200