from flask import Flask
from housing.exception import HavingException
from housing.logger import logging
import sys

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("Testing Exception")
    except Exception as e:
        housing=HavingException(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing log")
    return "THIS IS CI CD APP"


if __name__=="__main__":
    app.run(debug=True)