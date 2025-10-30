#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 10/20/25
#Description: given a time(t) the function will return how far an object has fallen in meters

#define fall distance function
def fall_distance(t):
    """
    calculate the distance an object falls due to gravity in a given amount time
    argument:
    t: The time in seconds that the object has been falling.

    returns:
    The distance in meters that the object has fallen
    """
    #gravity 9.8m/s^2
    g = 9.8
    #distance formula in regards to gravity
    d = (1 / 2) * g * t ** 2
    return d

#dist = fall_distance(200)
#print(dist,"meters")