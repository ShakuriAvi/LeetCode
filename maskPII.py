'''
05\06\24

831. Masking Personal Information

https://leetcode.com/problems/masking-personal-information/description/

String

medium

Accepted
19.2K
Submissions
39.5K
Acceptance Rate
48.6%

Memory
16.52
MB
Beats
39.81%
of users with Python3

Runtime
33
ms
Beats
70.87%
of users with Python3
'''
class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            return self.make_new_email(s)
        return self.make_new_number(s)

    def make_new_email(self, s: str) -> str:
        email_split = s.split("@")
        name, domain = email_split[0].lower(), email_split[1].lower()
        return f"{name[0]}*****{name[-1]}@{domain}"

    def make_new_number(self, s: str) -> str:
        country_code_digit = ''
        phone_number = ''

        for digit in s:
            if digit.isnumeric():
                phone_number += digit

        len_phone_number = len(phone_number)

        if len_phone_number > 10:
            country_code_digit = "+" + ("*" * (len_phone_number - 10)) + "-"

        masked_phone_number = '***-***-'
        last_four_phone_number = phone_number[-4:]
        return f"{country_code_digit}{masked_phone_number}{last_four_phone_number}"

if __name__ == '__main__':
    sol = Solution()
    print(sol.maskPII("LeetCode@LeetCode.com"))
    print(sol.maskPII("AB@qq.com"))
    print(sol.maskPII("1(234)567-89053"))
