from flask import Flask
from src.logger import logging

app=Flask(__name__)

@app.route('/',methods=['GET','POSH'])
def index():
    logging.info("We are testing our login file")

    return "Welcome Mukesh to ML projects"

if __name__ == "__main__":
    app.run(debug=True) #5000
