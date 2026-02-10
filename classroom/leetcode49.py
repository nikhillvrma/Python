class Solution(object):
    def groupAnagrams(self, strs):
        d = {}

        # method 1
        # for _ in strs:
        #     key = tuple(sorted(_))

        #     if key in d:
        #         d[key].append(_)
        #     else:
        #         d[key] = [_]

        # return list(d.values())

        # method 2
        for value in strs:
            data = sorted(value)
            data = "".join(data)
            if data in d:
                d[data].append(value)
            else:
                d[data] = [value]
        return list(d.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
obj = Solution()
r = obj.groupAnagrams(strs)
print(r)
