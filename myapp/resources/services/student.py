from myapp.resources.db_repository.database_manager import DBOperations

class Student:
    def add_student(self, body):
        id = DBOperations().insert(body)[0]
        body["id"] = id
        return body