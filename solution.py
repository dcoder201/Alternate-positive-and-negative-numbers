#User function Template for python3
from itertools import zip_longest
class Solution:
    def rearrange(self,arr, n):
        # code here
        res=[]
        pos=[x for x in arr if x>=0]
        neg=[y for y in arr if y<0]
        arr.clear()
        for i , j in zip_longest(pos,neg):
            if i!=None:
                arr.append(i)
            if j!=None:
                arr.append(j)
        return(arr)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends
