"""
News Fetch App
"""


def data_extract():
    """
        #1
        Erick Thohir: Maarten Paes Sah Bermain buat Timnas Indonesia
        Sepakbola | 2 jam yang lalu
        #2
        Maarten Paes Diharapkan Tingkatkan Level Timnas Indonesia
        Sepakbola | 58 menit yang lalu
        #3
        Bebas Bersyarat, Jessica Wongso Merasa Sudah Plong
        detikNews | 3 jam yang lalu
        #4
        FK Unpad Sanksi Keras 10 Pelaku Bullying di PPDS Bedah Saraf RSHS
        detikHealth | 2 jam yang lalu
        #5
        Cak Imin Ungkap Obrolan Saat Diajak Keliling IKN Bareng Jokowi
        detikNews | 35 menit yang lalu
    """


    extract = dict()
    extract['news1'] = 'Erick Thohir: Maarten Paes Sah Bermain buat Timnas Indonesia'
    extract['news2'] = 'Maarten Paes Diharapkan Tingkatkan Level Timnas Indonesia'
    extract['news3'] = 'Bebas Bersyarat, Jessica Wongso Merasa Sudah Plong'
    extract['news4'] = 'FK Unpad Sanksi Keras 10 Pelaku Bullying di PPDS Bedah Saraf RSHS'
    extract['news5'] = 'Cak Imin Ungkap Obrolan Saat Diajak Keliling IKN Bareng Jokowi'
    return extract


def show_data(result):
    print('Most Popular News Today:')
    print(f'News #1: {result['news1']}')
    print(f'News #2: {result['news2']}')
    print(f'News #3: {result['news3']}')
    print(f'News #4: {result['news4']}')
    print(f'News #5: {result['news5']}')


if __name__ == '__main__':
    print('Popular News\n')
    result = data_extract()
    show_data(result)
