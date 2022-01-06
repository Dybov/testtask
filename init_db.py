"""Inititalize and reinitialize DB"""
import os

import sqlalchemy


def main():
    """Drop, init, and prepopulate DB"""
    # Provide app_context and ensure all models from blueprints are loaded
    from app import create_app
    app = create_app()

    from db import init_db, drop_db, engine
    drop_db()
    app.logger.info('Database has dropped.')
    init_db()
    app.logger.info('Database has initialized.')

    # Traverse SQL fixtures (test seeds)
    for root, directories, files in os.walk('fixtures/sql'):
        for filename in files:
            # Skip not SQL files
            if not filename.lower().endswith('.sql'):
                continue

            path = os.path.join(root, filename)
            with open(path) as file:
                escaped_text = sqlalchemy.text(file.read())

            try:
                engine.execute(escaped_text)
            except sqlalchemy.exc.ProgrammingError:
                raise Exception(f'Put proper SQL in file {path}')


if __name__ == "__main__":
    main()
