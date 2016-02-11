
# coding: utf-8

# In[22]:

from pylab import *


# In[23]:

# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

# The slices will be ordered and plotted counter-clockwise.
labels = 'Open', "Didn't grow", 'Dead'
fracs = [81, 0, 19]
colors = ['green', 'yellow', 'red']

pie(fracs, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
                # The default startangle is 0, which would start
                # the Frogs slice on the x-axis.  With startangle=90,
                # everything is rotated counter-clockwise by 90 degrees,
                # so the plotting starts on the positive y-axis.

title('At 0gm/mL', bbox={'facecolor':'0.9', 'pad':5})
savefig('aliveAndDeadC1.png')

show()


# In[ ]:



