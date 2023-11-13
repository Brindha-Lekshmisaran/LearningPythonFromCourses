if __name__ == '__main__':
    namelst = []
    scorelst = []
    # Getting the value for N
    for _ in range(int(input())):
        #Getting the name of the student
        name = input()
        # Getting the grade of the student
        score = float(input())
        namelst.append(name)    
        scorelst.append(score)
    # zip these two lists together
    nestedlst = [[namelst[k], scorelst[k]] for k in range(len(namelst))]
    print(nestedlst)