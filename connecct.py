
# -*- coding: utf-8 -*-
"""
Spyder Editor

Created on 20 07 2021
@author: Chalo
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="contacto"
)

print(mydb)

cursor=mydb.cursor()
sql="INSERT INTO data (name, email, tel, message)VALUES ('andrea','fjsdf','4771712127','te amo')"
cursor.execute(sql) 
mydb.commit()

#%%
import pymysql

class DataBase:
    def __init__(self):
        self.connection=pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='contacto'
            )        
        self.cursor=self.connection.cursor()
        print("Conexion establecida exitosamente")

    
    def ingresos(self,name,email,tel,message):
       sql="INSERT INTO data (name,email,tel,message) VALUES ('{}','{}','{}','{}')".format(name,email,tel,message)
        # try :
       self.cursor.execute(sql)
       self.connection.commit()
        # except Exception as e:
        #     raise

dbs=DataBase()

dbs.ingresos('luz','jhsaga', 21312313,'gfjhashgdfhj')

#%%

import pymysql

class app:
    def __init__(self):
        self.conn=pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='contacto'
            )        
        self.cursor=self.conn.cursor()
        print("Conexion establecida exitosamente")
    
    def insertar (self):
        name=input("ingrese el nombre : \n")
        sql="INSERT INTO data (name) VALUES ('{}')".format(name)
        self.cursor.execute(sql)
        print("Agregado  exitosamente")


aplication=app()
aplication.insertar()       
#%%        
        