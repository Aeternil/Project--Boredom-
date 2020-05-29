print ("Wellcome to your post-quarantine activity manager!")
while (True):
    print("You can 'add' a new activity, 'edit' an existing activity, 'delete' an activity, 'search' for anything specific or 'exit'")
    print ("What would you like to do?")
    ans = str(input())
    if (ans == "exit"):
        print("Closing down")
        break
    elif (ans == "add"):
        print("What do you want to do after quarantine?")
        ans = str(input())
        
    elif (ans == "edit"):
        pass
    elif (ans == "delete"):
        pass
    elif (ans == "search"):
        pass
    else:     
        print("It seems your input was incorrect, please try again")
