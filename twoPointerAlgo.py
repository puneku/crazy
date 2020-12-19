'''Problem : for a given array A[n] of n element. Find a triplete whose sum is 0 with time complexity of order O(n**2)'''

def findTripleteSum(A):
	# writing a double pointer algorithm for two addition of two element.
	A.sort()
	for k in range(len(A)-2):
		if doubleSum(A,-A[k]):
			return True
	return False

def doubleSum(a,x):
	i , j = 0 , len(a)-1
	while i<j:
		if a[i]+a[j]<x:
			i+=1
		elif a[i]+a[j]>x:
			j-=1
		else:
			return True
	return False

a = [-4,-3,-2,-1,1,2,3,4,5]
if findTripleteSum(a):
    print("exists")
else:
    print("Does not exist")