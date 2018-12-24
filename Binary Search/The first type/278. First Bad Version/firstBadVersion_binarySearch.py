
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            if isBadVersion(1) == False:
                return 2
            else:
                return 1
        
        start, end = 1, n
        while start + 1 < end:
            mid = (start + end) / 2
            if isBadVersion(mid) == False:
                start = mid
            else:
                end = mid
        if isBadVersion(start) == True:
            return start
        else:
            return end
                
