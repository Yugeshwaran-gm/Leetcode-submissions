class Solution(object):
    def defangIPaddr(self, adr):
        adr=adr.replace(".","[.]")
        return adr