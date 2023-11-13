def maximum_grade():
    a = input("Midterm Score Out Of 40,(ex.30) If You Haven't Get The Midterm Score Return - :")
    if a == "-":
        midterm = [0,0]
    
    else:
        try:
            x = float(a)
            if 0< x <=40:
                midterm = [float(a),40]
            elif x > 40 or x < 0:
                print("Midterm Score Should Be Between 0-40 ,Please Re-Enter The Data...\n|\n|\n|")
                maximum_grade()
        except:
            print("Invalid Score Input,Please Re-Enter The Data...\n|\n|\n|")
            maximum_grade()

    b = input("Final Score Out Of 40,(ex.30) If You Haven't Get The Final Score Return - :")
    if b == "-":
        final = [0,0]
    
    else:
        try:
            x = float(b)
            if 0< x <=40:
                final = [float(b),40]
            elif x > 40 or x < 0:
                print("Final Score Should Be Between 0-40 ,Please Re-Enter The Data...\n|\n|\n|")
                maximum_grade()
        except:
            print("Invalid Score Input,Please Re-Enter The Data...\n|\n|\n|")
            maximum_grade()

    c = input("Homework Score Out Of 20,(ex.15) If You Haven't Get The Homework Score Return - :")
    if c == "-":
        homework = [0,0]
    
    else:
        try:
            x = float(c)
            if 0< x <=20:
                homework = [float(c),20]
            elif x > 20 or x < 0:
                print("Home Work Score Should Be Between 0-20 ,Please Re-Enter The Data...\n|\n|\n|")
                maximum_grade()
        except:
            print("Invalid Score Input,Please Re-Enter The Data...\n|\n|\n|")
            maximum_grade()


    score = [(midterm[0]+final[0]+homework[0]),(midterm[1]+final[1]+homework[1])]
    obtainable_score = 100 - float(score[1])
    max_score = obtainable_score + float(score[0])
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
        m = 0
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
        try:
            x = float(a)
            if 0< x <=40:
                midterm = [float(a),40]
            elif x > 40 or x < 0:
                print("Midterm Score Should Be Between 0-40 ,Please Re-Enter The Data...\n|\n|\n|")
                minimum_grade()
        except:
            print("Invalid Score Input,Please Re-Enter The Data...\n|\n|\n|")
            minimum_grade()

    b = input("Final Score Out Of 40,(ex.30) If You Haven't Get The Final Score Return - :")
    if b == "-":
        final = [0,0]
    
    else:
        try:
            x = float(b)
            if 0< x <=40:
                final = [float(b),40]
            elif x > 40 or x < 0:
                print("Final Score Should Be Between 0-40 ,Please Re-Enter The Data...\n|\n|\n|")
                minimum_grade()
        except:
            print("Invalid Score Input,Please Re-Enter The Data...\n|\n|\n|")
            minimum_grade()

    c = input("Homework Score Out Of 20,(ex.15) If You Haven't Get The Homework Score Return - :")
    if c == "-":
        homework = [0,0]
    
    else:
        try:
            x = float(c)
            if 0< x <=20:
                homework = [float(c),20]
            elif x > 20 or x < 0:
                print("Home Work Score Should Be Between 0-20 ,Please Re-Enter The Data...\n|\n|\n|")
                minimum_grade()
        except:
            print("Invalid Score Input,Please Re-Enter The Data...\n|\n|\n|")
            minimum_grade()


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
        print("Pleae Type Only One Of These(Capital Letter Is Neccessary)-->(Goal Seek,Max Score,Current Grade,Show Syllabus)\n|\n|\n|")
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
        print("Pleae Type Only One Of These(Capital Letter Is Neccessary)-->(Goal Seek,Max Score,Current Grade,Show Syllabus)\n|\n|\n|")
        repeat()

