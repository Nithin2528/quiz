print("Welcome to the quiz game")

ans = input("Are you ready to play the quiz (yes/no) : ")

score = 0
total_q = 4

if ans.lower() == "yes" :
    ans = input("Q1 . What is the nickname of nithin? : ")
    if ans.lower() == "neo" :
        score += 1
        print("You are correct")
    else:
        print("Nope You Are Wrong")


    ans = input("Q2 . What is the age of Nithin? : ")
    if ans == '18':
        score += 1
        print("Good You Got It.")
    else:
        print("Im sorry you are incorrect")


    ans = input("Q3 . Do you know what Nithin Loves more? : ")
    if ans.lower() == 'games':
        score += 1
        print("Great You know a lot")
    else:
        print("OOOPs.........ur wrong")


    ans = input("Q4 . Guess whats Nithins fav food? : ")
    if ans.lower() == 'burger':
        score += 1
        print("Impressive")
    else:
        print("Nope thats wrong")


    ans = input("Q5 . The Final Question Guess whom Nithin love the most? : ")
    if ans.lower() == 'granny' or ans.lower() == 'mom':
        score += 1
        print("youve got it ")
    else:
        print("Nope too bad")


    print("THANK YOU FOR PLAYING THE NEO QUIZ" , score , "questions correct")
    mark = (score/total_q) * 100
    print("Marks: ", mark)
    print('Good Bye')

else:
    print("FUCK OFF")
    
      
    
    
