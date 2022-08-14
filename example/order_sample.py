from telr_payment.api import Telr
from pprint import pprint

# if you dont want it to run in test mode change the test option according to docs
telr = Telr(auth_key = "YOUR_AUTH_KEY",store_id = "YOUR_STORE_ID",test=1)

order_response = telr.order(
    order_id = "ORDER_ID_TOKEN",
    amount=54.5,
    return_url= "http://domain.com/path/to/url",
    return_decl= "http://domain.com/path/to/url",
    return_can= "http://domain.com/path/to/url",
    description="testing"
)
pprint(order_response)