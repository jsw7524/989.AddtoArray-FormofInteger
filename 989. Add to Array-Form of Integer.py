import math
class Solution(object):
    def addToArrayForm(self, A, K):
        #prepare
        digitLength=max(math.ceil(math.log10(K+1)),len(A))
        A.reverse()
        arrayK=[0]*digitLength
        tmp=K
        for i in range(digitLength):
            arrayK[i]=tmp%10
            tmp//=10
        while len(A) < digitLength:
            A.append(0)
        # Add
        answer=[]
        carrier=0
        for i in range(digitLength):
            if ((arrayK[i] + A[i] + carrier)>= 10):
                answer.append((arrayK[i] + A[i] + carrier)%10)
                carrier=1
            else:
                answer.append((arrayK[i] + A[i] + carrier))
                carrier=0
        #Check carrier & reverse
        if carrier == 1:
            answer.append(1)
        answer.reverse()
        return answer

sln=Solution()
assert [1,2,3,4]==sln.addToArrayForm(A = [1,2,0,0], K = 34)
assert [1,0,0]==sln.addToArrayForm(A = [9,9], K = 1)
assert [1,0,0,0,0,0,0,0,0,0,0]==sln.addToArrayForm(A = [9,9,9,9,9,9,9,9,9,9], K = 1)
assert [1,0,2,1]==sln.addToArrayForm(A = [2,1,5], K = 806)
assert [4,5,5]==sln.addToArrayForm(A = [2,7,4], K = 181)
assert [2,3]==sln.addToArrayForm(A = [0], K = 23)
assert [0]==sln.addToArrayForm(A = [0], K = 0)
assert [2,3]==sln.addToArrayForm(A = [0], K = 23)
assert [2,3]==sln.addToArrayForm(A = [2,3], K = 0)
assert [1,0,0,0,0]==sln.addToArrayForm([0],10000)
