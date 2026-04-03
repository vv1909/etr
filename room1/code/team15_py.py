def sum_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    
    return total

try:
    num = int(input("Enter the number: "))
    result = sum_digits(num)
    print(f"Sum of digits: {result}")

except:
    print("Please enter a valid number")