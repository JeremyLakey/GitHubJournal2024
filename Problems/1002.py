class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        m = None
        

        for word in words:
            t = {}
            for c in word:
                if c in t:
                    t[c] += 1
                else:
                    t[c] = 1
            
            if m == None:
                m = t
            else:
                for key in m:
                    if key in t:
                        m[key] = min(m[key], t[key])
                    else:
                        m[key] = 0
                for key in t:
                    if key in m:
                        m[key] = min(m[key], t[key])

        fin = []

        for key in m:
            while m[key] > 0:
                fin.append(key)
                m[key] -= 1
        return fin
        