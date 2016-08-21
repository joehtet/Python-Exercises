
import unittest


def sumShift(s1, s2): # compares adjacent shifts and adds them together if they're inclusive
	comShift = [] # Combined shifts
	if(max(s1)<min(s2)): # Gap inbetween shifts
		# Gap value
		timeBS = min(s2)-max(s1) # time not covered btwn s1 and s2
	else: # no gap between shifts. 
		timeBS = 0
	
	comShift = [min(sorted(s1+s2)),max(sorted(s1+s2))]
	
	return [comShift,timeBS]

def answer(intervals):
    
    # sort by starting shift of each minion
	shifts = sorted(intervals)
	
	def totalTime(shifts): # difference btwn latest end shift and earliest start shift
		y = 0 # latest end shift
		for i in shifts:
			if(y>i[1]):
				continue
			else:
				y = i[1]

		z = 0 # latest start shift
		for i in shifts:
			if(z>i[0]):
				continue
			else:
				z = i[0]

		x = z # earliest start shift
		for i in shifts:
			if(x>i[0]):
				x = i[0]
			else:
				continue

		return y-x 
		
	total = totalTime(shifts)
	
	holder = shifts[0]	# variable for s1+s2 as well as setting initial condition
	for i in range(0,len(shifts)-1):
		f = sumShift(holder,shifts[i+1])
		if(f[1]==0):
			holder = f[0]
		else:
			holder = shifts[i+1]
		total = total - f[1]
	
	return total


# Test cases
case1 = [[[1, 3], [3, 6]], 5]
case2 = [[[10, 14], [4, 18], [19, 20], [19, 20],[21,22],[23,24]],17]

class ZombitTest(unittest.TestCase):
	def setUp(self):
		pass
    
	def test_case_sumShift(self):
		self.assertEqual(sumShift([1,3],[2,4]),[[1,4],0])
		
	def test_case_sumShift_2(self):
		self.assertEqual(sumShift([0,1],[2,3]),[[0,3],1])
	
	def test_case_sumShift_3(self):
		self.assertEqual(sumShift([1,4],[1,4]),[[1,4],0])
	
	def test_case_sumShift_4(self):
		self.assertEqual(sumShift([0,1],[0,3]),[[0,3],0])
		
	def test_case_answer_1(self):
		self.assertEqual(answer(case1[0]),case1[-1])
		
	def test_case_answer_1(self):
		self.assertEqual(answer(case2[0]),case2[-1])

suite = unittest.TestLoader().loadTestsFromTestCase(ZombitTest)
unittest.TextTestRunner(verbosity=2).run(suite)
           
 
