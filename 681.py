class Solution:
    def nextClosestTime(self, time):
        result = start = 60 * int(time[:2])+int(time[3:])
        elapsed = 24 * 60
        allowed  = [int(x) for x in time if x!=':']
        # print(list(itertools.product(allowed,repeat = 4)))
        for h1,h2,m1,m2 in itertools.product(allowed,repeat = 4):
            hours,mins = 10 * h1 + h2, 10 * m1 + m2
            if hours < 24 and mins < 60:
                current_time = hours * 60 + mins
                cand_elapsed = (current_time - start) % (24 * 60)
                if 0 < cand_elapsed < elapsed:
                    result = current_time
                    elapsed = cand_elapsed
        print(result)
        return "{:0>2d}:{:0>2d}".format(*divmod(result,60))
        
        
        
        """
        :type time: str
        :rtype: str
        """
        