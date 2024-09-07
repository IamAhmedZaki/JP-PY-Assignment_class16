import pymysql
from datetime import datetime
import json

def mysqlconnect():
    # To connect MySQL database
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

# def update_product(db_conn,update_data):
#     mycursor=db_conn.cursor()
#     update_id=update_data['id']
#     update_name=update_data['name']
    
#     current_datetime=datetime.now()
#     mycursor.execute(
#         """
#         update product set name=%s, updated_at=%s
#         where id=%s
#         """, 
#         (update_name, current_datetime,update_id)
#     )
    
#     db_conn.commit() 

# def delete_product(db_conn, delete_data):
#     mycursor = db_conn.cursor()
#     delete_id = delete_data['id']
#     print(f"Attempting to delete product with ID: {delete_id}")  # Debugging step
    
#     mycursor.execute(
#         """
#         DELETE FROM product 
#         WHERE id = %s
#         """, 
#         (delete_id,)
#     )
    
#     db_conn.commit()
#     print(f"Product with ID {delete_id} deleted successfully.")

# def display_categories(db_conn):
#     mycursor=db_conn.cursor()
#     mycursor.execute("SELECT * FROM category")
#     return mycursor.fetchall()

# def display_products(db_conn):   

#     mycursor=db_conn.cursor()
#     mycursor.execute("SELECT * FROM product")
#     return mycursor.fetchall()

# def display_combined(db_conn):
#     mycursor=db_conn.cursor()
#     mycursor.execute("""
#         SELECT 
#             product.id AS product_id,
#             product.name AS product_name,
#             category.name AS category_name,
#             product.created_at AS product_created_at
#         FROM 
#             product
#         INNER JOIN 
#             category
#         ON 
#             product.cat_id = category.id;
#         """
#     )
#     return mycursor.fetchall()


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
        # elif choice == '3':
        #      update_data={}
        #      update_data['id'] = input("enter product id:\n")
        #      update_data['name'] = input("enter product name:\n")
          
        #      update_product(db_conn,update_data)
        # elif choice == '4':
        #     delete_data={}
        #     delete_data['id']=int(input("enter product id:\n"))
        #     delete_product(db_conn, delete_data)
        # elif choice == '5':
        #      get_category=display_categories(db_conn)
        #      print(json.dumps(get_category,default=str,indent=4))
        # elif choice == '6':
        #     get_product=display_products(db_conn)
        #     print(json.dumps(get_product,default=str,indent=4))
        # elif choice == '7':
        #     combined_result=display_combined(db_conn)
        #     print(json.dumps(combined_result,default=str,indent=4))

        elif choice == '0':
            break
        else:
            print("Invalid choice! Please try again.")

# # Run the main function
if __name__ == "__main__":
    main()
