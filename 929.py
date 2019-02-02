class Solution:
    def numUniqueEmails(self, emails):
        result = set()
        for email in emails:
            # if '@'
            email_left = email[:email.find('@')]
            email_right = email[email.find('@')+1:]
            if '.'in email_left:
                email_left = email_left[:email.find('.')]
            if '+' in email_left:
                email_left = email_left[:email.find('+')]
            
            result.add(email_left+'@'+email_right)
        # print(result) 
        return len(result)
        """
        :type emails: List[str]
        :rtype: int
        """
        