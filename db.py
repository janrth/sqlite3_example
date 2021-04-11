import numpy as np
import pandas as pd
import sqlite3 

class database(object):
    '''Load csv, create database with columns and insert values from file. '''
    def __init__(self):
        self = self
        
       
    def training_db(self):
        #Make DB for train data:
        train = pd.read_csv('train.csv')
        conn = sqlite3.connect('train.db') #connect to train database from csv
        conn.execute('DROP TABLE IF EXISTS train')
        c = conn.cursor()

        c.execute('''Create TABLE train(
                    x real,
                    y1 real,
                    y2 real,
                    y3 real,
                    y4
                    )''')
        conn.commit()

        for row in range(0,train.shape[0]):
            col1 = train[train.columns[0]][row]
            col2 = train[train.columns[1]][row]
            col3 = train[train.columns[2]][row]
            col4 = train[train.columns[3]][row]
            col5 = train[train.columns[4]][row]

            c.execute("INSERT INTO train VALUES(?,?,?,?,?)", (col1,col2,col3,col4,col5))
        conn.commit()
        
        
    def ideal_db(self):
        #Make DB for test data:
        ideal = pd.read_csv('ideal.csv')
        conn = sqlite3.connect('ideal.db') #connect to train database from csv
        conn.execute('DROP TABLE IF EXISTS ideal')
        c = conn.cursor()

        c.execute('''CREATE TABLE ideal (x REAL)''')

        #Create all columns in loop
        col_names = ideal.columns
        for column_name in col_names[1:]:
            c.execute('''ALTER TABLE ideal ADD COLUMN ''' + column_name + ''' REAL''')

        #Insert all data in loop    
        col_array = np.array(ideal)

        for element in col_array:
            placeholders = ', '.join(['?'] * ideal.shape[1])
            c.execute('''INSERT INTO ideal VALUES ({})'''.format(placeholders), element)   
        conn.commit()    