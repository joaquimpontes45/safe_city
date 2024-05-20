import matplotlib.pyplot as plt


plt.figure(figsize=(6,6))
jo=['a','e','i','o','u','u','o','i','e','a']
v= [len(jo),12, 15, 19, 23, 40]
lab=['teste',"mundaú", "Cohab 3", "Boa Vista", "Cohab 2", "Magano"]
color = ['#808080','#1f77b4', '#4c92ca', '#7ab8e1', '#a8d3f8', '#d6e9ff']  # Azul escuro para azul claro

plt.pie(v,labels=lab, autopct='%.2f%%', colors=color)

plt.show()