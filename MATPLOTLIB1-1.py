import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st_mark=np.array([4,4.5,5,5.5,6,6.5,7,8,9])
st_score=np.array(["A","A1","B","B1","C","C1","G","G1","G2"])
tb_mark=pd.DataFrame(st_mark,columns=["MARK"])
tb_score=pd.DataFrame(st_score,columns=["SCORE"])
data_base=pd.concat([tb_mark,tb_score],axis=1)

# Representation Tha Data

# PLOT
plt.plot(st_mark,st_score,color="green")
plt.xlabel("THE MARKS")
plt.ylabel("THE SCORE",color="red")
plt.show()

# SCATTER
plt.scatter(st_mark,st_score,color="blue")
plt.xlabel("THE MARKS",color="orange")
plt.ylabel("THE SCORE",color="red")
plt.show()

# BAR
plt.bar(st_mark,st_score,alpha=0.5,color="red")
plt.xlabel("THE MARKS",color="blue")
plt.ylabel("THE SCORE",color="red")
plt.show()

# PLOT & SCATTER & BAR
plt.style.use("bmh")
plt.plot(st_mark,st_score,color="pink")
plt.scatter(st_mark,st_score,color="red")
plt.bar(st_mark,st_score,color="green",alpha=0.5)
plt.xlabel("THE MARKS",color="blue")
plt.ylabel("THE SCORE",color="red")
plt.show()

# HIST
plt.hist(st_score,histtype="bar",color="orange",bins=20)
plt.title("HISTOGRAM_THE_MARK",color="green",size=16)
plt.show()

