import connexion


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='openapi/')
    app.add_api('api_v1.yaml', arguments={'title': 'Hello World Example'})
    app.run()