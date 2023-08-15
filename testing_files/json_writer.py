import json
from flask import Flask, render_template, jsonify
#https://www.youtube.com/watch?v=v2TSTKlrPwo
application = Flask(__name__)

random_decimal = 10

#@application.route('/createData', methods=["POST"])
def createData():
    dictionary = [{
        "assignemntname": "sfdasfsfaq",
        "duedate": "Fri, Nov 1"
    },

    {
        "assignemntname": "afda",
        "duedate": "Fri, Nov 7"
    },

    {
        "assignemntname": "fsadfasfasfsa",
        "duedate": "Fri, Nov 10"
    },

    {
        "assignemntname": "asfdasl;nglskhgdahslkghkasl",
        "duedate": "Fri, Nov 14"
    }]
    
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    
    # Writing to sample.json
    with open("JSON\sample.json", "w") as outfile:
        outfile.write(json_object)

    print("Creating Data")
    #random_decimal = 11
    #return jsonify(' ', render_template('test_template.html', x = random_decimal))
createData()
#application.run()