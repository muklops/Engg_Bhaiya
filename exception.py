from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os,sys

app=Flask(__name__)

@app.route('/',methods=['GET','POSH'])
def index():
    try:
        raise Exception("We are Testing our Exception file") #error
    except Exception as e:
        ML=CustomException(e,sys)
        logging.info(ML.error_message)
        logging.info("We are testing our login file")

        return "Welcome Mukesh to ML projects"

if __name__ == "__main__":
    app.run(debug=True) #5000
