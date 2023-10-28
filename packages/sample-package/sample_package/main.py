import psycopg2


def connect_db(db_url: str):
    conn = psycopg2.connect(db_url)
    return conn


def query_hello_world(db_url) -> list:
    conn = connect_db(db_url)
    cur = conn.cursor()
    cur.execute("SELECT 'Hello, World!'")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result


def main() -> None:
    db_url = "dbname=postgres user=postgres password=postgres host=localhost port=5432"
    print(query_hello_world(db_url))
