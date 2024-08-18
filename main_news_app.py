"""
News Fetch App
"""
from learn_pop_news import data_extract, show_data

if __name__ == '__main__':
    print('Popular News\n')
    result = data_extract()
    show_data(result)