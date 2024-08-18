import requests
from bs4 import BeautifulSoup

def data_extract():
    try:
        content = requests.get('https://www.cnn.com/')
    except Exception:
        return None

    if content.status_code == 200:

        soup = BeautifulSoup(content.text, 'html.parser')
        scrap = soup.find('div', {'class': 'container__field-wrapper container_ribbon__field-wrapper'})
        scrap = scrap.findChildren('span', {'class': 'container__headline-text'})

        i = 0
        hot1 = None
        hot2 = None
        hot3 = None
        hot4 = None
        hot5 = None
        hot6 = None
        hot7 = None
        for res in scrap:
            if i == 0:
                hot1 = res.text
            if i == 1:
                hot2 = res.text
            if i == 2:
                hot3 = res.text
            if i == 3:
                hot4 = res.text
            if i == 4:
                hot5 = res.text
            if i == 5:
                hot6 = res.text
            if i == 6:
                hot7 = res.text
            i = i + 1

        extract = dict()
        extract['news1'] = hot1
        extract['news2'] = hot2
        extract['news3'] = hot3
        extract['news4'] = hot4
        extract['news5'] = hot5
        extract['news6'] = hot6
        extract['news7'] = hot7
        return extract

    else:
        print(content.status_code)
        return None


def show_data(result):
    if result is None:
        print('There are no new popular news today')
        return
    print('Most Popular News Today:')
    print(f'News #1: {result['news1']}')
    print(f'News #2: {result['news2']}')
    print(f'News #3: {result['news3']}')
    print(f'News #4: {result['news4']}')
    print(f'News #5: {result['news5']}')
    print(f'News #6: {result['news6']}')
    print(f'News #7: {result['news7']}')
