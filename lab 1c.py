
trial1 = float(input("Enter performance for Trial 1: "))
trial2 = float(input("Enter performance for Trial 2: "))
trial3 = float(input("Enter performance for Trial 3: "))

performances = [trial1, trial2, trial3]
performances.sort(reverse=True)
best_two_average = (performances[0] + performances[1]) / 2

print("The average of the all the Following above trails:",best_two_average)
