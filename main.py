import os
import sys
from sensor.exception import SensorException
from sensor.logger import logging

import sys

def test_exception():  # Check the error in which line relate this line no {functio}
    try:
        logging.info("yha pr ek error zero division error")
        a = 10 / 0
    except Exception as e:
        raise SensorException(e, sys)
        # raise e

if __name__ == "__main__":
    try:
        test_exception()
    except SensorException as se:
        print(se)
