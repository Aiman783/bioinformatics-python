# Problem: Weird or Not Weird
# Given an integer n,print "Weird" or "Not Weird"
# based on the given conditions.
n = int(input().strip())
if n %2 != 0:
        print("Weird")
elif 2 <= n <= 5:
        print("Not Weird")
elif 6 <=n <=20:
        print("Weird")
else:
        print("Not Weird")
        
