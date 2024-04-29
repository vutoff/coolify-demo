# Write a simple python webapp that listens on port 5000 connects to a database and returns the results of a query.

from flask import Flask
import psycopg2

app = Flask(__name__)


@app.route("/")
def hello_world():
    conn = psycopg2.connect(
        "dbname=postgres user=postgres password=postgres host=postgres"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM test")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return str(rows)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
