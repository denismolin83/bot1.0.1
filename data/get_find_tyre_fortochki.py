from zeep import Client, helpers
from config_reader import fortochki_login, fortochki_password


def get_find_tyre_fortochki(diameter: int, height: int, season: list[str], width: int, thorn: bool) -> list[str]:
    client = Client('https://api-b2b.4tochki.ru/WCF/ClientService.svc?wsdl')

    ArrayOfString = client.get_type('ns3:ArrayOfstring')
    ArrayOfint = client.get_type('ns3:ArrayOfint')
    season_list = ArrayOfString(season)
    wrh_list = ArrayOfint([1015])

    FindTyreFilter = client.get_type('ns2:FindTyreFilter')
    tyre_filter = FindTyreFilter(diameter_max=diameter,
                                 diameter_min=diameter,
                                 height_max=height,
                                 height_min=height,
                                 quality=0,
                                 season_list=season_list,
                                 sort=3,
                                 width_max=width,
                                 width_min=width,
                                 thorn=thorn,
                                 wrh_list=wrh_list,
                                 include_paid_delivery=False,
                                 retread=False)

    response = client.service.GetFindTyre(login=fortochki_login,
                                          password=fortochki_password,
                                          filter=tyre_filter,
                                          page=0,
                                          pageSize=100)

    data = helpers.serialize_object(response, dict)

    # print(data)

    if data['price_rest_list'] is None:
        return []

    tyre_price_rest = data['price_rest_list']['TyrePriceRest']
    list_of_tyre_price_rest = []

    for tyre in tyre_price_rest:
        list_of_tyre_price_rest.append(
            f'{tyre['code']} - {tyre['name']} - {tyre['whpr']['wh_price_rest'][0]['price']} - {tyre['whpr']['wh_price_rest'][0]['rest']}')

    return list_of_tyre_price_rest

