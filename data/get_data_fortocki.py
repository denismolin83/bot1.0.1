from zeep import Client, helpers

client = Client('https://api-b2b.4tochki.ru/WCF/ClientService.svc?wsdl')

ArrayOfString = client.get_type('ns3:ArrayOfstring')
array_code = ['R2960', 'E4522']
value_code_list = ArrayOfString(array_code)

response = client.service.GetGoodsInfo(login='sa23208',
                                       password='aByeHZ4tS-',
                                       code_list=value_code_list)

data = helpers.serialize_object(response, dict)

#print(response)

print(data['tyreList'])

tyreList = data['tyreList']['TyreContainer']

for tyre in tyreList:
    print(f"{tyre['code']} - {int(tyre['diameter'])}")



