class Solution:
    def romanToInt(self, s: str) -> int:
        onecounter = 0
        tencounter = 0
        hundredcounter = 0
        totalsum = 0
        for i in s:
            if i == 'I':
                onecounter += 1
            elif i == 'V':
                totalsum += 5
                if onecounter != 0:
                    onecounter -= 2
            elif i == 'X':
                tencounter += 10
                if onecounter != 0:
                    onecounter -= 2
            elif i == 'L':
                totalsum += 50
                if tencounter != 0:
                    tencounter -= 20
            elif i == 'C':
                hundredcounter += 100
                if tencounter != 0:
                    tencounter -= 20
            elif i == 'D':
                totalsum += 500
                if hundredcounter != 0:
                    hundredcounter -= 200
            elif i == 'M':
                totalsum += 1000
                if hundredcounter != 0:
                    hundredcounter -= 200
        return totalsum + onecounter + tencounter + hundredcounter

