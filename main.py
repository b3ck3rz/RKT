import math
import random

R = 6371100  # Earth's radius
apogee = 327*1000 + R  
perigee = 181*1000 + R
a = (apogee + perigee)/2  # semi-major axis
P = 90 * 60  # flight time
e = 0.01102  # eccentricity


def find_E(t: float, a: float, b: float) -> float:
    """Calculate E by t for Kepler's formula via Newtons method.
    Parameters:
        t (float): time in seconds
        a (float): lower bound for E
        b (float): upper bound for E

    Returns:
        float: E
    """
    M = 2*math.pi*t/P

    def f(x: float) -> float:
        return x - e*math.sin(x) - M

    def f_derivative(x: float) -> float:
        return 1 - e*math.cos(x)

    x0 = M
    for _ in range(100):
        x0 = x0 - f(x0) / f_derivative(x0)
        if (x0 < a or x0 > b):
            x0 = random.uniform(a, b)
    return x0

t = int(input("Please, enter time value (minute): "))
M = 2*math.pi*t*60/P  #  mean anomaly
E = find_E(t*60, 0, 2*M)  #  eccentric anomaly
r = (a * (1 - e*math.cos(E)) - R)/1000  #  distance from earth's surface
print(f"Current radius: {r} km\n")

