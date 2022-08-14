def number_is_polindrom(n):
    return str(n) == str(n)[::-1]
       
n = int(input("Enter number: "))
print(number_is_polindrom(n))