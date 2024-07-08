class Solution:
    def romanToInt(self, s: str) -> int:
        rom_to_int = {
            'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000
        }
        intValue = 0
        i = 0
        while i < len(s):
            #Substration case
            if i + 1 < len(s) and rom_to_int[s[i]] < rom_to_int[s[i+1]]:
                intValue += rom_to_int[s[i+1]] - rom_to_int[s[i]]
                i += 2
            # Additon case
            else:
                intValue += rom_to_int[s[i]]
                i += 1
        return intValue