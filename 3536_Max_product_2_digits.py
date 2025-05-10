class Solution:
    def maxProduct(self, n: int) -> int:
      x = list(str(n))
      i = 0
      for i in range(len(x) - 1):
        for i in range(len(x) - 1):
           if x[i] > x[i+1]:
             x[i], x[i+1] = x[i+1], x[i]
    


      x1 = int(x[-1])
      x2 = int(x[-2])
      return x1 * x2
