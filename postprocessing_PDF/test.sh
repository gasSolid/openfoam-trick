#!/usr/bin/python

import random
import matplotlib.pyplot as plt

x = range(1, 101)
y1 = [random.randint(1, 100) for _ in xrange(len(x))]
y2 = [random.randint(1, 100) for _ in xrange(len(x))]

fig = plt.figure()
ax = fig.add_subplot(111)    # The big subplot
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

# Turn off axis lines and ticks of the big subplot
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
#ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

ax1.loglog(x, y1)
ax2.loglog(x, y2)

# Set common labels
ax.set_xlabel('common xlabel')
ax.set_ylabel('common ylabel')

ax1.set_title('ax1 title')
ax2.set_title('ax2 title')

plt.savefig('common_labels.png', dpi=300)
