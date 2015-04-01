"""
1. What's the primary difference between the following two ipython magic (%)
commands?
"""
%matplotlib inline
%pylab inline



"""
2.  We have a file called "ads_performance.csv" which includes the following
header rows, and one row and the end that sums the total of the dataset.

Google Adwords Perfomance
February 16 2015, February 22 2015
Brand
date, ad_id, strategy_group, description, spend, spend_wfees, impressions, clicks
02/16/2015, 1772, 'team_bananas', 'Did you know there are 100s of bananas? Click here to find out more!', 23.75, 24.33, 107771, 10

Write the pd.read_csv function that would ignore the additional headers, use the
correct header for the column names, and ignore the very last row.
"""

header_row = ['date', 'ad_id', 'strategy_group', 'description', 'spend', 'spend_wfees', 'impressions', 'clicks',]
url = 'ads_performance.csv'
ads = pd.read_csv(url, header=0)
ads.columns = header_row


"""
3. With the ads dataset stored in name `ads`, write code that'd create a subset
of just ad_id 200 where the spend was more than 30 dollars

subset = ads...(some_code)...
"""

subset = ads[(ads.ad_id == 200) & (ads.spend > 30)]


"""
4. We want to aggregate the sum of spend by day and ad. What code would return
back that dataset?
"""

grouped = ads.groupby(['date', 'ad_id']).sum()

"""
5. Explain what the following code block is doing, line by line.
"""
#import the matplotlib module
import matplotlib.pyplot as plt 

#w import the division module. This will change the / operator to mean true division throughout the module.
from __future__ import division


#add a new column called 'crt', divide the data in the clicks column by the impressions column
ads['ctr'] = ads['clicks'] / ads['impressions']

#initialize a new figure object
fig = plt.figure()

#create the first subplot object
plt.subplot(1, 2, 1)

#create a histogram using the data from the spend column
plt.hist(ads.spend)

#create the second subplot object
plt.subplot(1, 2, 2)

#plot a scatter plot using ads.spend as the x values and ads.ctr as the y values. The chart will be plotted with . and is green
plt.plt(ads.spend, ads.ctr, 'g.')
plt.show()


"""
6-8. Imagine we're viewing the following coefficient table for the following
regression:

(ad_id1772 is either 1 or 0, meaning it was ad 1772, or it was not)
'spend ~ impressions + clicks + ad_id1772'

column          coefficient         pvalue
y_intercept     0.02                0.000
impressions     0.00057             0.038
clicks          0.976               0.78
ad_id1772      -0.5                 0.02


6. How much can we assume the ad cost to place online, based on it having
   no impressions?
7. Which part of the model seems insignificant to solving for cost?
8. What effect does ad 1772 have on the cost of the ad?

"""


"""
9. What does a Trellis plot allow you to do?
What python library does theTrellis plot come from?
"""


"""
10. What does the reset_index() function do on a DataFrame?
Describe an instance you might need to use it.
"""