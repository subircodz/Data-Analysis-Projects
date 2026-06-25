import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")
# inspect
print(df.head())
print(df.info())
print(df.describe())

avg_marks = df.mean(numeric_only=True)
print(avg_marks)
plt.bar(avg_marks.index, avg_marks.values)
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Average marks of Subjects")
plt.savefig("average.png")
plt.show()

print(df[df["Maths"] > 90])

print(df[
    df["Maths"] < 30][["Name", "Maths"]]
    )

# Marks variations, how are the marks spreadout
plt.hist(df["Maths"])
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Maths marks distribution")
plt.grid(alpha=0.3) # 0, 0.3, 0.5, 1
plt.savefig("Maths_marks_distribution.png")
plt.show()
