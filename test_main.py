import numpy as np
import unittest
import main

class UnitTests(unittest.TestCase) :
    def test_neg_binom(self) : 
       for r in range(2,6) : 
           for i in range(1,9) : 
               p, mean = i*0.1, 0 
               for j in range(100) : mean = mean + negative_binomial(r,p)
               mean = mean / 100
               var = (r*(1-p)) / (p*p) 
               self.assertTrue( np.fabs( mean - r/p )<bar, "your negative binomial function is not sampling from the correct distribution" )
