from telr_payment.api import Telr
from pprint import pprint

# if you dont want it to run in test mode change the test option according to docs
telr = Telr(auth_key = "YOUR_AUTH_KEY",store_id = "YOUR_STORE_ID",test=1)

status_response = telr.status(
    order_reference = "ORDER_REF_TOKEN"
)
pprint(status_response)