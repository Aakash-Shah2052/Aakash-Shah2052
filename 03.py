while (i>=5)
    print("Next candidates please..")
    skill = input(str(i+1) + " Enter the skills you have.\n")
    if skill == "kubernetes":
        print("Everybody go home we found our developer")
        break
print("done for today")