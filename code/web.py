from flask import Flask, render_template, request, redirect, url_for
from mysql2python import python_connect_mysql, operation_to_sql
from config_from_yaml import config_from_yaml_file

config = config_from_yaml_file("config.yaml")
table_names = python_connect_mysql(config, state='show_tables')

app = Flask(__name__)
@app.route('/')
def p1():
   # redirect to initial_page
   return redirect(url_for('initial_page'))

@app.route('/initial_page')
def initial_page():
   # Show tables
   return render_template('p1.html', table_names=table_names)

@app.route('/table', methods=['POST', 'GET'])
def table():
   # Show a table of data from database
   if request.method == 'POST':
      result = request.form
      table_name = result['table_name']
      col_names = python_connect_mysql(config, state='show_col', table_name=table_name)
      data = python_connect_mysql(config, table_name=table_name)
      return render_template("table.html", table_name=table_name, col_names=col_names, data=data)
   
@app.route('/operation', methods=['POST', 'GET'])
def operation():
   if request.method == 'GET':
      # Go back to initial_page
      return redirect(url_for('initial_page'))
   else:
      # Go to the operation page
      result = request.form
      table_name = result['table_name']
      col_names = python_connect_mysql(config, state='show_col', table_name=table_name)
      data = python_connect_mysql(config, table_name=table_name)
      operation_name = result['operation']

      if operation_name == 'insert':
         return render_template("insert.html", table_name=table_name, col_names=col_names, data=data, operation_name=operation_name)
      elif operation_name == 'delete':
         return render_template("delete.html", table_name=table_name, col_names=col_names, data=data, operation_name=operation_name)
      elif operation_name == 'update':
         return render_template("update.html", table_name=table_name, col_names=col_names, data=data, operation_name=operation_name)

@app.route('/success', methods=['POST', 'GET'])
def operation_toSQL():
   if request.method == 'POST':
      # Do insert, delete and update
      result = request.form
      table_name = result['table_name']
      col_names = python_connect_mysql(config, state='show_col', table_name=table_name)
      data = python_connect_mysql(config, table_name=table_name)

      query = operation_to_sql(config, col_names=col_names, input_value=result, data=data, operation=result["operation_name"])
      return render_template("operat_info.html", result=result, query=query)

@app.route('/success/1', methods=['POST', 'GET'])
def succ():
   # Show the infomation of operations
   if request.method == 'GET':
      # Go back to initial_page
      return redirect(url_for('initial_page'))

@app.route('/survey', methods=['POST', 'GET'])
def survey():
   # Go to the survey
   if request.method == 'GET':
      return render_template("survey.html")

@app.route('/survey/1', methods=['POST', 'GET'])
def survey_price():
   # Calculate price
   if request.method == 'POST':
      result = request.form
      # Here add python function to calculate the price.
      return render_template("price.html", result=result)

if __name__ == '__main__':
   app.run(debug = True)