from markupsafe import escape
import sqlite3 as sq
from db_info import db_path
from db_info import db_name

def find_by_id(id):
    # returns single reading element if found
    con = sq.connect(db_path)
    cur = con.cursor()

    reading = None
    for row in cur.execute(f''' SELECT * 
                                FROM {db_name} 
                                WHERE id = {escape(id)}
                                '''):
        reading = row

    con.close()
    return reading

def get_all_readings():
    #returns list of all reading elements
    con = sq.connect(db_path)
    cur = con.cursor()

    readings = []
    for row in cur.execute(f'SELECT * FROM {db_name}'):
        readings.append(row)

    con.close()

    return readings

def edit_db_reading(id, value, timeStamp):
    #returns true if edit was successful, if not false
    con = sq.connect(db_path)
    cur = con.cursor()

    reading = find_by_id(id)

    if reading is not None:
        # check if new values are not None, if they are, keep the old values
        # other checks can be added here if necessary
        reading_value = reading[1]
        reading_timeStamp = reading[2]

        if value is not None:
            reading_value = value

        if timeStamp is not None:
            reading_timeStamp = timeStamp

        cur.execute(f'''UPDATE {db_name} 
                        SET 
                        value={escape(reading_value)}, 
                        timeStamp='{escape(reading_timeStamp)}' 
                        WHERE id={escape(id)}
                        ''')
        con.commit()
        con.close()

        return True

    return False

def delete_db_reading(id):
    # returns true if delete was successful, if not false
    con = sq.connect(db_path)
    cur = con.cursor()

    reading = find_by_id(id)

    if reading is not None:
        cur.execute(f"DELETE FROM {db_name} WHERE id={escape(id)}")
        con.commit()
        con.close()

        return reading

    return None

def get_readings_in_specific_time_window(startingDate, endDate):
    #returns list of all elements with the same timeStamp as provided
    con = sq.connect(db_path)
    cur = con.cursor()

    correct_values = []

    for row in cur.execute(f''' SELECT * 
                                FROM {db_name} 
                                WHERE 
                                timeStamp >= '{escape(startingDate)}' 
                                AND 
                                timeStamp <= '{escape(endDate)}'
                                '''):
        correct_values.append(row)

    con.close()
    
    return correct_values

def insert_reading(value, timeStamp):
    reading = get_latest_reading_entry()

    con = sq.connect(db_path)
    cur = con.cursor()

    id = reading[0] + 1 if len(reading) > 0 else 1

    cur.execute(f'''INSERT INTO {db_name} 
                    VALUES (
                        {id}, 
                        {escape(value)}, 
                        '{escape(timeStamp)}'
                        )''')

    con.commit()
    con.close()

def get_latest_reading_entry():
    con = sq.connect(db_path)
    cur = con.cursor()

    reading = []
    for row in cur.execute(f'''SELECT * 
                              FROM {db_name} 
                              GROUP BY id
                              '''):
        reading = row
    con.commit()
    con.close()

    return reading

def reading_to_string(reading):
    return f'''
    <p> 
    Reading: id={reading[0]} 
    value={reading[1]} 
    time stamp={reading[2]}
    </p>'''
