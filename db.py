import sqlite3 as sq
with sq.connect("baza.db") as con:
    cur = con.cursor()
    
#jadvallarni yaratish
cur.execute("""CREATE TABLE IF NOT EXISTS xaridor
           id INTEGER PRIMARY KEY,
           user_id INTEGER,
           product_name TEXT,
           price INTEGER
            """)

#jadvallarga malumot qo'shish
#1-usul: INSERT OR IGNORE
cur.excute("""INSERT OR IGNORE INTO users (id, first_name, last_name =, age)
           VALUES (1, 'Xakimbayev', 'Rasulbek', 16)""")

cur.execute("""INSERT OR IGNORE INTO xaridlar (id, user_id, product_name, price)
            VALUES (2, 'Abdullayev', 'Farhod', 16)""")

cur.execute("""INSERT OR IGNORE INTO xaridlar (id, user_id, product_name, price)
            VALUES (3, 'Hayotbekov', 'Durbek', 16)""")

cur.execute("""INSERT OR IGNORE INTO xaridlar (id, user_id, product_name, price)
            VALUES (4, 'Lazoyev', 'Behzod', 16)""")

cur.execute("""INSERT OR IGNORE INTO xaridlar (id, user_id, product_name, price)
            VALUES (5, 'Qodirova', 'Lobarxon', 16)""")


cur.execute("""INSERT OR IGNORE INTO xaridlar (id, user_id, product_name, price)
            VALUES (6, 'Rajabov', 'Navro'z', 16)""")   

cur.execute("""INSERT OR IGNORE INTO xaridlar (id, user_id, product_name, price)
            VALUES (7, 'Bahtiyorov', 'Shohjaxon', 16)""") 

con.commit()