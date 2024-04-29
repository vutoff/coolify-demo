import os

from flask import Flask
import psycopg2

app = Flask(__name__)


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_NAME = os.getenv("DB_NAME", "postgres")


@app.route("/")
def hello_world():
    try:
        conn = psycopg2.connect(
            f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST}"
        )
    except ConnectionError as e:
        return "Connection Error to Database: {}".format(e)

    cur = conn.cursor()
    cur.execute("SELECT * FROM postgres")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return str(rows)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
