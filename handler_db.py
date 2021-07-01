import os
import sqlite3 as lite
from typing import List

import requests
from peewee import Model, SqliteDatabase, TextField

# db
db = SqliteDatabase("posts.db")


# model
class User(Model):
    first_name = TextField()
    last_name = TextField()
    gender = TextField()
    phone = TextField()
    email = TextField()
    state = TextField()
    img = TextField()

    class Meta:
        database = db


def load_rows(rows: int):
    """
    loading db data when starting app
    """
    data = requests.get(f"https://randomuser.me/api/?results={rows}").json()
    users = []

    for user in data["results"]:
        users.append(
            {
                "first_name": user["name"]["first"],
                "last_name": user["name"]["last"],
                "gender": user["gender"],
                "phone": user["phone"],
                "email": user["email"],
                "state": user["location"]["country"],
                "img": user["picture"]["large"],
            }
        )

    User.create_table()

    with db.atomic():
        query = User.insert_many(users)
        query.execute()


def show_rows() -> List[dict]:
    """
    sending data to client from db
    """
    db.connect()
    users_selected = User.select().order_by(User.id.desc()).dicts().execute()
    row = [user for user in users_selected]
    db.close()
    return row


def del_rows():
    """
    delete old db
    """
    if db:
        os.remove("posts.db")


def sql_query(query: str, db="posts.db"):
    conn = lite.connect(db)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    results = cursor.fetchall()
    conn.close()
    return results


"""
Сортировка значений по нескольким колонкам
SELECT * FROM mytable ORDER BY column1 ASC, column2 DESC, column3 ASC
"""

print(
    sql_query(
        """
    SELECT first_name,COUNT(first_name)
    FROM user
    GROUP BY first_name
    """
    )
)
