from flask import Flask
from flask import jsonify
from flask import abort
from flask import request
from db_create import create_db
from routes import *
from reading_db_manipulation import *
from reading_statistics import *
import datetime

# initialize flask app and create database, if it doesn't exist
app = Flask(__name__)
create_db()

@app.route(INDEX_PAGE, methods=['GET'])
def index_page():
    return f"<p> index page </p> "

@app.route(LIST_ALL, methods=['GET'])
def show_all_readings():
    return jsonify(get_all_readings())

@app.route(FIND, methods=['GET'])
def retrieve_by_id(id):
    reading = find_by_id(id)

    if reading is None:
        return abort(404)

    return jsonify(reading)

@app.route(ADD, methods=['POST'])
def add_reading():
    new_reading = request.get_json()

    #check if dates are the correct format
    try:
        timeStamp = datetime.datetime.fromisoformat(new_reading['timeStamp'])
    except:
        return abort(400)
        
    if type(new_reading['value']) is float:
        insert_reading(new_reading['value'], timeStamp)
    else:
        return abort(400)

    return new_reading

@app.route(EDIT, methods=['PUT'])
def edit_reading(id):
    new_reading = request.get_json()

    #check if dates are the correct format
    try:
        timeStamp = datetime.datetime.fromisoformat(new_reading['timeStamp'])
    except:
        return abort(400)

    if type(new_reading['value']) is float:
        if edit_db_reading(id, new_reading['value'], timeStamp):
            return new_reading
        else:
            return abort(404) 
    else:
        return abort(400)

@app.route(DELETE, methods=['DELETE'])
def delete_reading(id):
    reading = delete_db_reading(id)
    
    if reading is not None:
        return jsonify(reading)
    else:
        return abort(404)

@app.route(STATISTICS, methods=['GET'])
def retrieve_statistics():
    time = request.get_json()

    #check if dates are the correct format
    try:
        start = datetime.datetime.fromisoformat(time['startDate'])
        end = datetime.datetime.fromisoformat(time['endDate'])
    except:
        return abort(400)

    correct_values = get_readings_in_specific_time_window(start, end)

    if len(correct_values) == 0:
        return abort(404)

    readings = get_all_readings()
    distribution = is_normal_distribution(readings=correct_values, p_treshold=0.05)

    if distribution:
        result = {
        "count" : len(correct_values),
        "mean" : get_readings_mean(correct_values),
        "variance" : get_readings_variance(correct_values),
        "is_normal_distribution" : distribution,
        "confidence interval" : get_confidence_treshold(correct_values, treshold=.95),
        "is_stationary" : is_stationary(readings, 0.01)
    }
    # if distribution is false don't return confidence interval
    else:
        result = {
        "count" : len(correct_values),
        "mean" : get_readings_mean(correct_values),
        "variance" : get_readings_variance(correct_values),
        "is_normal_distribution" : distribution,
        "is_stationary" : is_stationary(readings, 0.01)
    }
    
    return result

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
