'''Problem : for a given array A[n] of n element. Find a triplete whose sum is 0 with time complexity of order O(n*n).'''

f , s = -1 , -1
def findTripleteSum(A):
    # writing a double pointer algorithm for two addition of two element.
    A.sort()
    global f,s
    for k in range(len(A)-1):
        if doubleSum(A,-A[k],k+1):
            return (A[f], A[s],A[k])

def doubleSum(a,x,i):
    j = len(a)-1
    while i<j:
        if a[i]+a[j]<x:
            i+=1
        elif a[i]+a[j]>x:
            j-=1
        else:
            global f,s
            f = i
            s = j
            return True
    return False

a = [-4,-3,-2,-1,1,2,3,4]
if findTripleteSum(a) == None:
    print("No triplete found.")
else:
    print(findTripleteSum(a))
