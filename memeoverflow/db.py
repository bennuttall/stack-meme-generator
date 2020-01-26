import sqlite3


class MemeDatabase:
    """
    Meme database interface (sqlite)

    :param str site:
        The name of the StackExchange site as an identifier (used as the table
        name)

    :param str db_path:
        Path to the sqlite database file
    """
    def __init__(self, site, db_path):
        self.site = site
        self.conn = sqlite3.connect(db_path)
        cursor = self.conn.cursor()
        cursor.execute(f'create table if not exists {site} (question_id int unique)')
        cursor.close()

    def __repr__(self):
        return f"<MemeDatabase object for site {self.site}>"

    def insert_question(self, id):
        "Insert a question ID"
        cursor = self.conn.cursor()
        cursor.execute(f'insert into {self.site} values (?)', (id, ))
        self.conn.commit()
        cursor.close()

    def question_is_known(self, id):
        """
        Return True if the provided question ID is already in the database,
        otherwise return False
        """
        cursor = self.conn.cursor()
        cursor.execute(f'select 1 from {self.site} where question_id = ?', (id, ))
        result = bool(cursor.fetchone())
        cursor.close()
        return result
