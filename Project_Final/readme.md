# CSCI-GA 2433 Final Project

## Description:
In this part, we will create an interactive system to connect to MySQL through Python to interact with the database.

The interactive system includes showing tables, selecting tables, and updating (inserting, deleting, and updating) the data. In addition, this interactive system also consists of the code from project3(Machine Learning part).

We can use the machine learning part to predict medical insurance prices and insert the price into the table. We use Python (in the Project3's Jupyter notebook) to calculate the weight of the [Medical Insurance Premium Prediction](https://www.kaggle.com/datasets/tejashvi14/medical-insurance-premium-prediction) data and export the weights into Python to predict the price.

## Packages
In this project, we use packages below.
```
pip install PyYAML
pip install easydict
pip install Flask
pip install mysql-connector-python
```

## Preparing
1. Please go to **setup.md** to connect the MySQL Server
2. Run the code to get the client flag for configs
```
cd code
python get_client_flags.py
```
3. Copy the result to **/code/config.yaml**; also motify the config to connect the database server.

## Launch
```
cd code
python web.py
```

## Files
1. **setup.md**: The tutorial on connecting to the Microsoft Azure server
2. **code**: Contains all the code of this project.
    
    1) **config.yaml**: Contains the config connected to the server.
    2) **get_client_flags.py**: Get the client flag, which is needed when modifying the yaml file.
    3) **config_from_yaml.py**: Convert the yaml file into a dictionary.
    4) **mysql2python.py**: Contains all the code connecting Python and MySQL (show tables, get columns, get data, insert, delete and update)
    5) **web.py**: The main file of this project contains Python flask code.
    6) **templates**: Contains all html files.
    7) **xgb_reg.pkl:** The weight of Machine Learning model from project 3.


## Progress
- [x] Show tables names, select table, and submit button

- [x] Show table (table head, and data)

- [x] Back to Content

- [x] Insert data

- [x] Delete data

- [x] Update data

- [x] Machine learning part insert

## Reference
1. [Microsoft Azur, Python connect to MySQL](https://learn.microsoft.com/en-us/azure/mysql/single-server/connect-python)
2. [Flask_templates](https://www.tutorialspoint.com/flask/flask_templates.htm)
