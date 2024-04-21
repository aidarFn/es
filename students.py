import sqlite3

with sqlite3.connect('students.db') as conn:
    pult = conn.cursor()
    pult.execute("""CREATE TABLE IF NOT EXISTS students(
    id INTEGER ,
    hobby TEXT NOT NULL,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    birthday INTEGER NOT NULL,
    hw_score INTEGER NOT NULL
    )""")

    pult.execute("""UPDATE students SET firstname = 'genius' WHERE hw_score > 10""")
    pult.execute("""SELECT * FROM students WHERE firstname = 'genius'""")
    for i in pult:
        print(i)

    print()

    pult.execute("""SELECT * FROM students WHERE LENGTH(lastname) > 10""")
    for i in pult:
        print(i)

    print()

    # pult.execute("""DELETE FROM students WHERE id % 2 = 0""")
    pult.execute("""SELECT * FROM students WHERE id % 2 == 1""")
    for i in pult:
        print(i)


