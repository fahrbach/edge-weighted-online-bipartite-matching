from mpmath import mp

mp.dps = 1000

k_max = 8
kappa = mp.mpf(1.5)
gamma = mp.mpf(1)/mp.mpf(16)
Gamma = mp.mpf(0.50503484)

a = [
	0.24748256,
	0.13684883,
	0.06415997,
	0.03009310,
	0.01413332,
	0.00666576,
	0.00318572,
	0.00158503,
	0.00088057
]
b = [
	0.25251744,
	0.12877617,
	0.06035174,
	0.02827176,
	0.01322521,
	0.00615855,
	0.00282566,
	0.00123280,
	0.00044028
]

a = list(map(mp.mpf, a))
b = list(map(mp.mpf, b))

def constraint_1():
	print('Constraint 1:')
	for k in range(k_max + 1):
		lhs = kappa*b[k]
		for l in range(k, k_max + 1):
			lhs += a[l]
		rhs = pow(2, -k)
		exponent = max(k - 1, 0)
		rhs *= pow(1 - gamma, exponent)
		print(' -', k, lhs, rhs, lhs <= rhs)
		if lhs > rhs:
			print('FAIL')
	print()
		
def constraint_2():
	print('Constraint 2:')
	lhs = a[0] + b[0]
	rhs = 0.5
	print(' -', lhs, rhs, lhs <= rhs)
	if lhs > rhs:
		print('FAIL')
	print()	

def constraint_3():
	print('Constraint 3:')
	for k in range(1, k_max + 1):
		lhs = a[k] + b[k]
		rhs = pow(mp.mpf(2), -k - 1) * pow(mp.mpf(1 - gamma), k-1) * (1 + gamma)
		print(' -', k, lhs, rhs, lhs <= rhs)
		if lhs > rhs:
			print('FAIL')
	print()
		
def constraint_4():
	print('Constraint 4:')
	lhs = a[0]
	rhs = gamma/2
	print(' -', lhs, rhs, lhs >= rhs)
	if lhs < rhs:
		print('FAIL')
	print()

def constraint_5():
	print('Constraint 5:')
	lhs = 0
	for l in range(k_max + 1):
		lhs += a[l]
	rhs = Gamma
	print(' -', lhs, rhs, lhs >= rhs)
	if lhs < rhs:
		print('FAIL')
	print()
		
def constraint_6():
	print('Constraint 6:')
	for k in range(1, k_max + 1):
		lhs = 0
		for l in range(k):
			lhs += a[l]
		lhs += 2*b[k]
		rhs = Gamma
		print(' -', k, lhs, rhs, lhs >= rhs)
		if lhs < rhs:
			print('FAIL')
	print()

def constraint_7():
	print('Constraint 7:')
	for k in range(1, k_max + 1):
		lhs = 0
		for l in range(k + 1):
			lhs += a[l]
		lhs += kappa*b[k]
		rhs = Gamma
		print(' -', k, lhs, rhs, lhs >= rhs)
		if lhs < rhs:
			print('FAIL')
	print()

def main():
	constraint_1()
	constraint_2()
	constraint_3()
	constraint_4()
	constraint_5()
	constraint_6()
	constraint_7()
	
main()
