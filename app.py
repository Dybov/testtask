from flask import Flask

app = Flask(__name__)

# Dynamic config to use this entrypoint by both development and production.
# Do not forget to create config/prod.py with ProdConfig class in production.
app.config.from_object('config.AppConfig')


if __name__ == '__main__':
    # app.run() allows to use is in development like 'python app.py'
    # and in production with uwsgi.
    # Avoid using 'flask run' command without setting FLASK_ENV='development'.
    app.run()
