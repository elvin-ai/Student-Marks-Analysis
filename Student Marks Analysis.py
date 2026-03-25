import numpy as np
import matplotlib.pyplot as plt 

print("Hello. Welcome to the student mark analyser project created by Elvin Pillay.")
names=input("Enter names : \n").split()
marks=list(map(int,input("Enter marks : \n").split()))

m=np.array(marks)
n=np.array(names)

avg=np.average(m)
mean=np.mean(m)
m1=np.max(m)
hm=np.argmax(m)
indices=np.where(m==m1)[0]
toppers=n[indices]

print("Highest Marks  : ", m1)
print("Highest Scorer : ",toppers)

plt.bar(n,m)
plt.title("Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
