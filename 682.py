class Solution(object):
    def calPoints(self, ops):
        valid_round = [0,0]
        total = 0
        for letter in ops:
            this_round = 0
            if letter == '+':
                this_round = valid_round[-1] + valid_round[-2]
                total += this_round
                valid_round.append(this_round)
            elif letter == 'D':
                this_round = 2 * valid_round[-1]
                total += this_round
                valid_round.append(this_round)
            elif letter == 'C':
                total = total - valid_round[-1]
                valid_round.pop(-1)
                
            else:
                this_round = int(letter)
                total += this_round
                valid_round.append(this_round)
            # print total
        return total   
                
        """
        :type ops: List[str]
        :rtype: int
        """
        