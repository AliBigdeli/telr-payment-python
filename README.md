<p align="center">
<a href="https://telr.com/" target="_blank"> <img src="https://user-images.githubusercontent.com/29748439/184531831-9c209f6b-7d78-44c0-92b0-5ac864ba5e4a.jpg" style="max-width:1280 px;"/> </a>
</p>
<h1 align="center">Python Telr Payment Gateway API</h1>
<h3 align="center">a simple module to integrate with telr api for python language</h3>



# Overview
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Status](#status)
- [Test Cards](#test-cards)
- [Order Creation Response Sample](#order-creation-response-sample)
  - [successful](#successful)
  - [Failed](#failed)
- [Check Response Sample](#check-response-sample)
  - [Successful](#successful-1)
  - [Pending](#pending)
  - [Canceled](#canceled)
- [References](#references)

# Installation
This module is a pip package for implement API's payment service of Telr. in order to use this module you have to install it by pip command or through setup.

```bash
pip install telr_payment
```
Import package into your project by:

```bash
from telr_payment.api import Telr
```
in order to use the module please consider looking at examples and documentations.

# Usage
For easy implementations i have provided two simple examples, one for creating the transaction and one for checking which is like this

```python
# order_sample.py
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

```


```python
# check_sample.py
from telr_payment.api import Telr
from pprint import pprint

# if you dont want it to run in test mode change the test option according to docs
telr = Telr(auth_key = "YOUR_AUTH_KEY",store_id = "YOUR_STORE_ID",test=1)

status_response = telr.status(
    order_reference = "ORDER_REF_TOKEN"
)
pprint(status_response)

```
# Status
The table of status of checking transaction

<table>
<thead>
<tr class="row-1 odd">
	<th class="column-1">Order Status</th><th class="column-2">Description</th>
</tr>
</thead>
<tbody class="row-hover">
<tr class="row-2 even">
	<td class="column-1">1</td><td class="column-2">Pending</td>
</tr>
<tr class="row-3 odd">
	<td class="column-1">2</td><td class="column-2">Authorised (Transaction not captured, such as an AUTH transaction or a SALE<br>
transaction which has been placed on hold)</td>
</tr>
<tr class="row-4 even">
	<td class="column-1">3</td><td class="column-2">Paid (Transaction captured, SALE transaction, not placed on hold)</td>
</tr>
<tr class="row-5 odd">
	<td class="column-1">-1</td><td class="column-2">Expired</td>
</tr>
<tr class="row-6 even">
	<td class="column-1">-2</td><td class="column-2">Cancelled</td>
</tr>
<tr class="row-7 odd">
	<td class="column-1">-3</td><td class="column-2">Declined</td>
</tr>
</tbody>
</table>


# Test Cards

<table>
<thead>
<tr class="row-1 odd">
	<th class="column-1">Card number</th><th class="column-2">Type</th><th class="column-3">CVV</th><th class="column-4">MPI</th>
</tr>
</thead>
<tbody class="row-hover">
<tr class="row-2 even">
	<td class="column-1">4000 0000 0000 0002</td><td class="column-2">Visa</td><td class="column-3">123</td><td class="column-4">No</td>
</tr>
<tr class="row-3 odd">
	<td class="column-1">4111 1111 1111 1111</td><td class="column-2">Visa</td><td class="column-3">123</td><td class="column-4">Yes</td>
</tr>
<tr class="row-4 even">
	<td class="column-1">4444 3333 2222 1111</td><td class="column-2">Visa</td><td class="column-3">123</td><td class="column-4">Yes</td>
</tr>
<tr class="row-5 odd">
	<td class="column-1">4444 4244 4444 4440</td><td class="column-2">Visa</td><td class="column-3">123</td><td class="column-4">Yes</td>
</tr>
<tr class="row-6 even">
	<td class="column-1">4444 4444 4444 4448</td><td class="column-2">Visa</td><td class="column-3">123</td><td class="column-4">Yes</td>
</tr>
<tr class="row-7 odd">
	<td class="column-1">4012 8888 8888 1881</td><td class="column-2">Visa</td><td class="column-3">123</td><td class="column-4">Yes</td>
</tr>
<tr class="row-8 even">
	<td class="column-1">5105 1051 0510 5100</td><td class="column-2">Mastercard</td><td class="column-3">123</td><td class="column-4">No</td>
</tr>
<tr class="row-9 odd">
	<td class="column-1">5454 5454 5454 5454</td><td class="column-2">Mastercard</td><td class="column-3">123</td><td class="column-4">Yes</td>
</tr>
<tr class="row-10 even">
	<td class="column-1">5555 5555 5555 4444</td><td class="column-2">Mastercard</td><td class="column-3">123</td><td class="column-4">Yes</td>
</tr>
<tr class="row-11 odd">
	<td class="column-1">5555 5555 5555 5557</td><td class="column-2">Mastercard</td><td class="column-3">123</td><td class="column-4">Yes</td>
</tr>
<tr class="row-12 even">
	<td class="column-1">5581 5822 2222 2229</td><td class="column-2">Mastercard</td><td class="column-3">123</td><td class="column-4">Yes</td>
</tr>
<tr class="row-13 odd">
	<td class="column-1">5641 8209 0009 7002</td><td class="column-2">Maestro UK</td><td class="column-3">123</td><td class="column-4">Yes</td>
</tr>
<tr class="row-14 even">
	<td class="column-1">6767 0957 4000 0005</td><td class="column-2">Solo</td><td class="column-3">123</td><td class="column-4">No</td>
</tr>
<tr class="row-15 odd">
	<td class="column-1">3434 343434 34343</td><td class="column-2">American Express</td><td class="column-3">1234</td><td class="column-4">No</td>
</tr>
<tr class="row-16 even">
	<td class="column-1">3566 0020 2014 0006</td><td class="column-2">JCB</td><td class="column-3">123</td><td class="column-4">No</td>
</tr>
<tr class="row-17 odd">
	<td class="column-1">3111 1111 1111 1111</td><td class="column-2">MADA</td><td class="column-3">123</td><td class="column-4">No</td>
</tr>
</tbody>
</table>

<p>The card security code (CVV) to use with the test cards is 123 (except for American Express, which should be 1234) for an authorised response, other codes will be declined.</p>

<p>Cards which show ‘Yes’ in the MPI column will use a simulated 3D Secure authentication page, allowing you to test the transaction flow when Verified by Visa or MasterCard SecureCode is used. </p>


# Order Creation Response Sample

## successful
```javascript
{'method': 'create',
 'order': {'ref': 'ORDER_REF_TOKEN',
           'url': 'https://secure.telr.com/gateway/process.html?o=ORDER_REF_TOKEN'},
 'trace': 'xxxx/xxxx/xxxxxxxx'}
```
## Failed
```javascript
{
  "method":"create",
  "error":{
    "message":"Exx: Error Name",
    "note":"Message according to error"
  }
}
```

# Check Response Sample

## Successful

```javascript
 {'method': 'check',
 'order': {'amount': '4.50',
           'card': {'country': 'AE',
                    'expiry': {'month': x, 'year': xxxx},
                    'first6': 'xxxxxx',
                    'last4': 'xxxx',
                    'type': 'Visa Credit'},
           'cartid': 'ORDER_ID_TOKEN',
           'currency': 'AED',
           'customer': {'address': {'city': 'xxxxx',
                                    'country': 'AE',
                                    'line1': 'xxxx,xxx,xxx',
                                    'mobile': '1234567890'},
                        'email': 'test@test.com',
                        'name': {'forenames': 'FIRST_NAME', 'surname': 'LAST_NAME'}},
           'description': 'testing',
           'paymethod': 'Card',
           'ref': 'ORDER_REF_TOKEN',
           'status': {'code': 3, 'text': 'Paid'},
           'test': 1,
           'transaction': {'class': 'ECom',
                           'code': '924861',
                           'date': '04 Aug 2022 12:56 GST',
                           'message': 'Authorised',
                           'ref': 'REF_TOKEN',
                           'status': 'A',
                           'type': 'sale'}},
 'trace': 'xxxx/xxxx/xxxxxxxx'}
```

## Pending

```javascript
{'method': 'check',
 'order': {'amount': '54.50',
           'cartid': 'ORDER_ID_TOKEN',
           'currency': 'AED',
           'description': 'TRANSACTION_DESCRIPTION',
           'ref': 'ORDER_REF_TOKEN',
           'status': {'code': 1, 'text': 'Pending'},
           'test': 1,
           'url': 'https://secure.telr.com/gateway/process.html?o=ORDER_REF_TOKEN'},
 'trace': 'xxxx/xxxx/xxxxxxxx'}
```

## Canceled

```javascript
{'method': 'check',
 'order': {'amount': '54.50',
           'cartid': 'ORDER_ID_TOKEN',
           'currency': 'AED',
           'description': 'TRANSACTION_DESCRIPTION',
           'ref': 'ORDER_REF_TOKEN',
           'status': {'code': -2, 'text': 'Cancelled'},
           'test': 1},
 'trace': 'xxxx/xxxx/xxxxxxxx'}
```

# References
- https://telr.com/support/knowledge-base/hosted-payment-page-integration-guide/
