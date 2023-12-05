class Solution:
    tribonacci_ans = {}
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n ==2:
            return 1
        elif n in Solution.tribonacci_ans:
            return Solution.tribonacci_ans[n]
        elif n not in  Solution.tribonacci_ans:
            ans_1 = self.tribonacci(n -1)
            Solution.tribonacci_ans[n-1] = ans_1

            ans_2 = self.tribonacci(n - 2)
            Solution.tribonacci_ans[n-2] = ans_2

            ans_3 = self.tribonacci(n - 3)
            Solution.tribonacci_ans[n-3] = ans_3

            return ans_1 + ans_2 + ans_3