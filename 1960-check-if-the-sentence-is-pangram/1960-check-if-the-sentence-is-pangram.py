class Solution(object):
    def checkIfPangram(self, s):
        fl=True
        ase=set(string.ascii_lowercase)
        for w in ase:
            if w not in s:
                fl=False
                break
        return fl