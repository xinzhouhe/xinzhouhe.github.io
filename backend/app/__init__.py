# backend/app/__init__.py
from flask import Flask, send_from_directory
from .config import Config
from .extensions import db, jwt, mail
from .routes import register_routes

def create_app():
    app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)

    # 注册控制器中的路由
    register_routes(app)

    # 处理React路由
    @app.route('/')
    @app.route('/<path:path>')
    def serve_react_app(path=None):
        if path is None:
            path = 'index.html'
        return send_from_directory(app.static_folder, path)

    return app
