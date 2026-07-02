#Check Whether a Number is Even or Odd Using Bitwise AND
def check_even_odd(num):
    if num & 1:
        print(f"{num} is Odd")
    else:
        print(f"{num} is Even")


check_even_odd(10)
check_even_odd(15)


#Find the Unique Element Using XOR
def find_unique(nums):
    result = 0

    for num in nums:
        result ^= num

    return result


nums = [2, 3, 4, 3, 2]

print("Unique Element:", find_unique(nums))



#Check Whether a Number is a Power of Two
def is_power_of_two(n):
    if n <= 0:
        return False

    return (n & (n - 1)) == 0


print(is_power_of_two(8))
print(is_power_of_two(10))



#Count the Number of Set Bits (1's)
def count_set_bits(n):
    count = 0

    while n > 0:
        count += (n & 1)
        n >>= 1

    return count


print(count_set_bits(13))