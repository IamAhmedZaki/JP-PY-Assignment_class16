import pymysql
from datetime import datetime
import json

def mysqlconnect():
    
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password="ahmedzaki", # empty password
        db='ecommerce_db',
        cursorclass=pymysql.cursors.DictCursor,
    )
    print("db connected")
    return conn
    
db_conn=mysqlconnect()

def add_categories(db_conn,data):
    mycursor=db_conn.cursor()
    category_id=data['cid']
    category_name=data['name']
    
    mycursor.execute(
        """
        INSERT INTO categories (category_id, category_name)
        VALUES (%s, %s)
        """, 
        (category_id, category_name)
    )
    
    db_conn.commit() 

def add_product(db_conn,product_data):
    mycursor=db_conn.cursor()
    product_id=product_data['product_id']
    product_name=product_data['product_name']
    product__cat_i=product_data['category_id']#can this be automated??
    product_price=product_data['price']
    product_stock_quantity=product_data['stock_quantity']
    current_datetime=datetime.now()
    mycursor.execute(
        """
        INSERT INTO products (product_id, product_name, price, stock_quantity, category_id, created_at)
        VALUES (%s, %s, %s,%s,%s,%s)
        """, 
        (product_id, product_name,product_price,product_stock_quantity, product__cat_i, current_datetime)
    )
    
    db_conn.commit() 


def main():
    while True:
        print("""
        _______________________________________________________
        What action do you want to perform:
        1. Add categories
        2. Add products
        3. Add Orders
        4. Add Products
        5. Add Payments
        6. View Sales Metrics
        7. View Order Metrics
        8. View Payment Metrics
        9. View Product Metrics
        10. View Geographical Metrics
        0. Exit 
        _______________________________________________________
        """)
        choice = input("Enter your choice: ")

        if choice == '1':
          data = {}
          data['cid'] = input("enter category id:\n")
          data['name'] = input("enter category name:\n")
          add_categories(db_conn,data)
        elif choice == '2':
          product_data = {}
          product_data['product_id'] = input("enter product id:\n")
          product_data['product_name'] = input("enter product name:\n")
          product_data['price']=input("enter product price:\n")
          product_data['stock_quantity']=input("enter product stock quantity:\n")
          product_data['category_id']=input("enter category id:\n")
          add_product(db_conn,product_data)
        

        elif choice == '0':
            break
        else:
            print("Invalid choice! Please try again.")

# # Run the main function
if __name__ == "__main__":
    main()
