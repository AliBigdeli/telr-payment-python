import requests


class Telr:

    url = "https://secure.telr.com/gateway/order.json"
    default_currency = "AED"

    def __init__(self, auth_key, store_id, **options):

        if isinstance(auth_key, str):
            self.auth_key = auth_key
        else:
            raise TypeError("auth_key must be String")

        if isinstance(store_id, str):
            self.store_id = store_id
        else:
            raise TypeError("store_id must be String")
        self.options = options

        self.test = options.get('test') or 0

    def order(self, **options):
        post_data = {
            "ivp_method": "create",
            "ivp_currency": options.get('currency') or self.default_currency,
            "ivp_test": self.test,
            "ivp_authkey": self.auth_key,
            "ivp_store": self.store_id
        }

        if not bool(options.get("order_id")):
            raise ValueError("Unique order_id is not provided.")

        if not bool(options.get("amount")):
            raise ValueError("amount is not provided.")

        if not bool(options.get("return_url")):
            raise ValueError("return_url is not provided.")

        if not bool(options.get("description")):
            raise ValueError("description is not provided.")

        post_data["ivp_cart"] = options.get("order_id")
        post_data["return_auth"] = options.get("return_url")
        post_data["return_decl"] = options.get("return_decl")
        post_data["return_can"] = options.get("return_can")
        post_data["ivp_desc"] = options.get("description")
        post_data["ivp_amount"] = options.get("amount")
        post_data["bill_fname"] = options.get("first_name") or None
        post_data["bill_sname"] = options.get("last_name") or None
        post_data["bill_addr1"] = options.get("address") or None
        post_data["bill_city"] = options.get("city") or None
        post_data["bill_country"] = options.get("country") or None
        post_data["bill_email"] = options.get("email") or None

        return requests.post(url=self.url, data=post_data).json()


    def status(self, order_reference):

        if order_reference is None:
            raise ValueError("orderReference is not provided.")

        post_data = {
            "ivp_method": "check",
            "order_ref": order_reference,
            "ivp_test": self.test,
            "ivp_authkey": self.auth_key,
            "ivp_store": self.store_id
        }

        return requests.post(url=self.url, data=post_data).json()
