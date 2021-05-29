import math
import unittest
import random

def wallis (n): #  Function to estimate pi using the WALLIS ESTIMATION 
    points=1 #intializing  the value
    for i in range (1,(n+1)):
        numerator=(pow(i,2)*4)
        denominator=(pow(i,2)*4)-1
        points=points*(numerator/denominator) #calculating pi/2 by finding numerator and denominator separately then dividing
    z=2*points #according to wallis formula
    return (z)

def monte_carlo (n): #Estmating pi using the MONTE CARLO METHOD 
    circle=0
    for i in range (n):
        x=random.random() #generating random x cordinate
        y=random.random()
        point=[x,y]
        origin=[0,0]
        z=math.dist(point,origin)  #calculating distance
        if z<=1:                #checking if distance <=1 (inside the circle)
            circle=circle+1
    try:
        montcarlo_solution=(4*circle)/n   #the monte carlo estimation of pi
    except:
        montcarlo_solution=(4*circle)
    return (montcarlo_solution)
    
class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()


