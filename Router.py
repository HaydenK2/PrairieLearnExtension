from flask import Flask, render_template
import json
import datetime
from scraper import *

app = Flask(__name__)
#app.config['SECRET_KEY'] = "tester"


@app.route("/home", methods=('GET', 'POST'))
@app.route("/")

def index():
    dictionary = webScrape()

    json_object = json.dumps(dictionary, indent=4)
    
    # Writing to sample.json
    with open("JSON\sample.json", "w") as outfile:
        outfile.write(json_object)

    #get the data from json
    event_data = []
    f = open('JSON\sample.json')

    data = json.load(f)
    for i in data:

        event = []
        event.append(i["title"])
        event.append(i["date"])

        text_color = "0"
        current_time = datetime.datetime.now()
        splitted_date = i["date"].split("-")
        event_date_day = int(splitted_date[2])
        event_date_month = int(splitted_date[1])
        event_date_year = int(splitted_date[0])
        if (current_time.year > event_date_year or current_time.month > event_date_month or current_time.day > event_date_day or abs(event_date_day - current_time.day) < 3):
            text_color = "1"

        event.append(text_color)

        event_data.append(event)
    f.close()


    #sort by day from first to last day
    for i in range(len(event_data)):
        curr_date = event_data[i][1]
        splitted_curr_date = curr_date.split("-")
        curr_date_day = int(splitted_curr_date[2])
        for j in range (len(event_data) - 1): 
            next_date = event_data[j][1]
            splitted_next_date = next_date.split("-")
            next_date_day = int(splitted_next_date[2])

            if (curr_date_day < next_date_day): 
                temp_event = event_data[i]
                event_data[i] = event_data[j]
                event_data[j] = temp_event

    #sort by month from first to last month
    for i in range(len(event_data)):
        curr_date = event_data[i][1]
        splitted_curr_date = curr_date.split("-")
        curr_date_month = int(splitted_curr_date[1])

        for j in range (len(event_data) - 1): 
            next_date = event_data[j][1]
            splitted_next_date = next_date.split("-")
            next_date_month = int(splitted_next_date[1])

            if (curr_date_month < next_date_month): 
                temp_event = event_data[i]
                event_data[i] = event_data[j]
                event_data[j] = temp_event

    #sort by year smallest year to biggest year
    for i in range(len(event_data)):
        curr_date = event_data[i][1]
        splitted_curr_date = curr_date.split("-")
        curr_date_year = int(splitted_curr_date[0])

        for j in range (len(event_data) - 1): 
            next_date = event_data[j][1]
            splitted_next_date = next_date.split("-")
            next_date_year = int(splitted_next_date[0])

            if (curr_date_year < next_date_year): 
                temp_event = event_data[i]
                event_data[i] = event_data[j]
                event_data[j] = temp_event

    #add number
    for i in range(len(event_data)):
        assignment_num = i + 1
        event_data[i].append(str(assignment_num))           

    #render html file with the data from JSON
    #https://stackoverflow.com/questions/22259847/application-not-picking-up-css-file-flask-python
    return render_template('prairielearnplusplus.html', output = event_data)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8080, app)
    #app.run(debug=True)