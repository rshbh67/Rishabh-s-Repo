import requests

data={
  "order_id": "ordID14",
  "order_date": "2024-04-15",
  "order_type": "ESSENTIALS",
  "consignee_name": "Aman",
  "consignee_phone": 8597888884,
  "consignee_email": "johnhelp@gmail.com",
  "consignee_address_line_one": "Sector 49",
  "consignee_address_line_two": "Sohna Road",
  "consignee_pin_code": 122001,
  "consignee_city": "Gurgaon",
  "consignee_state": "Haryana",
  "product_detail": [
    {
      "name": "cooler",
      "sku_number": "22",
      "quantity": 1,
      "discount": "",
      "hsn": "#123",
      "unit_price": 1000,
      "product_category": "Other"
    }
  ],
  "payment_type": "PREPAID",
  "cod_amount": "",
  "weight": 35,
  "length": 25,
  "width": 25,
  "height": 25,
  "warehouse_id": "",
  "gst_ewaybill_number": "",
  "gstin_number": ""
}

url = "https://shipping-api.com/app/api/v1/push-order"

headers = {
    "accept": "application/json" ,
    "public-key": "W0rZ4fuo1mv2pJTSMVOh",
    "private-key": "AZK92QSq7ZOWE8fwkYFo",
    "Content-Type": "application/json"
}

res = requests.post(url, json=data, headers=headers)

print(res.status_code)
print(res.json())
print(res.content)
