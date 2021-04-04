1 num = int(input("Enter any number : "))
2 if num > 1:
    for i in range(2, num):
4	        if (num % i) == 0:
5	            print(num, "is NOT a prime number")
6	            break
7	  else:
8	        print(num, "is a PRIME number")
9 elif num == 0 or 1:
10	    print(num, "is a neither prime NOR composite number")
11 else:
12	    print(num, "is NOT a prime number it is a COMPOSITE number")