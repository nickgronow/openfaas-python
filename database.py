import psycopg2
import psycopg2.extras


class Database:
    """Simple way to query and write to a postgres database"""

    def __init__(self, **options):
        self.connection = psycopg2.connect(
            database=options["db"],
            user=options["user"],
            password=options["password"],
            host=options["host"],
            port=options["port"],
        )
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def query(self, sql: str, *params) -> psycopg2.cursor:
        """
        Run an sql query, returning the cursor.
        """
        self.cursor.execute(sql, params)
        return self.cursor

    def first(self, sql: str, *params) -> dict:
        """
        Run an sql query, returning a dict of the first row.
        """
        return self.query(sql, *params).fetchone()

    def all(self, sql: str, *params) -> []:
        """
        Run an sql query, returning an array with all the results.
        Each row contains a tuple with each column value.
        """
        return self.query(sql, *params).fetchall()

    def find(self, table: str, **where) -> dict:
        """
        Run an sql query, returning a dict of the matched row.
        """
        statement = "SELECT * FROM {0} WHERE {1} ORDER BY id DESC LIMIT 1"
        where_clause = " AND ".join([col + " = %s" for col in where])
        sql = statement.format(table, where_clause)
        return self.first(sql, *where.values())
