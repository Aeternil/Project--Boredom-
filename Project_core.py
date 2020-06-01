import openpyxl
data = openpyxl.load_workbook('data.xlsx')
Sheet = data.active
print ("Wellcome to your post-quarantine activity manager!")
while (True):
    print("You can 'add' a new activity, 'edit' an existing activity, 'delete' an activity, 'search' for anything specific or 'exit'")
    print ("What would you like to do?")
    ans = str(input())
    if (ans == "exit"):
        data.save('data.xlsx')
        print("Closing down")
        break
    
    elif (ans == "add"):
        print("What do you want to do after quarantine?")
        ans = str(input())
        flag = False
        for cell in Sheet['A']:
            if (cell.value == ans):
                flag = True
                break
        if (flag):
            print("This activity is already in the database")
        else:
            Sheet['A'+ str(len(Sheet['A'])+1)] = ans
            print("Data saved")
    elif (ans == "edit"):
        pass
    elif (ans == "delete"):
        pass
    elif (ans == "search"):
        pass
    else:     
        print("It seems your input was incorrect, please try again")
