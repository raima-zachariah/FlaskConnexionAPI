import connexion
from myapp.resources.db_repository.database_manager import DBManager

if __name__ == '__main__':
    DBManager().instantiate_db()
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='myapp/openapi/')
    app.add_api('api_v1.yaml', arguments={'title': 'Hello World Example'})
    app.run()