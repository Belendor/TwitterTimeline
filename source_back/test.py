from datetime import datetime
import pycron

@pycron.cron("* * * * * */5")
async def test(timestamp: datetime):
    print(f"test cron job running at {timestamp}")

pycron.start()