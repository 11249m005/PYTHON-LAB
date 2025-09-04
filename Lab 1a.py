
test1 = float(input("Enter marks for Test 1: "))
test2 = float(input("Enter marks for Test 2: "))
test3 = float(input("Enter marks for Test 3: "))

marks = [test1, test2, test3]
marks.sort(reverse=True)

best_two_average = (marks[0] + marks[1]) / 2

print("Best two test average in Tests:", best_two_average)
