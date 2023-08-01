def percent(marks):
    p = ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p

marks1 = [45,98,78,60]
percentage1 = percent(marks1)

marks2 = [68,90,88,70]
percentage2 = percent(marks2)

marks3 = [90,98,89,86]
percentage3 = percent(marks3)

print(percentage1, percentage2, percentage3)
