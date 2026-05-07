while True:
    user_input = input("In: (eg:- 3 2 8 1)")
    nums = user_input.split()
    lcheck = 0
    t = len(nums) - 1
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(nums)), nums, color="blue")

    while True:
        for n in range(t):
            if(nums[n] >= nums[n+1]):
                nums[n],nums[n+1] = nums[n+1],nums[n]
                swap_state = True
            elif(lcheck > 500):
                swap_state = False
            else:
                lcheck += 1
        if(swap_state == False):
            break
    print(nums)
