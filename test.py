number = input("people?")
scorelist = []
for i in range(int(number)):
    score = input("score?")
    scorelist.append(int(score))
SortedScore = sorted(scorelist)
print("The highest score is: " + str(SortedScore[int(number)-1]))