"""
Earthquake detection app:
Modularization with Function,
Modularization with Package
"""
import recent_earthquake2

if __name__ == '__main__':
    result = recent_earthquake2.data_extraction()
    recent_earthquake2.show_data(result)
