import pandas as pd
import plotly.express as px

data=pd.read_csv('apple_products.csv')

#first we see top 10 highest rated iphone models
data.head()
data.describe()
data.isnull().sum() #no missing value

highest_rated=data.sort_values(by='Star Rating',ascending=False).head(10)
highest_rated

#use px
iphone=highest_rated['Product Name']
counts=highest_rated['Number Of Ratings']
figure=px.bar(highest_rated,x=iphone,y=counts,title='Number Of Ratings of Highest Rated iphone')
figure.update_layout()#just like tight_layout
figure.show()
#APPLE iPhone 8 Plus (Gold, 64 GB) has the highest Number of Ratings

iphone=highest_rated['Product Name']
counts=highest_rated['Number Of Reviews']
figure=px.bar(highest_rated,x=iphone,y=counts,title='Number Of Reviews of Highest Rated iphone')
figure.update_layout()#just like tight_layout
figure.show()
#APPLE iPhone 8 Plus (Gold, 64 GB) has the highest Number of Reviews too

figure=px.scatter(data_frame=data,x='Number Of Ratings',y='Sale Price',size='Discount Percentage',trendline='ols',title='Relationship between sales price & number of ratings of iphone')
figure.show()# marker will be big or small based on size of discount precentage more discount more marker size and vice-versa
#Based on the scatter plot, there appears to be a weak negative correlation between the sales price of iPhones and the number of ratings they receive.

# This means that, generally, as the number of ratings increases, the sales price tends to decrease slightly.

figure=px.scatter(data_frame=data,x='Number Of Ratings',y='Discount Percentage',size='Sale Price',trendline='ols',title='Relationship between Discount Percentage & number of ratings of iphone')
figure.show()
#Positive Correlation: There seems to be a positive correlation between the discount percentage and the number of ratings. This suggests that iPhones with higher discount percentages tend to have more ratings.