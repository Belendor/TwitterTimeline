from flask import Flask
from flask_cors import CORS
import pycron
from datetime import datetime

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    CORS(app)
    
    from .views import views
    from .auth import auth
    from .tweets import tweets

    app.register_blueprint(views)
    app.register_blueprint(auth)
    app.register_blueprint(tweets)

    # @pycron.cron("* * * * * */5")
    # async def test(timestamp: datetime):
    #     print(f"test cron job running at {timestamp}")

    # pycron.start()

    return app