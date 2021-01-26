#average your scores
ascore = input("your first score:")
bscore = input("your second score:")
cscore = input("your third score:")
avgscore = (int(ascore) + int(bscore) + int(cscore)) / 3
print("Your average is: " + str(avgscore))
if 0>=avgscore or avgscore>=100:
    print("That's not valid.")
elif avgscore>=90:
    print("Grade: A")
elif avgscore>=80:
    print("Grade: B")
elif avgscore>=70:
    print("Grade: C")
elif avgscore>=60:
    print("Grade: D")
else:
    print("You failed. You know that, right?")