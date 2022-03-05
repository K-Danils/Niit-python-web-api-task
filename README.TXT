IF FLASK IS NOT RECOGNIZED, INSTALL ALL PACKAGES IN REQUIREMENTS MANUALLY USING: pip install <name of the package>

To start open project in dev container, open terminal (bash) and run : 
    cd src
    export FLASK_APP=main.py
    flask run --port=8080

supported endpoints:
    *) index = "/" 
    no parameters required, 
    expected response : 200

    *) find reading = "/find/<id>" 
    parameter required: link - id (int), 
    expected response: 200, if found value, if not then 404, 
    returned value: the found reading

    *) edit reading = "/edit/<id>" 
    parameter required: link - id (int), body - json {value : (float), timeStamp : {datetime}}, 
    expected response: 200, if found value, if not then 404, if incorrect format used then 400
    returned value: the edited reading

    *) list all readings = "/list-readings" 
    no parameters required, 
    expected response : 200, 
    returned value : all found readings

    *) add reading = "/add" 
    parameter required: link - id (int), body - json {value : (float), timeStamp : {datetime}}, 
    expected response: 200, if incorrect format used then 400
    returned value: the added reading

    *) delete reading = "/delete/<id>" 
    parameter required: link - id (int), 
    expected response: 200, if reading not found then 404
    returned value: the deleted reading

    *) show reading statistics = "/statistics/<timeStamp>" 
    parameter required: link - timeStamp(datetime), 
    expected response: 200, if not found then 404, 
    returned value : all statistical information about readings

all values are returned as json
all parameters are escaped before they are put into sql querries
timeStamp must use format similar to: 2012-12-12 10:10:10, string to datetime is converted using datetime.fromisoformat(timeStamp)

