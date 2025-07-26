from logger import logging
from exception import CustomException
import sys

if __name__ == "__main__":
    logging.info('Check Log for Logger and Exception')


    try:
        a=1/0
    except Exception as e:
        CustomException(e,sys)
