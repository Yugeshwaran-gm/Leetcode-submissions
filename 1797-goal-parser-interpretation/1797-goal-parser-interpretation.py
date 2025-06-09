class Solution(object):
    def interpret(self, command):
        o=False
        ou=""
        for c in command:
            if c=="G":
                ou+="G"
            elif c=="(":
                o=True
            elif o==True and c==")":
                ou+="o"
                o=False
            elif o==True and c=="a":
                ou+="al"
                o=False
            else:
                pass
        print(ou)
        return ou