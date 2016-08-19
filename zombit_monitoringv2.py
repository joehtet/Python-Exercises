
import unittest

def answer(intervals):
    
    # sort by starting shift of each minion
    shifts = sorted(intervals)
    total = 0 
    
    def sumShift(s1, s2): # compares adjacent shifts and adds them together if they're inclusive
        comShift = [] # Combined shifts
        if(max(s1)<min(s2)): # Gap inbetween shifts
            comShift = s2
        else: # no gap between shifts. combine them together
            comShift = [min(sorted(s1+s2)),max(sorted(s1+s2))]
    return total


# Test cases
case1 = [[[1, 3], [3, 6]], 5]
case2 = [[[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]] , 16]

class ZombitTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_case_1(self):
        self.assertEqual(answer(case1[0]),case1[1])
        
    def test_case_2(self):
        self.assertEqual(answer(case2[0]),case2[1])
        
        
 