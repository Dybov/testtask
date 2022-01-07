from flask import Flask, render_template


def create_app(config_object='config.AppConfig'):
    app = Flask(__name__)

    # Dynamic config to use this entrypoint by both development and production.
    # Do not forget to create config/prod.py with ProdConfig in production.
    app.config.from_object(config_object)

    @app.route('/')
    def index():
        return render_template('index.html')

    # Use app context because DATABASE_URI provides by context
    with app.app_context():
        from db import init_app
        init_app(app)

    import auth
    app.register_blueprint(auth.bp)

    return app


if __name__ == '__main__':
    # app.run() allows to use it in both development like 'python app.py'
    # and production with uwsgi.
    # Avoid using 'flask run' command without setting FLASK_ENV='development'.
    app = create_app()
    app.run()
