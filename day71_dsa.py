#Valid Palindrome (Two Pointers)
import string

def is_palindrome(text):
    # Keep only letters and digits
    filtered = ""

    for ch in text:
        if ch.isalnum():
            filtered += ch.lower()

    left = 0
    right = len(filtered) - 1

    while left < right:
        if filtered[left] != filtered[right]:
            return False

        left += 1
        right -= 1

    return True


def main():
    text = "A man, a plan, a canal: Panama"

    print("Original String:")
    print(text)

    if is_palindrome(text):
        print("\nPalindrome")
    else:
        print("\nNot Palindrome")


if __name__ == "__main__":
    main()
    
    
#Remove Duplicates from Sorted Array
def remove_duplicates(nums):

    if len(nums) == 0:
        return 0

    slow = 0

    for fast in range(1, len(nums)):

        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


def main():

    nums = [1, 1, 2, 2, 3, 3, 4]

    print("Original Array")
    print(nums)

    length = remove_duplicates(nums)

    print("\nUnique Elements")
    print(nums[:length])

    print("\nLength =", length)


if __name__ == "__main__":
    main()    




#Move Zeroes
def move_zeroes(nums):

    slow = 0

    for fast in range(len(nums)):

        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


def main():

    nums = [0, 1, 0, 3, 12]

    print("Before")
    print(nums)

    move_zeroes(nums)

    print("\nAfter")
    print(nums)


if __name__ == "__main__":
    main()



#Two Sum ||
def two_sum(nums, target):

    left = 0
    right = len(nums) - 1

    while left < right:

        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return left, right

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return -1, -1


def main():

    nums = [2, 7, 11, 15]
    target = 9

    print("Array")
    print(nums)

    left, right = two_sum(nums, target)

    print("\nTarget =", target)
    print("Indices =", left, right)
    print("Numbers =", nums[left], nums[right])


if __name__ == "__main__":
    main()    



#Container With Most Water
def max_area(height):

    left = 0
    right = len(height) - 1

    maximum = 0

    while left < right:

        width = right - left

        current = min(height[left], height[right]) * width

        maximum = max(maximum, current)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maximum


def main():

    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    print("Heights")
    print(heights)

    area = max_area(heights)

    print("\nMaximum Water =", area)


if __name__ == "__main__":
    main()