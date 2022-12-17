from flask import Flask, render_template, request
from mysql2python import python_connect_mysql
from config_from_yaml import config_from_yaml_file

config = config_from_yaml_file("config.yaml")
table_names = python_connect_mysql(config, state='show_tables')

app = Flask(__name__)
@app.route('/')
def student():
   return render_template('student.html', table_names=table_names)


@app.route('/table',methods = ['POST', 'GET'])
def table():
   if request.method == 'POST':
      result = request.form
      table_name = result['table_name']
      col_names = python_connect_mysql(config, state='show_col', table_name=table_name)
      data = python_connect_mysql(config, table_name=table_name)
      return render_template("table.html", col_names=col_names, data=data)


if __name__ == '__main__':
   app.run(debug = True)