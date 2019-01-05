class Solution(object):
    def reverse(self, x):
        if (x > 2 ** 31 - 1) or (x < - 2 ** 31):
            return 0
        else:
            
            stringx = str(x)
            listx = list(stringx)
            if x < 0:
                listx.pop(0)

            
            
            reverse_string = list(reversed(listx))
            print(reverse_string)

            reverse_num = int(''.join(reverse_string))
            print(reverse_num)
        
            if x < 0:
                if -reverse_num < -2 ** 31:
                    return 0
                else:
                    return -reverse_num

            else:
                if reverse_num > 2** 31 -1:
                    return 0
                else:
                    return reverse_num

        

        """
        :type x: int
        :rtype: int
        """
        