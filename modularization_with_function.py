"""
Earthquake detection app:
Modularization with Function,
Modularization with Package

Manual input version
"""


def data_extract():
    """
    Date: 16 Agustus 2024
    Time: 08:16:04 WIB
    Magnitude: 5.1
    Depth: 226 km
    Location: LS=8.07 BT=123.01
    Epicentre: 27 km Timur Laut LARANTUKA-NTT
    Tsunami Alert: tidak berpotensi TSUNAMI
    :return:
    """

    extract = dict()
    extract['date'] = "16 Agustus 2024"
    extract['time'] = "08:16:04 WIB"
    extract['magnitude'] = 5.1
    extract['depth_in_km'] = 226
    extract['location'] = {'ls': 8.07, 'bt': 123.01}
    extract['epicentre'] = "27 km Timur Laut LARANTUKA-NTT"
    extract['tsunami_alert'] = "tidak berpotensi TSUNAMI"
    return extract


def show_data(result):
    print("BMKG latest earthquake detection")
    print(f"Date: {result['date']}")
    print(f"Time: {result['time']}")
    print(f"Magnitude: {result['magnitude']}")
    print(f"Depth: {result['depth_in_km']} km")
    print(f"Location: LS = {result['location']['ls']}, BT = {result['location']['bt']}")
    print(f"Epicentre: {result['epicentre']}")
    print(f"Tsunami Alert: {result['tsunami_alert']}")


if __name__ == '__main__':
    print('Main App\n')
    result = data_extract()
    show_data(result)
