#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#getting data for all companies of a particular date
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

# API endpoint to get stock data for all companies on a particular day
@app.route('/stocks/<string:date>', methods=['GET'])
def get_all_stock_data(date):
    # Connect to the SQLite database of all companies
    conn1 = sqlite3.connect('apple.db')
    c1 = conn.cursor()
    
    conn2 = sqlite3.connect('amazon.db')
    c2 = conn.cursor()
    
    conn3 = sqlite3.connect('disney.db')
    c3 = conn.cursor()
    
    conn4 = sqlite3.connect('microsoft.db')
    c4 = conn.cursor()
    
    conn5 = sqlite3.connect('tesla.db')
    c5 = conn.cursor()

    # Execute a SELECT query to retrieve the stock data for all companies on the specified date
    c1.execute("SELECT * FROM apple WHERE date=?", (date,))
    stock_data = c1.fetchall()
    
    c2.execute("SELECT * FROM amazon WHERE date=?", (date,))
    stock_data = c2.fetchall()
    
    c3.execute("SELECT * FROM disney WHERE date=?", (date,))
    stock_data = c1.fetchall()
    
    c4.execute("SELECT * FROM microsoft WHERE date=?", (date,))
    stock_data = c4.fetchall()
    
    c5.execute("SELECT * FROM tesla WHERE date=?", (date,))
    stock_data = c5.fetchall()

    if stock_data:
        # Create a dictionary to store the stock data for all companies
        all_stock_data = {}
        
        # Loop through the results of the SELECT query and add the stock data to the dictionary
        for row in stock_data:
            company = row[0]
            stock_data = {
                'open':               row[1],
                'high':               row[2],
                'low':                row[3],
                'close' :             row[4],
                'adjusted close':     row[5],
                'volume':             row[6],
                'dividend amount' :   row[7],
                'split coefficient' : row[8]
            }
            all_stock_data[company] = stock_data

        # Return the stock data in a JSON format
        return jsonify(all_stock_data)
    else:
        # Return an error message in a JSON format
        return jsonify({'error': 'Unable to retrieve stock data'})
if __name__ =='__main__':
    app.run()


# In[ ]:


#data for a particular company of a particular date
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/stocks/<company_name>/<date>', methods=['GET'])
def get_stock_data(company_name, date):
    # Establish connection to the SQLite database
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()
    
    # Execute a query to retrieve stock data for the specified company and date
    c.execute("SELECT * FROM stocks WHERE company = ? AND date = ?", (company_name, date))
    data = c.fetchall()
    
    # Convert the retrieved data to a JSON object and return it
    if data:
        return jsonify(data)
    else:
        return jsonify({'message': 'No stock data found for the specified company and date.'}), 404

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:


#data for a particular company 
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/stocks/<company_name>', methods=['GET'])
def get_stock_data(company_name):
    # Establish connection to the SQLite database
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()
    
    # Execute a query to retrieve stock data for the specified company 
    c.execute("SELECT * FROM stocks WHERE company = ? ", (company_name))
    data = c.fetchall()
    
    # Convert the retrieved data to a JSON object and return it
    if data:
        return jsonify(data)
    else:
        return jsonify({'message': 'No stock data found for the specified company '}), 404

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:


#adding data by using POST API to update stock data for a company by date
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/stocks/update', methods=['POST'])
def update_stock_data():
    # Get the company name and date from the request body
    request_data     = request.get_json()
    company_name     = request_data['company_name']
    date             = request_data['date'],
    open             = request_data['open'],
    high             = request_data['high'],
    low              = request_dataargs['low'],
    close            = request_data['close'],
    adjusted close   = request_data['adjusted close'],
    volume           = request_data['volume'],
    dividend amount  = request_data['dividend amount'],
    split coefficient= request_data['split coefficient']

    # Connect to the SQLite database
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()

    # Update the stock data for the specified company and date
    c.execute("UPDATE stocks SET open=?, high=?, low=?, close=?, adjusted close=?,volume= ?,dividend amount=?, split coefficient=? WHERE company_name=? AND date=?", 
              (open, high, low, close, adjusted close, volume, dividend amount, split coefficient, company_name, date))
    conn.commit()

    # Close the database connection
    conn.close()

    # Return a success message
    return jsonify({'message': 'Stock data updated successfully'})

if __name__ == '__main__':
    app.run(debug=True)

