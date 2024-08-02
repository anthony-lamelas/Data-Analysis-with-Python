import numpy as np
import matplotlib.pyplot as plt


data = {'Illiterate': 38.7, 'Dietary': 18.7, 'Living Alone':22.9,'Housing':19.2,
         'Unmet Health Needs':26, 'Washing Oneself': 17.4, 'D.E.D': 11, 'Intense Pain': 58}

problems = list(data.keys())
percent = list(data.values())

fig, ax = plt.subplots(figsize=(12,8))


bars = ax.barh(problems, percent, color='blue')


ax.set_title("Percent of Elderly Experiencing Issues")


ax.tick_params(axis='both', which='major', labelsize=8)

for bar in bars:
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height()/2, f'{width:.1f}%', 
            va='center', ha='left', fontsize=10)


plt.show()