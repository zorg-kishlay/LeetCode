class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        versions1 = version1.split(".")
        versions2 = version2.split(".")
        i, j = 0, 0
        while i < len(versions1) and j < len(versions2):
            if int(versions1[i]) > int(versions2[j]):
                return 1
            elif int(versions1[i]) < int(versions2[j]):
                return -1
            else:
                i += 1
                j += 1

        while i < len(versions1):
            if int(versions1[i]) == 0:
                i += 1
                continue

            return 1
        
        while j < len(versions2):
            if int(versions2[j]) == 0:
                j += 1
                continue

            return -1
        
        return 0