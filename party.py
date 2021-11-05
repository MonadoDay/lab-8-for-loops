userinput = prompt("Let's party! How long till the party?"):
usernum = Int(userinput)
if usernum < 1:
    print("PARTY NOW!!!")
else:
    for (i = usernum: i >= 1: i = i - 1):
        print(i)
    print("PARTY TIME!!!"):
