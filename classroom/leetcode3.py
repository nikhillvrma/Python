class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = []
        maxlen = 0
        for ch in s:
            if ch in st:
                while ch in st:
                    st.pop(0)
            st.append(ch)
            maxlen = max(maxlen, len(st))
        return maxlen
