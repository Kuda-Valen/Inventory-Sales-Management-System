import sqlite3
from models.product import Product

def add_product():
    print("\n-- Add Product --\n")
    name = input("Enter Product Name: ").strip()
    cost_price = ("Enter Product Cost Price Per Item: ").strip()
    selling_price = input("Enter Selling Price Per Item: ").strip()
    stock = int(input("Enter Number of Items: "))
    supplier_name = input("Enter Supplier Name: ").strip()

    product = Product(name, cost_price, selling_price, stock, supplier_name)
    save_to_sql (product)

def save_to_sql(product: Product):
    conn = sqlite3.connect("database/database.db")
    cursor = conn.cursor()

    with conn:
        cursor.execute(
            
            """
            INSERT INTO products (name, cost_price, selling_price, stock, supplier_name) VALUES (?, ?, ?, ?, ?);
        """,
        ( product.name, product.cost_price, product.selling_price, product.stock, product.supplier_name)
        )

        

