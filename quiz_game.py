print("welcome to computer quiz")

playing = input("do you want to play :)")

if playing.lower() != "yes":
    quit()

print("okay let's paly")
score = 0

answer = input("what does cpu stands for ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does gpu stands for ")
if answer.lower() == "graphical processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does ram stands for ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does psu stands for ")
if answer.lower() == "power supply":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("you got " + str(score) + " question correct")