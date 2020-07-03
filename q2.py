#There are two sorted arrays nums1 and nums2 of size m and n respectively.
#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#You may assume nums1 and nums2 cannot be both empty
def getMedian( ar1, ar2 , n): 
    i = 0 
    j = 0
    m1 = 0
    m2 = 0

    count = 0
    while count < n + 1: 
        count += 1

        if i == n: 
            m1 = m2 
            m2 = ar2[0] 
            break

        elif j == n: 
            m1 = m2 
            m2 = ar1[0] 
            break

        if ar1[i] <= ar2[j]: 
            m1 = m2 
            m2 = ar1[i] 
            i += 1
        else: 
            m1 = m2 
            m2 = ar2[j] 
            j += 1
    return (m1 + m2)/2
ar1 = [1, 2] 
ar2 = [3,4] 
n1 = len(ar1) 
n2 = len(ar2) 
if n1 == n2: 
    print("Median is ", getMedian(ar1, ar2, n1)) 
else: 
    print("Doesn't work for arrays of unequal size")
