
bangla = int(input("Enter Your marks for Bangla :"))
English = int(input("Enter Your marks for English :"))
Math = int(input("Enter Your marks for Math :"))
Science = int(input("Enter Your marks for Science :"))


avarage = (bangla + English + Math + Science) / 4

if (avarage < 41): 
    grade = "F"
elif(avarage < 61):
    grade = "D"
elif(avarage < 71):
    grade = "C"
elif(avarage < 81):
    grade = "B"
elif(avarage < 91):
    grade = "A"
else:
    grade = "A+"


if( grade != "F"):
    print("Your Grad is :", grade)
else:
    print("You Fail")
