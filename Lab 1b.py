
t1 = float(input("Enter score of Mini-Test 1: "))
t2 = float(input("Enter score of Mini-Test 2: "))
t3 = float(input("Enter score of Mini-Test 3: "))

scores = [t1, t2, t3]
scores.sort(reverse=True)

average = (scores[0] + scores[1]) / 2
print("Best average score of two mini-tests:", average)