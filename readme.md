# CSCI-GA 2433 Final Project

## Description:
In this part, we will create an interactive system to connect to MySQL through Python to interact with the database.

The interactive system includes show tables, select tables, update(insert, delete, and update) the data. 
In addiction, this interactive system also include the code from project3(Machine Learning part). 

We expect we could use the machine learning part to predict medical insurance price, and insert the price into the table.
We use python (in the jupyter notebook) to calculate the weight of the [Medical Insurance Premium Prediction](https://www.kaggle.com/datasets/tejashvi14/medical-insurance-premium-prediction) data, and export the weights into Python to predict the price.

## Packages
In this project, we use packages below.
```
pip install PyYAML
pip install easydict
pip install Flask
pip install mysql-connector-python
```

## Preparing
1. Please go to setup.md to connect the MySQL Server
2. Run the code to get the client flag for configs
```
cd code
python get_client_flags.py
```
3. Copy the result to /code/config.yaml; also motify the config to connect the database server.

## Progress
- [x] Show tables names, select table, and submit button

- [x] Show table (table head, and data)

- [x] Back to Content

- [x] Insert data

- [x] Delete data

- [ ] Update data

- [ ] Machine learning part insert

## Reference
1. [Microsoft Azur, Python connect to MySQL](https://learn.microsoft.com/en-us/azure/mysql/single-server/connect-python)
2. [Flask_templates](https://www.tutorialspoint.com/flask/flask_templates.htm)
