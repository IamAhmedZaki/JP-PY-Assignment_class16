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

def add_customerr(db_conn,customer_data):
    mycursor=db_conn.cursor()
    customer_id=customer_data['user_id']
    customer_fname=customer_data['first_name']
    customer_lname=customer_data['last_name']
    customer_email=customer_data['email']#can this be automated??
    customer_password=customer_data['password']
    customer_address=customer_data['address']
    customer_city=customer_data['city']
    customer_state=customer_data['state']
    customer_zipcode=customer_data['zipcode']
    customer_country=customer_data['country']
    customer_phone=customer_data['phone']
    
    
    current_datetime=datetime.now()
    mycursor.execute(
        """
        INSERT INTO users (user_id, first_name,last_name,email,passwords,address,city,state,zip_code,country,phone,created_at)
        VALUES (%s, %s, %s,%s,%s,%s,%s, %s, %s,%s,%s,%s)
        """, 
        (customer_id,customer_fname,customer_lname,customer_email,customer_password,customer_address,customer_city,customer_state,customer_zipcode,customer_country,customer_phone,current_datetime)
    )
    
    db_conn.commit() 


def add_orders(db_conn,order_data):
    mycursor=db_conn.cursor()
    
    orderuser_id=order_data['user_id']
    order_status=order_data['status']
    current_datetime=datetime.now()
    mycursor.execute(
        """
        INSERT INTO orders (user_id,order_date,status)
        VALUES (%s,%s,%s)
        """, 
        (orderuser_id,current_datetime,order_status)
    )
    
    order_id=mycursor.lastrowid
    db_conn.commit()
    return order_id
    


def order_details(db_conn, order_data):    
    try:
        mycursor = db_conn.cursor()
        order_id = order_data['order_id']
        
        orderproduct_id = order_data['orderproduct_id']
        order_quantity = order_data['quantity']
        order_unitprice = order_data['unit_price']

        mycursor.execute(
            """
            INSERT INTO order_details (order_id, product_id, quantity, unit_price)
            VALUES (%s, %s, %s, %s)
            """, 
            (order_id, orderproduct_id, order_quantity, order_unitprice)
        )

        db_conn.commit()

    except pymysql.Error as e:
        print(f"Error adding order details: {e}")


def add_payments(db_conn,payment_data):
    mycursor=db_conn.cursor()
    
    paymentorder_id=payment_data['order id']
    
    current_datetime=datetime.now()
    payment_amount=payment_data['amount']
    payment_status=payment_data['status']
    mycursor.execute(
        """
        INSERT INTO payments (order_id,payment_date,amount,status)
        VALUES (%s,%s,%s,%s)
        """, 
        (paymentorder_id,current_datetime,payment_amount,payment_status)
    )
    
    db_conn.commit()

def total_revenue(db_conn):
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT SUM(amount) AS total_revenue
        FROM payments
        WHERE status = 'Completed'
        AND payment_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH);

             
        
        """
    )
    return mycursor.fetchall()

def revenue_by_product(db_conn):
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT p.product_name, SUM(od.quantity * od.unit_price) AS revenue
        FROM order_details od
        JOIN payments p ON od.product_id = P.product_id
        JOIN orders o ON od.order_id = o.order_id
        JOIN payments py ON o.order_id = py.order_id
        WHERE py.status = 'Completed'
        GROUP BY p.product_name
        ORDER BY revenue DESC;
        
        """
    )
    return mycursor.fetchall()

def top_selling_products(db_conn):
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT P.product_name, SUM(OD.quantity) AS total_units_sold
        FROM order_details OD
        JOIN products P ON OD.product_id = P.product_id
        JOIN orders O ON OD.order_id = O.order_id
        WHERE O.order_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
        GROUP BY P.product_name
        ORDER BY total_units_sold DESC
        LIMIT 5;

        
        """
    )
    return mycursor.fetchall()

def revenue_city(db_conn):
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT U.city, SUM(PY.amount) AS total_revenue
        FROM users U
        JOIN orders O ON U.user_id = O.user_id
        JOIN payments PY ON O.order_id = PY.order_id
        WHERE PY.status = 'Completed'
        GROUP BY U.city
        ORDER BY total_revenue DESC;

        """
    )
    return mycursor.fetchall()

def total_orders(db_conn):
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT COUNT(*) AS total_orders
        FROM orders
        WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH);

        """
    )
    return mycursor.fetchall()

def pending_orders(db_conn):
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT COUNT(*) AS pending_orders
        FROM orders
        WHERE status = 'Pending';

        """
    )
    return mycursor.fetchall()

def cancelled_orders(db_conn):
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT COUNT(*) AS cancelled_orders
        FROM orders
        WHERE status = 'Cancelled';

        """
    )
    return mycursor.fetchall()


def successful_orders(db_conn):
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT COUNT(*) AS successful_orders
        FROM orders
        WHERE status IN ('Shipped', 'Delivered');

        """
    )
    return mycursor.fetchall()

def pending_payments(db_conn):
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT SUM(amount) AS pending_payments
        FROM payments
        WHERE status = 'Pending';


        """
    )
    return mycursor.fetchall()

def successful_payments(db_conn):
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT SUM(amount) AS successful_payments
        FROM Payments
        WHERE status = 'Completed'
        AND payment_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH);

        """
    )
    return mycursor.fetchall()