def yes():
    a = input("Midterm Score Out Of 40,(ex.30) If You Haven't Get The Midterm Score Return - :")
    if a == "-":
        midterm = [0,0]
    
    else:
        try:
            x = float(a)
            if 0< x <=40:
                midterm = [float(a),40]
            elif x > 40 or x < 0:
                print("Midterm Score Should Be Between 0-40 ,Please Re-Enter The Data...\n|\n|\n|")
                yes()
        except:
            print("Invalid Score Input,Please Re-Enter The Data...\n|\n|\n|")
            yes()

    b = input("Final Score Out Of 40,(ex.30) If You Haven't Get The Final Score Return - :")
    if b == "-":
        final = [0,0]
    
    else:
        try:
            x = float(b)
            if 0< x <=40:
                final = [float(b),40]
            elif x > 40 or x < 0:
                print("Final Score Should Be Between 0-40 ,Please Re-Enter The Data...\n|\n|\n|")
                yes()
        except:
            print("Invalid Score Input,Please Re-Enter The Data...\n|\n|\n|")
            yes()

    c = input("Homework Score Out Of 20,(ex.15) If You Haven't Get The Homework Score Return - :")
    if c == "-":
        homework = [0,0]
    
    else:
        try:
            x = float(c)
            if 0< x <=20:
                homework = [float(c),20]
            elif x > 20 or x < 0:
                print("Home Work Score Should Be Between 0-20 ,Please Re-Enter The Data...\n|\n|\n|")
                yes()
        except:
            print("Invalid Score Input,Please Re-Enter The Data...\n|\n|\n|")
            yes()


    score = [(midterm[0]+final[0]+homework[0]),(midterm[1]+final[1]+homework[1])]
    grade  = input("Insert The Grade You Want(A,B+,B,C+,C,D+,D):")
    obtainable_score = 100 - float(score[1])
    if grade == "A":
        if float(score[0]) >= 80 :
            print("You Have already reached A With The Current Score, Congratulations!")
        elif float(score[0]) < 80 :
            if float(score[0]) + obtainable_score >= 80:
                a = float(80-score[0])
                print(str(a) + " More Score Needed Out Of "+str(obtainable_score)+"!, Keep Fighting!")
            elif float(score[0]) + obtainable_score < 80:
                print("We Are Sorry, A is Unobtainable.")
    elif grade == "B+":
        if float(score[0]) >= 75 :
            print("You Have already reached B With The Current Score, Congratulations!")
        elif float(score[0]) < 75 :
            if float(score[0]) + obtainable_score >= 75:
                a = float(75-score[0])
                print(str(a) + " More Score Needed Out Of "+str(obtainable_score)+"!, Keep Fighting!")
            elif float(score[0]) + obtainable_score < 75:
                print("We Are Sorry, B+ is Unobtainable.")
    elif grade == "B":
        if float(score[0]) >= 70 :
            print("You Have already reached B With The Current Score, Congratulations!")
        elif float(score[0]) < 70 :
            if float(score[0]) + obtainable_score >= 70:
                a = float(70-score[0])
                print(str(a) + " More Score Needed Out Of "+str(obtainable_score)+"!, Keep Fighting!")
            elif float(score[0]) + obtainable_score < 70:
                print("We Are Sorry, B is Unobtainable.")
    elif grade == "C+":
        if float(score[0]) >= 65 :
            print("You Have already reached C+ With The Current Score, Congratulations!")
        elif float(score[0]) < 65 :
            if float(score[0]) + obtainable_score >= 65:
                a = float(65-score[0])
                print(str(a) + " More Score Needed Out Of "+str(obtainable_score)+"!, Keep Fighting!")
            elif float(score[0]) + obtainable_score < 65:
                print("We Are Sorry, C+ is Unobtainable.")
    elif grade == "C":
        if float(score[0]) >= 60 :
            print("You Have already reached C With The Current Score, Congratulations!")
        elif float(score[0]) < 60 :
            if float(score[0]) + obtainable_score >= 60:
                a = float(60-score[0])
                print(str(a) + " More Score Needed Out Of "+str(obtainable_score)+"!, Keep Fighting!")
            elif float(score[0]) + obtainable_score < 60:
                print("We Are Sorry, C is Unobtainable.")
    elif grade == "D+":
        if float(score[0]) >= 55 :
            print("You Have already reached D+ With The Current Score, Congratulations!")
        elif float(score[0]) < 55 :
            if float(score[0]) + obtainable_score >= 55:
                a = float(55-score[0])
                print(str(a) + " More Score Needed Out Of "+str(obtainable_score) + "!, Keep Fighting!")
            elif float(score[0]) + obtainable_score < 55:
                print("We Are Sorry, A is Unobtainable.")
    elif grade == "D":
        if float(score[0]) >= 50 :
            print("You Have already reached A With The Current Score, Congratulations!")
        elif float(score[0]) < 50 :
            if float(score[0]) + obtainable_score >= 50:
                a = float(50-score[0])
                print(str(a) + " More Score Needed Out Of "+str(obtainable_score)+"!, Keep Fighting!")
            elif float(score[0]) + obtainable_score < 50:
                print("We Are Sorry, D is Unobtainable,Please Try Harder Next Year...")
    else:
        print("Please Make Sure That You Enter The Grade Correctly(Capital Letter Is Neccessary...\n|\n|\n|")
        yes()
    repeat()

start()
                
