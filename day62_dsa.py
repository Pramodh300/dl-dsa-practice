#Two Sum In Sorted Array
def two_sum(arr,target):

    left=0

    right=len(arr)-1


    while left<right:


        total=arr[left]+arr[right]


        if total==target:

            return [
                left,
                right
            ]


        elif total<target:

            left+=1


        else:

            right-=1


    return -1



arr=[1,2,3,4,6]


print(
two_sum(arr,6)
)


#Reverse an Array
def reverse(arr):

    left=0

    right=len(arr)-1


    while left<right:


        arr[left],arr[right]=(
            arr[right],
            arr[left]
        )


        left+=1

        right-=1



arr=[1,2,3,4,5]


reverse(arr)


print(arr)



#Remove Duplicates From Sorted Array
def remove_duplicates(nums):

    slow=0


    for fast in range(1,len(nums)):


        if nums[fast]!=nums[slow]:


            slow+=1


            nums[slow]=nums[fast]


    return slow+1



nums=[1,1,2,2,3]


length=remove_duplicates(nums)


print(
nums[:length]
)


#Container With Most Water
def max_area(height):

    left=0

    right=len(height)-1


    answer=0


    while left<right:


        area=min(
            height[left],
            height[right]
        )*(right-left)


        answer=max(
            answer,
            area
        )


        if height[left]<height[right]:

            left+=1

        else:

            right-=1


    return answer



print(
max_area(
[1,8,6,2,5,4,8,3,7]
)
)