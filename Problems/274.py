class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        i = len(citations) - 1
        t = 0
        
        bsf = 0
        while i >= 0:
            if i > 0:
                j = i - 1
                v = citations[i]
                c = 1
                while j >= 0:
                    if citations[j] == v:
                        c += 1
                        j -= 1
                    else:
                        break

                if c + t >= v:
                    bsf = max(bsf, v)
                i -= c            
                t += c
            else:
                i -= 1
                t += 1
               
        i = 0
        while i < len(citations):

            if citations[i] >= t:
                bsf = max(bsf, t)
            i += 1
            t -= 1


        return bsf
        