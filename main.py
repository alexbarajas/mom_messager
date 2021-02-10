import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = os.environ.get("API_KEY")  # get your own API key from Twilio
account_sid = "####################"  # gotten from Twilio
auth_token = os.environ.get("AUTH_TOKEN")  # get your own authentication token from Twilio

twilio_number="+###########"  # get your own phone number from Twilio

# where the message is sent
proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
client = Client(account_sid, auth_token, http_client=proxy_client)
message = client.messages \
    .create(
    body="Good morning mom.",
    from_=twilio_number,
    to="##########"  # the number of the person you are sending the message to
)
