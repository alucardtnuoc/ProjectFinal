def maximum_grade():
    a = input("Midterm Score Out Of 40,(ex.30) If You Haven't Get The Midterm Score Return - :")
    if a == "-":
        midterm = [0,0]
    
    else:
        midterm = [int(a),40]

    b = input("Final Score Out Of 40,(ex.30) If You Haven't Get The Final Score Return - :")
    if b == "-":
        final = [0,0]
    
    else:
        final = [int(b),40]

    c = input("Homework Score Out Of 20,(ex.15) If You Haven't Get The Homework Score Return - :")
    if c == "-":
        homework = [0,0]

    else:
        homework = [int(c),20]


    score = [(midterm[0]+final[0]+homework[0]),(midterm[1]+final[1]+homework[1])]
    obtainable_score = 100 - int(score[1])
    max_score = obtainable_score + int(score[0])
    if max_score >= 80:
        max_grade = "A"
        m = max_score - 80
    elif max_score >= 75:
        max_grade = "B+"
        m = max_score - 75
    elif max_score >= 70:
        max_grade = "B"
        m = max_score - 70
    elif max_score >= 65:
        max_grade = "C+"
        m = max_score - 65
    elif max_score >= 60:
        max_grade = "C"
        m = max_score - 60
    elif max_score >= 55:
        max_grade = "D+"
        m = max_score - 55
    elif max_score >= 50:
        max_grade = "D"
        m = max_score - 50
    else:
        max_grade = ("F, Please Try Harder Next Year...")
    print("Current Score: " + str(score[0]))
    print("Highest score possible is " + str(max_score))
    print("Highest grade possible is " + max_grade)
    print("Number Of Exceeded Score For This Grade: "+str(m))
    repeat()
    
def minimum_grade():
    a = input("Midterm Score Out Of 40,(ex.30) If You Haven't Get The Midterm Score Return - :")
    if a == "-":
        midterm = [0,0]
    
    else:
        midterm = [int(a),40]

    b = input("Final Score Out Of 40,(ex.30) If You Haven't Get The Final Score Return - :")
    if b == "-":
        final = [0,0]
    
    else:
        final = [int(b),40]

    c = input("Homework Score Out Of 20,(ex.15) If You Haven't Get The Homework Score Return - :")
    if c == "-":
        homework = [0,0]

    else:
        homework = [int(c),20]


    score = [(midterm[0]+final[0]+homework[0]),(midterm[1]+final[1]+homework[1])]
    min_score = score[0]
    if min_score < 50:
        min_grade = "---"
    elif min_score < 55:
        min_grade = "D"
    elif min_score < 60:
        min_grade = "D+"
    elif min_score < 65:
        min_grade = "C"
    elif min_score < 70:
        min_grade = "C+"
    elif min_score < 75:
        min_grade = "B"
    elif min_score <80:
        min_grade = "B+"
    elif min_score >=80:
        min_grade = "A"
    if score[1] == 100:
        print("Your Grade Is: " + min_grade)
    else:
        print("You Are Guaranteed To Get At Least: " + min_grade)
    repeat()

def show():
    print( "A  80 Or More\nB+ 75 Or More\nB  70 Or More\nC+ 65 Or More\nC  60 Or More\nD+ 55 Or More\nD  50 Or More\nF  Lower Than 50")
    repeat()

def repeat():    
    print("What Else Would You Like Us To Help?,(Goal Seek,Max Score,Current Grade,Show Syllabus,End)")
    s = input()
    if s == "Goal Seek":
        yes()
    elif s == "End":
        print("Thank you For Using Grade Calculator!")
    elif s == "Max Score":
        maximum_grade()
    elif s == "Current Grade":
        minimum_grade()
    elif s == "Show Syllabus":
        show()
    else:
        repeat()

def start():    
    print("Welcome To Grade Calculator!,What Would You Like Us To Calculate Today?,(Goal Seek,Max Score,Current Grade,Show Syllabus)")
    s = input()
    if s == "Goal Seek":
        yes()
    elif s == "No":
        print("Thank you For Using Grade Calculator!")
    elif s == "Max Score":
        maximum_grade()
    elif s == "Current Grade":
        minimum_grade()
    elif s == "Show Syllabus":
        show()
    else:
        repeat()

