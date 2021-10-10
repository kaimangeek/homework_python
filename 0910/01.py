def polindrome(str):
    if str == str[::-1]:
        return("Yes")
    else:
        return("No")

print(polindrome('ротор'))