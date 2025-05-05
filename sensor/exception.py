# I can see the error in exception.py file

import sys
import os # kisme error aa rha hai pta chlta hai


def error_message_detail(error,error_detail:sys):  # detail for error (this is a function)
    _,_,exc_tb =error_detail.exc_info() # tupple me error deta hai

    filename = exc_tb.tb_frame.f_code.co_filename # ye error batata hai kis file me error hai


    error_message = "error occured and the filename is [{0}] and the linenumber is [{1}] and error is [{2}]".format(filename,exc_tb.tb_lineno,str(error))

    return error_message
  





##oops Concept
class SensorException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)

        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
        