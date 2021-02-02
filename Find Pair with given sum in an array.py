#find pair with given sum in the array
#native approch
def findpair(A,sum):
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            if A[i]+A[j]==sum:
                print("Pair found at index",i,"and",j)
                return
            
            
            
            
    print("Pair not found")
if __name__=='__main__':
    A = [2,3,5,4,7,8,2,3,4,5,6,7]
    sum = 10
    findpair(A,sum)    
    
    
    
#O(nlog(n))    solution using Sorting
    
    def find(A,sum):
        A.sort()
        (low, high) = (0, len(A)-1)
        
        while low < high:
                if A[low]+A[high] == sum:
                    print("Pair found")
                    return
                if A[low] + A[high] < sum:
                    low = low + 1
                else:
                    high = high = high - 1
        print("pair not found")
    
    
    if __name__ == '__main__':
        A = [1,4,2,8,7,9,5,4]
        sum = 18
        
        find(A,sum)
        
        
#O(n)solution Hashing
def ffind(A,sum):
    dict = {}
    for i,e in enumerate(A):
        if sum - e in dict:
            print("Pair found at index",dict.get(sum-e),"and",i)
            return
        dict[e]=i
        print("Pair not found")
if __name__ == '__main__':
    A = [5,6,7,8,4,54,3,34,54,8]
    sum = 88
                    
    ffind(A,sum)
    
    