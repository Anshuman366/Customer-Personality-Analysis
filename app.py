
import logging
from flask import Flask
from Personality_analysis_main.Logger import logging

app=Flask(__name__)

@app.route("/",methods=["GET",'POST'])
def fun():
    logging.info("THis is logging module")
    return "HELLO LEARNERS . COMPLETE CICD PIPELINE HAS BEEN DEVELOPED"
    
if __name__=="__main__":
    app.run(debug=True)