import requests

url ="https://api.ycloud.com/v2/whatsapp/messages/sendDirectly"


order_number = 155501
order_id = "idid"
track_id = "this_is_id"

headers={"X-API-Key": "386754f816783e4886c8bc7a99d14a0c" ,
"accept": "application/json" ,
"content-type": "application/json" 
}
j = {
    "from": "+919821908015",
    "to": "+918979830599",
    "type": "template",
    "template": {

    "name": "moonord2",
    "language": {
      "code": "en"
    },
    "components": [
      {
        "type": "body",
       "parameters": [
          {
            "type": "text",
            "text": order_number
          },{
            "type": "text",
            "text": order_id
          },{
            "type": "text",
            "text": track_id
          }
        ]
      }
    ]
    }
}

res=requests.post(url,headers=headers,json=j)

print(res.content,res.status_code)