class Solution(object):
    def splitPainting(self, segments):
        """
        :type segments: List[List[int]]
        :rtype: List[List[int]]
        """
        starts = {}
        ends = {}

        for seg in segments:
            if seg[0] in starts:
                starts[seg[0]] += seg[2]
            else:
                starts[seg[0]] = seg[2]

            if seg[1] in ends:
                ends[seg[1]] += seg[2]
            else:
                ends[seg[1]] = seg[2]

        startKeys = []
        for k in starts:
            startKeys.append(k)
        startKeys.sort()
        endKeys = []
        for k in ends:
            endKeys.append(k)
        endKeys.sort()

        sKI = 0
        eKI = 0

        total = 0
        last = 1 # last point of change
        
        fin = []

        while eKI < len(endKeys):
            if sKI >= len(startKeys):
                fin.append([last, endKeys[eKI], total])
                last = endKeys[eKI]
                total -= ends[endKeys[eKI]]
                eKI += 1
            elif startKeys[sKI] == endKeys[eKI]:
                tempTotal = total
                total += starts[startKeys[sKI]]
                total -= ends[endKeys[eKI]]
                fin.append([last, startKeys[sKI], tempTotal])
                last = startKeys[sKI]
                sKI += 1
                eKI += 1
            elif startKeys[sKI] < endKeys[eKI]:
                if total != 0:
                    fin.append([last, startKeys[sKI], total])
                last = startKeys[sKI]
                total += starts[startKeys[sKI]]
                sKI += 1
            else:
                fin.append([last, endKeys[eKI], total])
                last = endKeys[eKI]
                total -= ends[endKeys[eKI]]
                eKI += 1

        return fin        

        