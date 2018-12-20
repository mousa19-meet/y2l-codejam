
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 31 + 2 
nums = [ 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578]
def termmy(nterms):

  if nterms <= 0:
    print("Plese enter a positive integer")
  else:
    print("Fibonacci sequence:")
    for i in range(nterms):
      print(recur_fibo(i))
    return recur_fibo(i)

print(nums)
total = 0
for i in nums:
  if i % 2 ==0:
    total = total + i
    print(total)