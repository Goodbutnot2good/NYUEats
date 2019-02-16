#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect, flash, os
import pymysql.cursors
import time
import datetime
import hashlib

#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL
conn = pymysql.connect(host='localhost',
                       port = 8889,
                       user='root',
                       password='root',
                       db='NYUeats',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

#Method to run an sql query without commit.
#Input: query, data to be used in query, and amount, which is either "one" or "all" determines fetchone() or fetchall(). 
#Output: returns data from query
def run_sql(query, data, amount):
    cursor = conn.cursor()
    cursor.execute(query, data)
    data = None
    if amount == "one":
        data = cursor.fetchone()
    elif amount == "all":
        data = cursor.fetchall()
    cursor.close()
    return data
#Method to run an sql query with commit. 
#Input: query, data to be used in query.
#output: none.
def run_sql_commit(query, data):
    cursor = conn.cursor()
    cursor.execute(query, data)
    conn.commit()
    cursor.close()

app.secret_key = os.urandom(24)


#homepage
@app.route('/')
def homepage():
	#a session variable will act as a cart, a python list holding all orders
	session['orders'] = []		
	return render_template('homepage.html')

#selection
@app.route('/selection')
def selection():
	return render_template('selection.html')

#menu
@app.route('/menu')
def menu():
	return render_template('menu.html')

@app.route('/detail')
def detail():
	return render_template('detail.html')

@app.route('/checkout')
def checkout():
	return render_template('checkout.html')

@app.route('/pickuptime')
def pickuptime():
	return render_template('pickuptime.html')

#test connection to MySQL database
@app.route('/db')
def connect():
	cur.execute('''SHOW TABLES''')
	result = cur.fetchall()
	return str(result)

#test creating a order with a nyu id
#@app.route('/create/order')
#def order():
	#get nyu id from html form and create table with the same name
	#netid = 
	#cur.execute('''CREATE TABLE %s (name VARCHAR(20) NOT NULL, time TIME)''', netid)
	#get pickup time from html form and insert to table
	#pickuptime = time.strptime(       , '%Y-%m-%d %H:%M:%S')
	#pickuptime = time.strftime('%Y-%m-%d %H:%M:%S', pickuptime)
	#cur.execute('''INSERT INTO %s (time) VALUES (%s)''', (netid, pickuptime))
	#insert orders into table
	#for item in session['orders']:
		#cur.execute('''INSERT INTO %s (name) VALUES (%s)''', (netid, item))
	#clear the cart
	#session.pop('orders')
	#commit at the very end


if __name__ == "__main__":
	app.run(debug=True)
