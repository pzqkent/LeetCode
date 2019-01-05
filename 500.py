class Solution(object):
    def findWords(self, words):
        
        keyboard = ['qwertyuiop','asdfghjkl','zxcvbnm']

        # counter = [0,0,0]
        result = []
        for word in words:
            counter = [0,0,0]
            word1 = word.lower()
            for letter in word1:
                if letter in keyboard[0]:
                    counter[0] += 1
                elif letter in keyboard[1]:
                    counter[1] += 1
                    
                elif letter in keyboard[2]:
                    counter[2] += 1
            # print(counter)
            if len(word) in counter:
                result.append(word)
            # counter = [0,0,0]
        return result
        """
        :type words: List[str]
        :rtype: List[str]
        """
        