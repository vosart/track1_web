from flask import Blueprint, current_app, render_template

from webapp.news.models import News
from webapp.weather import weather_by_city

blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    title = 'Новости Python'
    city = current_app.config['WEATHER_DEFAULY_CITY']
    weather = weather_by_city(city)
    news_list = News.query.order_by(News.published.desc()).all()
    return render_template(
        'news/index.html',
        page_title=title,
        weather=weather,
        news_list=news_list,
    )
