import matplotlib.pyplot as plt
months = ["jan", "feb", "mar", "apr", "may"]
revenue_2025 = [100, 120, 110, 150, 130]
revenue_2027 = [150, 118, 130, 140, 190]


plt.figure(figsize=(14, 5), dpi=100) #75, 100, 150, 300
plt.suptitle("Comparison of charts", fontsize=18, fontweight='bold')


# default chart
plt.subplot(1, 2, 1)
plt.plot(months, revenue_2025)
plt.plot(months, revenue_2027)

# custom chart
plt.subplot(1, 2, 2)
plt.plot(months, revenue_2025,
         color='red',
         lw=3,
         marker='o', # s, x 
         markersize=5,
         markerfacecolor='yellow',
         markeredgecolor='black',
         linestyle='-', # --, :, :-
         label="2025 Data")
plt.plot(months, revenue_2027,
         color='blue',
         lw=3,
         marker='o', # s, x 
         markersize=5,
         markerfacecolor='green',
         markeredgecolor='black',
         linestyle=':', # --, :, :-
         label="2027 Data")
plt.xlabel("Months", fontsize=14)
plt.ylabel("Revenue", fontsize=14)
plt.grid(alpha=0.3)
plt.legend()
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout(rect=[0.05, 0.05, 0.95, 0.95])
plt.savefig("screenshots/compare.png")
plt.show()