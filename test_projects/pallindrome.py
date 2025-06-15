try:
    check_list = ["12311racecar", "12311level", "world"]
    result = []
    for user_input in check_list:  
        # Check if the string is a palindrome
        reversed_str = ""
        for i in range(len(user_input)-1, -1, -1):
            reversed_str += user_input[i]
        if user_input == reversed_str:
            result.append(user_input)
            print(f"{user_input} is a Palindrome")
        else:
            print(f"{user_input} is Not a Palindrome")
    if result == []:
        print("No Palindromes found")
    else:
        print("Palindromes found:", result)
except Exception as e:
        print(f"An error occurred: {e}")