from flask import Flask
import config, schedule_config
from flask_apscheduler import APScheduler
from app.resources import create_api

scheduler = APScheduler()

def create_app():
    app = Flask(__name__, template_folder='../front')
    app.config.from_object(config)
    # 加载定时任务配置
    app.config.from_object(schedule_config)
    scheduler.init_app(app)

    api = create_api()
    api.init_app(app)

    scheduler.start()
    return app