import seaborn as sns
import matplotlib.pyplot as plt
mpg = sns.load_dataset("mpg")
#sns.displot(data=mpg,x='cylinders',bins=5,kde=True)
#plt.xlabel("No. of cylinder")
#plt.show()
print(mpg.shape)
print(mpg.info())
print(mpg.isnull().sum())
mpg=mpg.sort_values(by='horsepower',ascending=False)
print(mpg.drop_duplicates(keep='first'))