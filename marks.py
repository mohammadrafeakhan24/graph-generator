import matplotlib.pyplot as plt
week = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Marks = [12, 10, 10, 15, 17, 25, 12, 22, 35, 40]
#plotting line graph
plt.plot(week, Marks)
#Set the x axis and y-axis labels.
plt.xlabel('Week')
plt.ylabel('Unit Test marks')
plt.show()
