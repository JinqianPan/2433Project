import mysql.connector
from mysql.connector import errorcode
from config_from_yaml import config_from_yaml_file

def python_connect_mysql(config, state, table_name="contractpremium"):
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
            print(table_names)
        else:
            # Read data
            query = "SELECT * FROM " + table_name + ";"
            cursor.execute(query)
            rows = cursor.fetchall()
            print("Read",cursor.rowcount,"row(s) of data.")
            # print(cursor.description)

            # Print all rows
            for row in rows:
                print("Data row = (%s, %s, %s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])))

        # Cleanup
        conn.commit()
        cursor.close()
        conn.close()

if __name__ == "__main__":
    config = config_from_yaml_file("config.yaml")
    python_connect_mysql(config, state='show_tables')