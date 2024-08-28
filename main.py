"""
Earthquake detection app:
Modularization with Function,
Modularization with Package
Procedural program 002
"""
import recent_earthquake2

if __name__ == '__main__':
    print('Package description is', recent_earthquake2.description)
    result = recent_earthquake2.data_extraction()
    recent_earthquake2.show_data(result)

