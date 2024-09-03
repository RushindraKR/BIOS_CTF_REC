import math

def is_sum_of_squares(n):
    left = 0
    right = int(math.sqrt(n))

    while left <= right:
        current_sum = left * left + right * right
        
        if current_sum == n:
            return True
        elif current_sum < n:
            left += 1
        else:
            right -= 1
    
    return False
n = int(input("Enter the number: "))
print(is_sum_of_squares(n))
