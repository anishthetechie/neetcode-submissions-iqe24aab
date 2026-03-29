class Solution:
    def isPalindrome(self, s: str) -> bool:

        #res = ''
        #for ch in s:
        #    if ch.isalnum():  # O(N^2)
        #        res += ch    # due to this

        #res = res.lower()

        res = []

        for ch in s:
            if ch.isalnum():
                res.append(ch.lower())


        left = 0
        right = len(res) - 1

        while left <= right:
            if res[left] != res[right]:
                return False
            else:
                left += 1
                right -= 1

        return True