def yes():
    a = input("Midterm Score Out Of 40,(ex.30) If You Haven't Get The Midterm Score Return - :")
    if a == "-":
        midterm = [0,0]
    
    else:
        midterm = [int(a),40]

    b = input("Final Score Out Of 40,(ex.30) If You Haven't Get The Final Score Return - :")
    if b == "-":
        final = [0,0]
    
    else:
        final = [int(b),40]

    c = input("Homework Score Out Of 20,(ex.15) If You Haven't Get The Homework Score Return - :")
    if c == "-":
        homework = [0,0]
    
    else:
        homework = [int(c),20]


    score = [(midterm[0]+final[0]+homework[0]),(midterm[1]+final[1]+homework[1])]
    grade  = input("Insert The Grade You Want(A,B+,B,C+,C,D+,D):")
    obtainable_score = 100 - int(score[1])
    if grade == "A":
        if int(score[0]) >= 80 :
            print("You Have already reached A With The Current Score, Congratulations!")
        elif int(score[0]) < 80 :
            if int(score[0]) + obtainable_score >= 80:
                a = int(80-score[0])
                print(str(a) + " More Score Needed Out Of "+str(obtainable_score)+"!, Keep Fighting!")
            elif int(score[0]) + obtainable_score < 80:
                print("We Are Sorry, A is Unobtainable.")
    elif grade == "B+":
        if int(score[0]) >= 75 :
            print("You Have already reached B With The Current Score, Congratulations!")
        elif int(score[0]) < 75 :
            if int(score[0]) + obtainable_score >= 75:
                a = int(75-score[0])
                print(str(a) + " More Score Needed Out Of "+str(obtainable_score)+"!, Keep Fighting!")
            elif int(score[0]) + obtainable_score < 75:
                print("We Are Sorry, B+ is Unobtainable.")
    elif grade == "B":
        if int(score[0]) >= 70 :
            print("You Have already reached B With The Current Score, Congratulations!")
        elif int(score[0]) < 70 :
            if int(score[0]) + obtainable_score >= 70:
                a = int(70-score[0])
                print(str(a) + " More Score Needed Out Of "+str(obtainable_score)+"!, Keep Fighting!")
            elif int(score[0]) + obtainable_score < 70:
                print("We Are Sorry, B is Unobtainable.")
    elif grade == "C+":
        if int(score[0]) >= 65 :
            print("You Have already reached C+ With The Current Score, Congratulations!")
        elif int(score[0]) < 65 :
            if int(score[0]) + obtainable_score >= 65:
                a = int(65-score[0])
                print(str(a) + " More Score Needed Out Of "+str(obtainable_score)+"!, Keep Fighting!")
            elif int(score[0]) + obtainable_score < 65:
                print("We Are Sorry, C+ is Unobtainable.")
    elif grade == "C":
        if int(score[0]) >= 60 :
            print("You Have already reached C With The Current Score, Congratulations!")
        elif int(score[0]) < 60 :
            if int(score[0]) + obtainable_score >= 60:
                a = int(60-score[0])
                print(str(a) + " More Score Needed Out Of "+str(obtainable_score)+"!, Keep Fighting!")
            elif int(score[0]) + obtainable_score < 60:
                print("We Are Sorry, C is Unobtainable.")
    elif grade == "D+":
        if int(score[0]) >= 55 :
            print("You Have already reached D+ With The Current Score, Congratulations!")
        elif int(score[0]) < 55 :
            if int(score[0]) + obtainable_score >= 55:
                a = int(55-score[0])
                print(str(a) + " More Score Needed Out Of "+str(obtainable_score) + "!, Keep Fighting!")
            elif int(score[0]) + obtainable_score < 55:
                print("We Are Sorry, A is Unobtainable.")
    elif grade == "D":
        if int(score[0]) >= 50 :
            print("You Have already reached A With The Current Score, Congratulations!")
        elif int(score[0]) < 50 :
            if int(score[0]) + obtainable_score >= 50:
                a = int(50-score[0])
                print(str(a) + " More Score Needed Out Of "+str(obtainable_score)+"!, Keep Fighting!")
            elif int(score[0]) + obtainable_score < 50:
                print("We Are Sorry, D is Unobtainable,Please Try Harder Next Year...")
    repeat()

start()
                
