import pprint

class Palindrome(object):

    def str_to_list(self, payload: str) -> []:
        '''strs = []
            for char in payload:
                if char.isalnum():
                    strs.append(char.lower())'''
        return [i for i in payload if i.isalnum()]


    def isPalindrome(self, ls: []) -> dict:
        '''while len(ls) > 1:
            if ls.pop(0) != ls.pop():'''
        return {"RESULT": False for i in ls if ls.pop(0) != ls.pop()}


