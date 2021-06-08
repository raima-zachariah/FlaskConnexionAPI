from sqlalchemy import create_engine
from myapp.resources.db_repository.models import meta, students
import os

class DBManager:
    def __init__(self):
        self.uri = os.environ.get("DB_URI")
        self.engine = create_engine(self.uri)
        self.instantiate_db()
    
    def instantiate_db(self):
        meta.create_all(self.engine)

    
class DBOperations:
    def __init__(self):
        self.uri = os.environ.get("DB_URI")s
        self.engine = create_engine(self.uri)
        self.conn = self.engine.connect()
        self.db = students

    def insert(self, body):
        ins = self.db.insert().values(body)
        result = self.conn.execute(ins)
        return result.inserted_primary_key
    
    def read(self):
        query = self.db.select()
        result = self.conn.execute(query)

        # for row in result:
        #     print (row)

        return result
    
    def update(self, id, body):
        query = self.db.update().where(self.db.c.id==id).values(body)
        self.conn.execute(query)

    def delete(self, id):
        query = self.db.delete().where(self.db.c.id==id)
        self.conn.execute(query)