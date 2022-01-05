from flask import Flask


def create_app(config_object='config.AppConfig'):
    app = Flask(__name__)

    # Dynamic config to use this entrypoint by both development and production.
    # Do not forget to create config/prod.py with ProdConfig in production.
    app.config.from_object(config_object)

    return app


if __name__ == '__main__':
    # app.run() allows to use it in both development like 'python app.py'
    # and production with uwsgi.
    # Avoid using 'flask run' command without setting FLASK_ENV='development'.
    app = create_app()
    app.run()
