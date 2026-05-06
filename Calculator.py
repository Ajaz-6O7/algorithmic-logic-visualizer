while True:
    user_input = input("Input: ")

    parts = user_input.split()

    x = float(parts[0])
    operator = parts[1]
    y = float(parts[2])

    if(operator == "/"):        
        if(y != 0):
            ans = x/y

        else:
            ans = "error"
    elif(operator == "*"):
        ans = x*y
    elif(operator == "+"):
        ans = x + y
    elif(operator == "-"): 
        ans = x - y
    else:
        ans = "error"

    print("Answer: " + str(ans))
