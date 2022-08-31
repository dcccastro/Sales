from flask import Flask
import api


def create_app():
    app = Flask(__name__)
    app.config.from_object('app_config')
    api.init_app(app)

    return app

app = create_app()

if __name__ == "__main__":
    app.run()