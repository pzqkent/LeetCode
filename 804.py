class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        maps = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = ''
        result1 = []
        result2 = []
        dic1=dict(zip(letter, maps))
        # print(dic1)
        # print(words[0])
        # for i in range(len(words)):
        #     for j in range(len(words[i])):
        #         result = result + dic1[words[i][j]]
        #     result1.append(result)
        #     result = ''
        for word in words:
            for letter in word:
                result += dic1[letter]
            result1.append(result)
            result = ''
        # print(result1)
        for item in result1:
            if item not in result2:
                result2.append(item)
        # for item in result1:
        #     if item in result2:
        #         pass
        #     else:
        #         result2.append(item)
        return len(result2)