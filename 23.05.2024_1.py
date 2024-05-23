import sqlite3
conn = sqlite3.connect('C:\\Users\\Stud\\Desktop\\eov\\23.05.2024_2.db')
check_same_thread = False
cursor = sqlite3.Cursor(conn)
cursor.execute(
    """
      CREATE TABLE IF NOT EXISTS meals (
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      name VARCHAR(20))
    """)

cursor.execute(
    """
      CREATE TABLE IF NOT EXISTS orders (
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      price INTEGER)
    """)
cursor.execute(
    """
      CREATE TABLE IF NOT EXISTS orders_meal (
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      order_id INTEGER,
      meal_id INTEGER,
      
      FOREIGN KEY (order_id) REFERENCES orders (id)
      ON DELETE CASCADE,
      FOREIGN KEY (meal_id) REFERENCES meals (id)
      ON DELETE CASCADE
    )""")

cursor.execute('INSERT INTO meals (name) VALUES ("греческий салат")')
meal_id = cursor.lastrowid
cursor.execute('INSERT INTO orders (price) VALUES (80)')
order_id = cursor.lastrowid

cursor.execute(f'INSERT INTO orders_meal (order_id, meal_id) VALUES ({order_id}, {meal_id})')
conn.commit()

