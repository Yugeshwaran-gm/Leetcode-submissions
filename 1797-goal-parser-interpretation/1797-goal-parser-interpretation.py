class Solution(object):
    def interpret(self, command):
        # command.replace("()","o")
        command=command.replace("()", "o").replace("(","").replace(")","")
        print(command)
        return command