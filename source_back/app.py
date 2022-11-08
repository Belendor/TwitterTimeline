from twitter import create_app
from datetime import datetime
# import pycron

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')


# @pycron.cron("* * * * * */5")
# async def test(timestamp: datetime):
#     print(f"test cron job running at {timestamp}")


pycron.start()


   