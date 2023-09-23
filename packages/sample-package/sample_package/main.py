import psycopg2


def connect_db(db_url: str):
    conn = psycopg2.connect(db_url)
    return conn


def query_hello_world() -> list:
    conn = connect_db(
        "dbname=postgres user=postgres password=postgres host=localhost port=5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT 'Hello, World!'")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result


def main() -> None:
    print(query_hello_world())
