def scene1():
    print("""   WELCOME TO CASSEY'S ADVENTURE ON HER WAY TO SCHOOL!
            Cassey on her first day of school. She was so excited! As she was walking going to school,
            she found an old lady asking for food.
            Will Cassey help her or will she continue on her way to school?

            Pick your choice: HELP or IGNORE?
            """)
    choice = input()
    if(choice.upper()=="HELP"):
        scene2_help()
    elif(choice.upper()=="IGNORE"):
        scene2_ignore()
    else:
        print("ENTER YOUR CHOICE! Help or Ignore?")

def scene2_help():
    print("""Cassey decides to help the old lady and give some of her packed lunch.
    
                Pick your choice: SHARE or GO TO SCHOOL?
            """)
    choice = input()
    if(choice.upper()=="SHARE"):
        print("Good job on your choice! Cassey give her food to the lady.")
        scene3_choice1()
    elif(choice.upper()=="GO TO SCHOOL"):
        print("GO TO SCHOOL")
        scene3_choice2()
    else:
        print("ENTER YOUR CHOICE! SHARE or GO TO SCHOOL")

def scene2_ignore():
    print("Cassey just went on her way to school as she was so excited on her first day!")
    choice = input()
    if(choice.upper()=="SHARE"):
        print("SHARE")
        scene3_choice1()
    elif(choice.upper()=="GO TO SCHOOL"):
        print("GO TO SCHOOL")
        scene3_choice2()
    else:
        print("ENTER YOUR CHOICE! SHARE OR GO TO SCHOOL")

def scene3_choice1():
   print("Cassey decided to share her food to the lady.")

def scene3_choice2():
    print("Cassey just ignore the lady because she was so focused on going to school.")

scene1()
