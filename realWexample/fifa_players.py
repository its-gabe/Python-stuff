import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fifa = pd.read_csv(r'Python-stuff\fifa_data.csv')

# HISTOGRAM - Skill level of players
bins = list(range(0,101,10))

# plt.hist(fifa.Overall, bins=bins)
# plt.title("Distribution of fifa's soccer players")
# plt.ylabel('Number of Players')
# plt.xlabel('Skill level')
# plt.xticks(bins)
# plt.show()




# PIE - percentage of palyers who prefer left or right

# left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
# right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
# labels = ['left', 'right']

# plt.title('Foot Preference of FIFA players')
# plt.pie([left, right], labels=labels, colors=['b', 'purple'], autopct='%.2f %%')
# plt.show()





# PYCHART - Weight distribution of fifa players


# fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa['Weight']]

# plt.style.use('ggplot')
# light = fifa[(fifa.Weight < 125)].count()[0]
# light_medium = fifa[(fifa.Weight > 125) & (fifa.Weight <= 150)].count()[0]
# medium = fifa[(fifa.Weight > 150) & (fifa.Weight <= 175)].count()[0]
# medium_heavy = fifa[(fifa.Weight > 175) & (fifa.Weight <= 200)].count()[0]
# heavy = fifa[(fifa.Weight > 200)].count()[0]
# labels = ['Under 125', '125-150', '150-175', '175-200', 'Above 200']
# weights = [light, light_medium, medium, medium_heavy, heavy]
# distances = (.15, .01, .01, .01, .15)

# plt.pie(weights, labels=labels, autopct="%.2f %%", pctdistance=0.7, explode=distances)
# plt.show()







# BOXPLOT - Average of club overall's 

barcelona = fifa.loc[fifa['Club'] == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa['Club'] == 'Real Madrid']['Overall']
revs = fifa.loc[fifa['Club'] == 'New England Revolution']['Overall']

plt.figure(figsize=(5,8))
teams = barcelona, madrid, revs
labels = ['FC Barcelona', 'Real Madrid', 'New England']
plt.title('Overall soccer players from different teams')
plt.boxplot(teams, labels=labels)
plt.show()