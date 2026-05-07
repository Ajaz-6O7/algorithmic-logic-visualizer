while True:
    user_input = input("In: (eg:- 3 2 8 1)")
    nums = user_input.split()
    swap_state = True
    lcheck = 0
    t = len(nums) - 1

    while swap_state == True:
        for n in range(t):
            if(nums[n] >= nums[n+1]):
                nums[n],nums[n+1] = nums[n+1],nums[n]
                swap_state = True
            elif(lcheck > 500):
                swap_state = False
            else:
                lcheck += 1
    print(nums)
