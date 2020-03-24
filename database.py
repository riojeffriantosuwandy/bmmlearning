import psycopg2
import datetime
import calendar


def databaseconnect():
    return psycopg2.connect(database='bmmlearning', user='RexWar', password='Cibre70', host='localhost')

def insert_transaction(): # all rows from "" table
    databaseconnection = databaseconnect()
    print("Database connected.")
    cursor = databaseconnection.cursor()
    print("cursor created")
    date_input = input("enter transaction date: ")
    values_input = input("transaction details : ")
    amount_input = input("amount: ")
    is_db_input = input("db if Debit transaction, kr if Kredit Transaction: ")
    if is_db_input == 'db':
        is_db = True
    elif is_db_input == 'kr':
        is_db = False
    else:
        print("Please only input Debit or Kredit.")
    cursor.execute("INSERT INTO transaction (transaction_date, transaction_detail, amount, is_db) VALUES (%s, %s, %s, %s)", (date_input, values_input, amount_input, is_db))
    databaseconnection.commit()
    print("Values successfully inputted")
    databaseconnection.close()

def select_transaction(dbkr="db"):
    databaseconnection = databaseconnect()
    print("Database connected.")
    cursor = databaseconnection.cursor()
    print("cursor created")
    if dbkr == 'db':
        is_db_or_kr = True
    elif dbkr == 'kr':
        is_db_or_kr = False
    else:
        raise ValueError("Please input db or kr parameter only.")
    year_input = int(input("Enter Year: "))
    month_input = int(input("Enter Month: "))
    date_time1 = datetime.date(year_input, month_input, 1)
    date_time2 = datetime.date(year_input, month_input, calendar.monthrange(year_input, month_input)[1])
    cursor.execute("SELECT * FROM transaction WHERE (is_db = {}) AND (date_input BETWEEN '{}' AND '{}')".format(is_db_or_kr, date_time1, date_time2))
    rows = cursor.fetchall()
    print(rows)
    databaseconnection.close()

def insert_unit(field_code):
    databaseconnection = databaseconnect()
    print("Database connected.")
    cursor = databaseconnection.cursor()
    print("cursor created")
    cursor.execute("INSERT INTO unit (field_code) VALUES (%s)", (field_code,))
    databaseconnection.commit()
    print("Values successfully inputted")
    databaseconnection.close()

def insert_customer(name):
    databaseconnection = databaseconnect()
    print("Database connected.")
    cursor = databaseconnection.cursor()
    print("cursor created")
    cursor.execute("INSERT INTO customer (name) VALUES (%s)", (name,))
    databaseconnection.commit()
    print("Values successfully inputted")
    databaseconnection.close()

def insert_supplier(name, representative):
    databaseconnection = databaseconnect()
    print("Database connected.")
    cursor = databaseconnection.cursor()
    print("cursor created")
    cursor.execute("INSERT INTO supplier (name, supplier_representative) VALUES (%s, %s)", (name, representative))
    databaseconnection.commit()
    print("Values successfully inputted")
    databaseconnection.close()

def query(query_parameter):
    databaseconnection = databaseconnect()
    print("Database connected.")
    cursor = databaseconnection.cursor()
    print("cursor created")
    cursor.execute("SELECT * FROM {}".format(query_parameter))
    rows = cursor.fetchall()
    print(rows)
    databaseconnection.close()