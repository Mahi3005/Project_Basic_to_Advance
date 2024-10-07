print("Welcome to my computer Quiz!!")

playing=input("Do you want to play?")

if playing.lower()!='yes':
    quit()

print('Okay lets Play :)')
score= 0

answer=input("what does cpu stands for? ")
if answer.lower()=='central processing unit':
    print('Correct!!')
    score+=1
else:
    print('Incorrect!!')

answer=input("what does gpu stands for? ")
if answer.lower()=='graphics processing unit':
    print('Correct!!')
    score+=1
else:
    print('Incorrect!!')

answer=input("what does RAM stands for? ")
if answer.lower()=='random access memory':
    print('Correct!!')
    score+=1
else:
    print('Incorrect!!')

answer=input("what does PSU stands for? ")
if answer.lower()=='Power Supply':
    print('Correct!!')
    score+=1
else:
    print('Incorrect!!')

print("You got {} out of {} score!".format(score,score+1))
print("Thank you for playing!")