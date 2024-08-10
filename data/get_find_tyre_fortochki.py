from zeep import Client, helpers
from config_reader import fortochki_login, fortochki_password
from schemas.find_tyre import MaskTyre


# def get_find_tyre_fortochki(diameter: int, height: int, season: list[str],
#                             width: int, thorn: bool, wrh: list[int], brand: list[str]) -> list[str]:
def get_find_tyre_fortochki(mask_tyre: MaskTyre) -> list[str]:

    client = Client('https://api-b2b.4tochki.ru/WCF/ClientService.svc?wsdl')

    ArrayOfString = client.get_type('ns3:ArrayOfstring')
    ArrayOfint = client.get_type('ns3:ArrayOfint')
    season_list = ArrayOfString(mask_tyre.season)
    # wrh_list = ArrayOfint([1015])
    wrh_list = ArrayOfint(mask_tyre.wrh_list)
    brand_list = ArrayOfString(mask_tyre.brand_list)


    FindTyreFilter = client.get_type('ns2:FindTyreFilter')
    tyre_filter = FindTyreFilter(brand_list=brand_list,
                                 diameter_max=mask_tyre.diameter,
                                 diameter_min=mask_tyre.diameter,
                                 height_max=mask_tyre.height,
                                 height_min=mask_tyre.height,
                                 quality=0,
                                 season_list=season_list,
                                 sort=3,
                                 width_max=mask_tyre.width,
                                 width_min=mask_tyre.width,
                                 thorn=mask_tyre.thorn,
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

