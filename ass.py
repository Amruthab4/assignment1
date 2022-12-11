#question 1
assignment1=0
assignment2=0
assignment3=0
assignment4=0
assignment5=0
assignment1=int(input("marks of assignment1"))
assignment2=int(input("marks of assignment2"))
assignment3=int(input("marks of assignment3"))
assignment4=int(input("marks of assignment4"))
assignment5=int(input("marks of assignment5"))
if((assignment1<=0) or (assignment2<=0) or (assignment3<=0) or (assignment4<=0) or (assignment5<=0)):
    print("please enter a positive value")
else:
    print("Total Assignment marks are")
    totalMarks=assignment1+assignment2+assignment3+assignment4+assignment5
    print(totalMarks)

#2nd question
car={
    "MG":"blue",
    "BENZ":"black",
    "AUDI":"white",
    "BMW":"red",
    "Kia":"pink"
}
for brand in car:
    print(brand)
for colour in car:
    print(car[colour])
