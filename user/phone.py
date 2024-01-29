from melipayamak import Api
username = '09910774216'
password = '89G0T'
api = Api(username,password)
sms = api.sms()
to = '09145347800'
_from = '50002710074216'
isflash = True
text = 'تست وب سرویس ملی پیامک'
response = sms.send(to,_from,text,isflash)
print(response)