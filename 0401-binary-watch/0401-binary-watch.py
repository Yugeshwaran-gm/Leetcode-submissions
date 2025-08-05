class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        time=[]
        for h in range (12):
            for m in range(60):
                hours=bin(h).count('1')
                mins=bin(m).count('1')
                if hours+mins==turnedOn:
                    time.append(f"{h}:{m:02d}")
        return time