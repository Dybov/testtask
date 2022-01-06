def main():
    # Provide app_context and ensure all models from blueprints are loaded
    from app import create_app
    app = create_app()

    from db import init_db
    init_db()


if __name__ == "__main__":
    main()
