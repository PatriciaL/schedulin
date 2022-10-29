import pandas as pd
import pymysql
from sqlalchemy import create_engine
import json

user = "PatriciaLafuente"
passw = "Lapatri86!!"
host = "PatriciaLafuente.mysql.pythonanywhere-services.com"
database = "PatriciaLafuente$schedulin"

db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}/{3}' \
        .format(user, passw, host, database), \
    connect_args = {'connect_timeout': 10})
conn = db.connect()

#databases = conn.execute(
    #"SHOW DATABASES;"
#)

#conn.execute("""
#CREATE TABLE neighbors(
    #id_user VARCHAR(255) ,
    #name VARCHAR(255),
    #email VARCHAR(255))
    #""")

#conn.execute("""
#CREATE TABLE resources(
    #id_resource VARCHAR(255) ,
   #type VARCHAR(255),
    #max_pax VARCHAR(255)
    #price VARCHAR(255),
    #id_timetable VARCHAR(255),
    #in_advance)
    #""")

#conn.execute("""
#CREATE TABLE timetable(
    #id VARCHAR(255) ,
    #start_time VARCHAR(255),
    #end_time VARCHAR(255))
    #""")


#conn.execute("""
#CREATE TABLE booking(
    #id VARCHAR(255) ,
    #id_resource VARCHAR(255),
    #id_neighbour VARCHAR(255),
    #booking_status VARCHAR(255),
    #start_time VARCHAR(255),
    #end_time VARCHAR(255),
    #num_pax VARCHAR(255)
    #)
    #""")

    #VAMOS A CREAR TABLAS SEGUN EJEMPLO DEL PROFESOR

timetable_creation = """
    CREATE TABLE IF NOT EXISTS timetable (
        id INT AUTO_INCREMENT PRIMARY KEY,
        start_time TIME,
        end_time TIME,
        creation_date TIMESTAMP,
        modification_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deletion_date TIMESTAMP
    )  ENGINE=INNODB;
"""
resource_creation = """
    CREATE TABLE IF NOT EXISTS resource (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timetable_id INTEGER,
        type VARCHAR(255),
        description VARCHAR(2000),
        max_pax INTEGER,
        price DECIMAL(4, 2),
        hours_in_advance INTEGER,
        creation_date TIMESTAMP,
        modification_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deletion_date TIMESTAMP,
        FOREIGN KEY(timetable_id) REFERENCES timetable(id)
    )  ENGINE=INNODB;
"""
user_creation = """
    CREATE TABLE IF NOT EXISTS user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        status VARCHAR(255),
        creation_date TIMESTAMP,
        modification_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deletion_date TIMESTAMP
    )  ENGINE=INNODB;
"""
reservation_creation = """
    CREATE TABLE IF NOT EXISTS reservation (
        id INT AUTO_INCREMENT PRIMARY KEY,
        resource_id INTEGER,
        user_id INTEGER,
        start_time TIME,
        num_pax INTEGER,
        status VARCHAR(255),
        creation_date TIMESTAMP,
        modification_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deletion_date TIMESTAMP,
        FOREIGN KEY(resource_id) REFERENCES resource(id),
        FOREIGN KEY(user_id) REFERENCES user(id)
    )  ENGINE=INNODB;
"""

conn.execute(timetable_creation)
conn.execute(resource_creation)
conn.execute(user_creation)
conn.execute(reservation_creation)

#for db in databases.fetchall():
    #print(db)