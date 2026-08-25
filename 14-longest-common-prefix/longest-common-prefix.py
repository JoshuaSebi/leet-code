class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = 1

        while True:
            flag = False

            for i in range(1, len(strs)):
                st1 = strs[i - 1][0:pref]
                st2 = strs[i][0:pref]

                if st1 != st2:
                    flag = True
                    break

            if flag:
                return strs[0][0:pref - 1]
            if pref >= len(strs[0]):
                return strs[0]

            pref += 1