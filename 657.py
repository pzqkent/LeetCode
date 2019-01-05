class Solution(object):
    def judgeCircle(self, moves):
        originx = 0
        originy = 0
        
        for letter in moves:
            if letter == 'U':
                originy += 1
            elif letter == 'D':
                originy -= 1
            elif letter == 'L':
                originx -= 1
            else:
                
                originx += 1
        if originx == 0 and originy == 0:
            return True
        else:
            return False
        """
        :type moves: str
        :rtype: bool
        """
        