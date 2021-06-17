from random import randint, choice
def Prime(Number):
    TF = True
    if Number > 1:
        for i in range(2, Number):
            if Number % i == 0:
                TF = False
                break
    else:
        TF = False
    if TF:
        Txt = "\033[038;2;255;253;184mNumber Is Prime Number"
    else:
        Txt = "\033[038;2;255;253;184mNumber Is Not Prime Number"
    print(Txt)
    return TF
def Between(Number):
    print("Number Is Between {} and {}".format(randint(0, Number-1), randint(Number+1, Stop)))
def Divide(Number):
    k = 0
    for i in range(3, 10):
        if Number % i == 0:
            print("Number can Divide by {}".format(i))
            k += 1
def Option(Number):
    choice_arr = [Number]
    for i in range(2):
        choice_arr.append(randint(Number - randint(0, 10), Number + randint(0, 10)))
    One = choice(choice_arr)
    choice_arr.remove(One)
    Two = choice(choice_arr)
    choice_arr.remove(Two)
    Three = choice_arr[0]
    print("Choice : {} | {} | {} ".format(abs(One), abs(Two), abs(Three)))
def game(S, E):
    Number = randint(S, E)
    Prime(Number)
    Between(Number)
    Divide(Number)
    Option(Number)
    Answer = input("\033[038;2;153;230;255mEnter Answer (\"Hint\" for Hint) : ")
    score = 0
    Wrong = True
    try:
        if int(Answer) == Number:
            print("\033[038;2;79;255;82mNice!")
            Wrong = False
            score += 1
        else:
            print("\033[038;2;255;153;153mWrong!")
    except:
        OperatorList = ["+", "-", "*", "//"]
        if Answer.lower() == "hint":
            score -= 1
            Operator = choice(OperatorList)
            Random = randint(S, Number)
            Result = str(Number) + Operator + str(Random)
            print("\033[038;2;255;153;153mHint: x {} {} = {}".format(Operator, Random, eval(Result)))
        else:
            raise SyntaxError("\033[0;0mBad Input")
        Answer = input("\033[038;2;153;230;255mEnter Answer : ")
        if int(Answer) == Number:
            print("\033[038;2;185;255;150mNice!, but next time try to not use hint")
            Wrong = False
            score += 1
        else:
            print("\033[038;2;255;54;43mWrong!, EVEN USE HINT STILL WRONG?!!!")
    if Wrong:
        print("\033[038;2;156;255;219mAnswer is :", Number)
    return score
    
Games = int(input("\033[038;2;153;230;255mHow many Games You want to play : "))
Start, Stop = map(int, input("Enter Range of Number : ").split())
Collect_Score = 0
for i in range(Games):
    print("\033[038;2;174;247;96mQuesion <{}>\033[0;0m".format(i+1))
    Collect_Score += game(Start, Stop)
    print("\033[038;2;255;248;117mScore :", Collect_Score)
if Collect_Score/Games == 1:
    print("\033[038;2;247;202;96mMAX Score!!!\033[0;0m")
else:
    print("\033[038;2;247;202;96mTotal Score Is : {}/{}\033[0;0m".format(Collect_Score, Games))