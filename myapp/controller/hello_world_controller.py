from myapp.resources.services.student import Student


def post_greeting(body):
    return Student().add_student(body)    

def get_hello_world():
    return "Hello"  