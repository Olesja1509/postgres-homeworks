"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2

with psycopg2.connect(host="localhost", database="north", user="postgres", password="max1313") as conn:
    with conn.cursor() as cur:
        #  Добавление данных в таблицу employees
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s)",
                    (1, 'Nancy', 'Davolio', 'Sales Representative', '1948-12-08'))
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s)",
                    (2, 'Andrew', 'Fuller', 'Vice President, Sales', '1952-02-19'))
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s)",
                    (3, 'Janet', 'Leverling', 'Sales Representative', '1963-08-30'))
        cur.execute("SELECT * FROM employees")

        #  Добавление данных в таблицу customers
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                    ('ALFKI', 'Alfreds Futterkiste', 'Maria Anders'))
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                    ('ANATR', 'Ana Trujillo Emparedados y helados', 'Ana Trujillo'))
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                    ('ANTON', 'Antonio Moreno Taquería', 'Antonio Moreno'))
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                    ('AROUT', 'Around the Horn', 'Thomas Hardy'))
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                    ('BERGS', 'Berglunds snabbköp', 'Christina Berglund'))
        cur.execute("SELECT * FROM customers")

        #  Добавление данных в таблицу customers
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                    (10248, 'ALFKI', 1, '1996-07-04', 'Reims'))
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                    (10249, 'ANATR', 2, '1996-07-05', 'Münster'))
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                    (10250, 'ANTON', 3, '1996-07-08', 'Rio de Janeiro'))
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                    (10251, 'AROUT', 1, '1996-07-08', 'Lyon'))
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                    (10252, 'BERGS', 2, '1996-07-09', 'Charleroi'))
        cur.execute("SELECT * FROM orders")

        conn.commit()
