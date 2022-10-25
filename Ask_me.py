from unicodedata import name


name=input("what is your name? ")
name=name.title()
print(" Oh Hello,",name)
if name == "Isaac" or name == "Omega":
    print("Oh hello,",name) 
    print("Stay well dear," ,name)
else:
    print("Hello,friends......")
    age=int(input("Hello,can i know year age please? "))
    if age< 15:
        print("you have not qualified.")
   elif age> 18 and age,<25:
            print("You are the one we want.")
            elif age> 25 and age,<35:
                print("you should be in field now")
                elif age <40 and age, < 60:
                    print("youcant qualify")
                    else:
                        print("Goodbye,",name)
                        print("you are" ,age,"years old.")
                        print("you are not human")