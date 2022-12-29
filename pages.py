from matplotlib import pyplot as plt
import numpy as np
import csv

x = ["M", "T", "W", "R", "F", "S", "Su"]
y1=[]
y2=[]
for i in x:
  print("---", i, "---")
  y1.append(int(input("Number of pages read: ")))
  y2.append(60*float(input("Number of hours read (.1 hrs = 6 mins): ")))

r = np.corrcoef(y1, y2)[0,1]


plt.subplot(3, 3, 1)
plt.bar(x, y1, label="Pages")
plt.legend()
plt.title('Pages Read per Day')
plt.xlabel('Days')
plt.ylabel('Pages')

plt.subplot(3, 3, 3)
plt.bar(x, y2, label='Minutes', color='pink')
# plt.plot(x, y2, label='Minutes', color='pink')
plt.title("Minutes Read per Day", color='#A33C26')
plt.xlabel('Days', color='#A33C26')
plt.ylabel('Minutes', color='#A33C26')
plt.legend()

sessions = [] # per day
with open('data.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for i in plots:
        for j in i:
          sessions.append(int(j))


plt.subplot(3, 3, 7)
plt.hist(sessions, label='per day')
plt.xlabel('Sessions per Day')
plt.ylabel('Frequency')
plt.title('frequency of sessions per day')
plt.legend()


plt.subplot(3, 3, 9)
plt.scatter(y1, y2, label='r={:0.2f}'.format(r),
            color='k', s=25, marker='*')
plt.xlabel('pages')
plt.ylabel('hours')
plt.title('pages vs hours read')
plt.legend()


plt.show()
