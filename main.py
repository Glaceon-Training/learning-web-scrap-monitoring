"""
Earthquake detection app:
Modularization with Function,
Modularization with Package
Procedural program 002
"""
import recent_earthquake2

if __name__ == '__main__':
    indonesia_earthquake = recent_earthquake2.LatestEarthquake('https://bmkg.go.id/')
    indonesia_earthquake.show_description()
    indonesia_earthquake.run()
