import unittest
import Module2

class TestsForModule2(unittest.TestCase):
    
    def tests_flapsUpNormal(self):
        mod2out = Module2.module2(120000,1,0,0)
        self.assertTrue(not mod2out[0] and not mod2out[1])
    
    def tests_flapsUpHigh(self):    
        mod2out = Module2.module2(120000,2.51,0,1)
        self.assertTrue(mod2out[0] and mod2out[1])
    
    def tests_flapsUpLowSafe(self):
        mod2out = Module2.module2(120000,-1.0,0,1)
        self.assertTrue(not mod2out[0] and not mod2out[1])
    
    def tests_flapsUpLowExceed(self):
        mod2out = Module2.module2(120000,-1.01,0,0)
        self.assertTrue(mod2out[0] and not mod2out[1])
        
        
        
    def tests_flapsOutNormal(self):
        mod2out = Module2.module2(120000,2.0,0.1,0)
        self.assertTrue(not mod2out[0] and not mod2out[1])
    
    def tests_flapsOutHigh(self):    
        mod2out = Module2.module2(120000,2.01,15,1)
        self.assertTrue(mod2out[0] and mod2out[1])
    
    def tests_flapsOutLowSafe(self):
        mod2out = Module2.module2(120000,0.0,20,1)
        self.assertTrue(not mod2out[0] and not mod2out[1])
    
    def tests_flapsOutLowExceed(self):
        mod2out = Module2.module2(120000,-0.01,11,0)
        self.assertTrue(mod2out[0] and not mod2out[1])
        
        
    def tests_HeavySafe(self):
        mod2out = Module2.module2(120000,1.5,35,0)
        self.assertTrue(not mod2out[0] and not mod2out[1])
    
    def tests_HeavyUnsafe(self):    
        mod2out = Module2.module2(120000,1.51,27,1)
        self.assertTrue(mod2out[0] and mod2out[1])
        
        
    def tests_NormalSafe(self):
        mod2out = Module2.module2(100000,1.88,30.1,0)
        self.assertTrue(not mod2out[0] and not mod2out[1])
    
    def tests_NormalUnsafe(self):    
        mod2out = Module2.module2(100000,1.89,30,0)
        self.assertTrue(mod2out[0] and not mod2out[1])
        
    
    def tests_LightSafe(self):
        mod2out = Module2.module2(95000,2.00,25.1,0)
        self.assertTrue(not mod2out[0] and not mod2out[1])
    
    def tests_LightUnsafe(self):    
        mod2out = Module2.module2(95000,2.01,25,1)
        self.assertTrue(mod2out[0] and mod2out[1])

        
if __name__ == '__main__':
    unittest.main()
