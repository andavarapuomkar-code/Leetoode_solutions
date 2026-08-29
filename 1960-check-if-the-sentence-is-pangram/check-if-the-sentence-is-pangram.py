class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        '''
        a=len(set(sentence))
        if a==26:
            return True
        else:
            return False
        '''
        
        a=[]
        for i in sentence:
            if i not in a:
                a.append(i)
        if len(a)==26:
            return True
        else:
            return False
        
        