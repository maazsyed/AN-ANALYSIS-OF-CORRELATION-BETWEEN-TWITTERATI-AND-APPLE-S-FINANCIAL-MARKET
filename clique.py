# Enter your code here. Read input from STDIN. Print output to STDOUT
def turan(n,r):
	"""
	Turan's theorem gives us an upper bound on the number of edges a graph can have if we wish that it should not have a clique of size x
	"""
	return 0.5 * (n ** 2 - (n % r) * (n / r + 1) ** 2 - (r - (n % r)) * (n / r) ** 2)

def solveClique(n,m):
	lowerLimit = 0
	higherLimit = n
	while lowerLimit + 1 < higherLimit:
		mid = (lowerLimit+higherLimit) / 2
		turanEdge = turan(n,mid)

		if turanEdge < m:
			lowerLimit = mid
		else:
			higherLimit = mid

	return higherLimit

if __name__ == '__main__':
	testcases = int(input())
	for i in range(testcases):
		n,m = map( input().strip().split(' '),int )
		print (solveClique(n,m))