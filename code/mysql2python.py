import mysql.connector
from mysql.connector import errorcode
from config_from_yaml import config_from_yaml_file

def python_connect_mysql(config, state="", table_name="contractpremium"):
    try:
        conn = mysql.connector.connect(**config)
        print("Connection established")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with the user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor = conn.cursor()

        if state == 'show_tables':
            # Get all table names
            cursor.execute("SHOW TABLES;")
            table_names = []
            for i in cursor.fetchall():
                table_names.append(i[0])
            # print(table_names)
            return table_names
        elif state == 'show_col':
            # Get all column names
            query = "SELECT * FROM " + table_name + ";"
            cursor.execute(query)
            rows = cursor.fetchall()
            col_names = []
            for i in cursor.description:
                col_names.append(i[0])
            return col_names
        else:            
            # Read data
            query = "SELECT * FROM " + table_name + ";"
            cursor.execute(query)
            rows = cursor.fetchall()
            data = []
            index_num = 1    
            for row in rows:
                row_data = []
                row_data.append(index_num)
                index_num += 1
                for i in range(len(row)):
                    row_data.append(row[i])
                data.append(row_data)
            # print(data)
            return data

        # Cleanup
        conn.commit()
        cursor.close()
        conn.close()

def operation_to_sql(config, col_names=[], input_value={}, data=[], operation="insert"):
    try:
        conn = mysql.connector.connect(**config)
        print("Connection established")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with the user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor = conn.cursor()

        if operation == "insert":
            try:
                # query = "INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150)
                table_name, value_list = utili(operation, input_value, col_names)
                query = "INSERT INTO " + table_name + " ("
                for i in range(len(col_names)):
                    query = query + col_names[i]
                    if i == len(col_names) - 1:
                        query = query + ")"
                    else:
                        query = query + ", "
                query = query + " VALUES ("
                for i in range(len(value_list)):
                    query = query + "\'" + value_list[i] + "\'"
                    if i == len(value_list) - 1:
                        query = query + ");"
                    else:
                        query = query + ", "
                # print(query)
                cursor.execute(query)
                try:
                    conn.commit()
                    print("Inserted",cursor.rowcount,"row(s) of data.")
                except:
                    print("Fail to insert.")
            except Exception as err:
                print("Insert failed: ", err) 
                conn.rollback()
            return query
        elif operation == "delete":
            try:
                # query = "DELETE FROM inventory WHERE name=%(param1)s;", {'param1':"orange"}
                table_name, row_num = utili(operation, input_value)
                delete_row = data[int(row_num)-1][1:]
                query = "DELETE FROM " + table_name + " WHERE "
                for i in range(len(col_names)):
                    query = query + col_names[i] + " = " + delete_row[i]
                    if i != len(col_names)-1:
                        query = query + " AND "
                    else:
                        query = query + ";"
                cursor.execute(query)
                print("Deleted",cursor.rowcount,"row(s) of data.")
            except Exception as err:
                print("Delete failed: ", err) 
                conn.rollback()
        elif operation == "update":
            try:
                # query = "UPDATE inventory SET quantity = %s WHERE name = %s;", (300, "apple")
                table_name, row_num, value_list = utili(operation, input_value)
                update_row = data[int(row_num)-1][1:]
                query = "UPDATE " + table_name + " SET "
                for i in range(len(col_names)):
                    query = query + col_names[i] + " = " + value_list[i]
                    if i != len(col_names)-1:
                        query = query + " AND "
                query = query + " WHERE "
                for i in range(len(col_names)):
                    query = query + col_names[i] + " = " + update_row[i]
                    if i != len(col_names)-1:
                        query = query + " AND "
                    else:
                        query = query + ";"
                cursor.execute(query)
                print("Updated",cursor.rowcount,"row(s) of data.")
            except Exception as err:
                print("Update failed: ", err) 
                conn.rollback()

        # Cleanup
        cursor.close()
        conn.close()

def utili(operation, input_value, col_names):
    if operation == "insert":
        value_list = []
        dict = {}
        for key, value in input_value.items():
            dict[key] = value
        table_name = dict["table_name"]
        for i in range(len(col_names)):
            value_list.append(dict[col_names[i]])
        return table_name, value_list
    elif operation == "delete": 
        table_name = input_value['table_name']
        row_num = input_value["row"]
        return table_name, row_num
    elif operation == "update":
        value_list = []
        for key, value in input_value:
            if key == "table_name":
                table_name = value
            elif key == "operation_name":
                pass
            elif key == "row":
                row_num = value
            else:
                value_list.append(value)
        return table_name, row_num, value_list


if __name__ == "__main__":
    config = config_from_yaml_file("config.yaml")
    # python_connect_mysql(config, state='show_tables')
    # python_connect_mysql(config, state='show_col')
    # python_connect_mysql(config)