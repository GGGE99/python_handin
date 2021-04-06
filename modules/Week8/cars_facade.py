from sqlalchemy import create_engine
import pandas as pd
import os

import mysql.connector as mysql

con_str = "mysql+mysqlconnector://root:root@db/db"
engine = create_engine(con_str)

class Cars_facade:
    def __init__(self, filename):
        print(os.getcwd() + filename)
        self.cnx = mysql.connect(host = "db", user = "root", passwd = "root", db = "db")
        self.data = pd.read_csv(filename, sep=';', skiprows=[1])
        self._index = None

    def replace(self):
        self.data = self.data.applymap(str)
        self.data.to_sql('cars',con=engine, if_exists='replace', index = True, index_label = 'id')
        return self.data
    
    def add_car( self, 
        car, 
        mpg, 
        cylinders, 
        displacement,
        horsepower,
        weight,
        acceleration,
        model,
        origin):
        id = self._next_index()
        self.cnx.connect()
        cur = self.cnx.cursor()
        query = "INSERT INTO cars values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (id, car, mpg, cylinders, displacement, horsepower, weight, acceleration, model, origin))
        self.cnx.commit()
        cur.execute("SELECT * FROM cars where Car= %s AND MPG=%s AND Cylinders=%s", (car, mpg, cylinders))
        res = cur.fetchall()
        self.cnx.close()

        print(self._next_index())

        cur.close()

        return res 
        # {'Car': car, 'MPG': mpg, 'Cylinders': cylinders, 'Displacement': displacement, 'Horsepower': horsepower, 'Weight': weight, 'Acceleration': acceleration, 'Model': model, 'Origin': origin}

    def get_all_cars(self):
        self.cnx.connect()
        cur = self.cnx.cursor()
        cur.execute('SELECT * FROM cars')
        result = cur.fetchall()
        self.cnx.close()

        return result
    
    def get_car(self, id ):
        self.cnx.connect()
        cur = self.cnx.cursor()
        cur.execute('SELECT * from cars WHERE id=%s', (id, ))
        res = cur.fetchall()
        self.cnx.close()
        return res

    def delete_car(self, id ):
        res = self.get_car(id)
        self.cnx.connect()
        cur = self.cnx.cursor()
        cur.execute('DELETE from cars WHERE id=%s', (id, ))
        self.cnx.commit()
        self.cnx.close()
        return res

    def _next_index(self):
        if self._index:
            self._index += 1
        else:
            self.cnx.connect()
            cur = self.cnx.cursor()
            cur.execute('SELECT MAX(id) from cars')
            self._index = cur.fetchone()[0] + 1
            self.cnx.close()
        return self._index



def get_facade(filename):
    return Cars_facade(filename)