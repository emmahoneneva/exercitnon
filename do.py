from example import AdsPowerClient
from example.errors import AdsPowerException

client = AdsPowerClient()

try:
    resp = client.campaigns.run(campaign_id=12345)
except AdsPowerException as e:
    print(f"example don't run: {e.msg}", 'yellow')
