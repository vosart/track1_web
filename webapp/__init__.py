from flask import Flask, render_template
from webapp.model import db
from webapp.weather import weather_by_city
from webapp.python_org_news import get_python_news



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        title = "Новости Python"
        city = app.config['WEATHER_DEFAULY_CITY']
        weather = weather_by_city(city)
        news_list = get_python_news()
        return render_template('index.html', page_title=title, weather=weather, news_list=news_list )
    return app

