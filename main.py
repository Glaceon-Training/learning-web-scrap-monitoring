"""
Earthquake detection app:
Modularization with Function,
Modularization with Package
"""
from learn_recent_earthquake2 import data_extraction, show_data

if __name__ == '__main__':
    print('Main App\n')
    result = data_extraction()
    show_data(result)