def inventory_levels(db_conn):
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT product_name, stock_quantity
        FROM products
        ORDER BY stock_quantity ASC;

        """
    )
    return mycursor.fetchall()

def out_of_stock_products(db_conn):
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT product_name
        FROM products
        WHERE stock_quantity = 0;

        """
    )
    return mycursor.fetchall()

def top_cities_by_sales(db_conn):
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT U.city, COUNT(O.order_id) AS total_orders
        FROM users U
        JOIN orders O ON U.user_id = O.user_id
        GROUP BY U.city
        ORDER BY total_orders DESC
        LIMIT 5;

        """
    )
    return mycursor.fetchall()

def top_countries_by_sales(db_conn):
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT U.country, SUM(PY.amount) AS total_revenue
        FROM users U
        JOIN orders O ON U.user_id = O.user_id
        JOIN payments PY ON O.order_id = PY.order_id
        WHERE PY.status = 'Completed'
        GROUP BY U.country
        ORDER BY total_revenue DESC;

        """
    )
    return mycursor.fetchall()







def main():
    while True:
        print("""
        _______________________________________________________
        What action do you want to perform:
        1. Add categories
        2. Add products
        3. Add customer
        4. Add order
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
        elif choice=='3':
            
            customer_data={}
            customer_data['user_id']= input("enter user id :\n")
            customer_data['first_name']= input("enter first name :\n")
            customer_data['last_name']= input("enter last name :\n")
            customer_data['email']= input("enter eamil:\n")
            customer_data['password']= input("enter password:\n")
            customer_data['address']= input("enter  address:\n")
            customer_data['city']= input("enter  city:\n")
            customer_data['state']= input("enter state:\n")
            customer_data['zipcode']= input("enter zipcode:\n")
            customer_data['country']= input("enter  country:\n")
            customer_data['phone']= input("enter phone:\n")
            add_customerr(db_conn,customer_data)
        elif choice=='4':
            order_data={}
            
            order_data['user_id']= input("enter user id:\n")
            order_data['status']= input("enter status:\n")
            
            order_data['orderproduct_id']= input("enter product id:\n")
            order_data['quantity']= input("enter quantity:\n")
            order_data['unit_price']= input("enter unit price:\n")
            order_id=add_orders(db_conn,order_data)
            if order_id:
                order_data['order_id']=order_id
                order_details(db_conn,order_data)
        elif choice=='5':
             payment_data={}
             
             payment_data['order id']= input("enter order id:\n")
             payment_data['amount']= input("enter product's unit amount:\n")
             payment_data['status']= input("enter status:\n")
             add_payments(db_conn,payment_data)
        elif choice == '6':
            print("\n Total Revenue this Month")
            tot_rev=total_revenue(db_conn)
            print("\n",json.dumps(tot_rev,default=str,indent=4))
            
            # print("\n Revenue by Product")
            # rev_prod=revenue_by_product(db_conn)
            # print("\n",json.dumps(rev_prod,default=str,indent=4))
        
            print("\n Top Selling Product this Month")
            tot_sell_prod=top_selling_products(db_conn)
            print("\n",json.dumps(tot_sell_prod,default=str,indent=4))
            
            print("\n Revenue by City")
            rev_cit=revenue_city(db_conn)
            print("\n",json.dumps(rev_cit,default=str,indent=4))
        
        
        
        elif choice == '7':
            print("\n Total orders this Month")
            tot_ord=total_orders(db_conn)
            print("\n",json.dumps(tot_ord,default=str,indent=4))
            
            print("\n Pending Orders")
            pen_ord=pending_orders(db_conn)
            print("\n",json.dumps(pen_ord,default=str,indent=4))
            
            print("\n Cancelled Orders")
            canc_ord=cancelled_orders(db_conn)
            print("\n",json.dumps(canc_ord,default=str,indent=4))
        
            print("\n Successful Orders")
            succ_ord=successful_orders(db_conn)
            print("\n",json.dumps(succ_ord,default=str,indent=4))
        

        
        
        elif choice == '8':
            print("\n Pending Payments")
            pen_pay=pending_payments(db_conn)
            print("\n",json.dumps(pen_pay,default=str,indent=4))
        
            print("\n Pending Payments")
            succ_pay=successful_payments(db_conn)
            print("\n",json.dumps(succ_pay,default=str,indent=4))
        
        
        elif choice == '9':
            print("\n Inventory Levels")
            inv_lev=inventory_levels(db_conn)
            print("\n",json.dumps(inv_lev,default=str,indent=4))
        
            print("\n Out of Stock Products")
            out_prod=out_of_stock_products(db_conn)
            print("\n",json.dumps(out_prod,default=str,indent=4))
        
        elif choice == '10':
            print("\n Top Cities By Sales This Month")
            top_city_sal=top_cities_by_sales(db_conn)
            print("\n",json.dumps(top_city_sal,default=str,indent=4))
        
            print("\n Top Cities By Sales This Month")
            top_country_sal=top_countries_by_sales(db_conn)
            print("\n",json.dumps(top_country_sal,default=str,indent=4))
        
        
        elif choice == '0':
            break
        else:
            print("Invalid choice! Please try again.")

# # Run the main function
if __name__ == "__main__":
    main()




