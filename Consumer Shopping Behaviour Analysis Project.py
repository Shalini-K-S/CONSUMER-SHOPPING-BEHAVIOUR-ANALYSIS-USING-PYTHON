#!/usr/bin/env python
# coding: utf-8

# #                                      CONSUMER SHOPPING BEHAVIOUR ANALYSIS

# The 'Customer sales data'provides detailed overview of the customer preferences including their demographic details,product preferences,purchase history,prefered shipping method etc.Using this data we can analyze the relationship between one another.
# This helps to make customer based decision making like target market identification,identify marketing strategies etc ,this helps in optimizing the customer satisfaction and increases the overall sales rate.
# 

# In[1]:


#Analysis of Clothing and Accessories store sales data


# In[5]:


# Importing data from 'Customer sales data.csv'file
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
raw_data=pd.read_csv('Customer sales data.csv',index_col='Customer ID')
raw_data


# In[2]:


raw_data.shape


# In[7]:


# Number of rows and columns in the data


# In[8]:


print("Number of rows:",raw_data.shape[0])
print("Number of columns:",raw_data.shape[1])


# In[9]:


#Column names 


# In[10]:


raw_data.columns


# In[11]:


#Statistical information about the data


# In[12]:


raw_data.describe()


# In[13]:


#Displaying the top 15 rows
raw_data.head(15)


# In[14]:


#Displaying the bottom 15 rows
raw_data.tail(15)


# In[15]:


# Data cleaning and preparation


# In[16]:


#Removing the duplicate rows
raw_data.drop_duplicates()


# In[17]:


#Identification of blank cells in each column
raw_data.isnull().sum()


# In[8]:


#Removing null values in 'item Purchase','Category','Purchase amount(USD)','Location'columns
sales_data=raw_data.dropna(subset=['Item Purchased','Category','Purchase Amount (USD)','Location'])
sales_data


# In[19]:


#Inserting values in 'Subscription Status'and 'Promo code used' column
sales_data.fillna('No')


# In[20]:


sales_data.info()


# In[21]:


# Visualization  of cleaned data


# In[22]:


# Identifying the Age group of customers


# In[23]:


sns.histplot(sales_data.Age,kde=True,color='green',alpha=0.5)
plt.title(' Customers Age group');


# Based on the above graph we can conclude that the age group of customers is 20 to 70 years.

# In[24]:


# Gender distribution by purchase Amount


# In[5]:


gender_sum=sales_data.groupby('Gender')['Purchase Amount (USD)'].sum()
gender_sum


# In[6]:


color=['brown','violet']
plt.pie(gender_sum,labels=gender_sum.index,autopct='%1.1f%%',startangle=180,colors=color)
plt.title('Impact of Gender on Purchases');


# Male spend (67%)is more than female(32%).

# In[27]:


#Visualization of top 15 location by Average Purchased value


# In[36]:


location_sum=sales_data.groupby('Location')['Purchase Amount (USD)'].agg(['mean','median','sum'])
location=location_sum.sort_values(by=['mean'],ascending=False).head(15)
location


# In[35]:


plt.figure(figsize=(12,6))
plt.bar(location.index,location['mean'])
plt.xlabel('Location')
plt.ylabel('Average Purchased Value')
plt.title('Top 15 Location Based on Average Purchased Value')
plt.xticks(rotation=90);


# Alaska is the region with highest average Purchase value which is followed by Pennslyvania and Arizona.

# In[ ]:


#Shopping Behaviour in each region


# In[37]:


location_group=sales_data.groupby('Location')
for location,location_data in location_group:
    print("Regional Trends for",location,":")
    avg_amt=location_data['Purchase Amount (USD)'].mean()
    print(f"The average purchase amount of the region :${avg_amt:.2f}")
    prefer_category=location_data['Category'].value_counts().idxmax()
    print("Most preferred category is",prefer_category)
    payment_method=location_data['Payment Method'].value_counts()
    print("Payment method preference:\n",payment_method)


# In[ ]:


#Impact of size on Purchases


# In[10]:


size=sales_data['Size'].value_counts()
size


# In[28]:


plt.pie(size,startangle=90,labels=size.index,autopct='%1.1f%%')
plt.title('Impact of size on Purchase');


# From the chart we can say that majority of purchases are of size M (45%).

# In[12]:


#Impact of Season on Purchase


# In[15]:


seasonal_purchase=sales_data.groupby('Season')['Purchase Amount (USD)'].mean()
seasonal_purchase


# In[25]:


plt.bar(seasonal_purchase.index,seasonal_purchase,color='violet',alpha=0.8)
plt.title("Impact of Season on Purchase")
plt.xlabel('Season')
plt.ylabel('Average Purchase (USD)');


# The bar graph shows that customers buy more in the Winter and Fall.

# In[ ]:


#Category distribution by number products sold


# In[31]:


category_count=sales_data['Category'].value_counts()
category_count


# In[32]:


plt.figure(figsize=(12,6))
myexplode=[0.2,0,0,0]
plt.pie(category_count,autopct='%1.1f%%',explode=myexplode,shadow=True)
plt.legend(category_count.index)
plt.title('Impact of Category on Purchase '); 


# The highest purchased is Clothing(44%) and Accessories(31.8%) whereas Outwear(8.3%) is the least purchased category.

# In[33]:


#Average Review Rating for each category


# In[49]:


plt.figure(figsize=(40,15))
plot=sns.barplot(x=sales_data['Review Rating'],y=sales_data['Category'],palette='magma')
plot.bar_label(plot.containers[0],fontsize=25)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.title("Average Review Rating by item Category",fontsize=45)
plt.ylabel("Item Category", fontsize = 45)
plt.xlabel("Review Rating", fontsize = 45);


# The average Review rating for every Category is equal to 3.7.

# In[ ]:


#Visualiztion on preferred Shipping method


# In[26]:


shipping=sales_data['Shipping Type'].value_counts()
shipping


# In[29]:


col=['orange','pink','red','yelow','blue','grey']
plt.barh(shipping.index,shipping.values,color = ['blue','yellow','pink','red','orange','lightblue'])
plt.title('Shipping Method')
plt.xlabel('');


# The most preferred Shipping method is Free shipping which is followed by Standard and Store pickup.

# In[54]:


#Impact of Promo code on Purchase


# In[56]:


discount_applied=sales_data['Promo Code Used'].value_counts()
plt.pie(discount_applied,labels=discount_applied.index,autopct='%1.1f%%')
plt.title('Impact of Promo code on Purchase');


# According to the Pie chart there is no big impact of Promotions in purchase.

# In[58]:


# Visualization of Preferred Payment method


# In[59]:


pay=sales_data['Payment Method'].value_counts()
pay


# In[60]:


plt.bar(pay.index,pay.values,data=pay.values,color='violet')
for index,values in enumerate(pay):
    plt.text(index,values,str(values))
plt.xlabel('Payment mode')
plt.ylabel('count')
plt.title('Preferred Payment Method');


# The most Preferred Payment Method is Paypal and least preferred is Bank Transfer.

# In[ ]:


#Visualization of frequency of Purchases


# In[9]:


freq=sales_data['Frequency of Purchases'].value_counts().sort_values(ascending=True)
freq


# In[10]:


plt.figure(figsize=(12,6))
plt.bar(freq.index,freq.values,color='violet')
plt.title('Frequency of Purchases')
plt.xlabel('Purchases')
plt.ylabel('Frequency');


# In[65]:


#Visualization of frequency of Purchase each Products


# In[64]:


purchase=sales_data.groupby('Item Purchased')['Purchase Amount (USD)'].agg(['count'])
plt.pie(purchase['count'],labels=purchase.index,autopct='%1.1f%%',pctdistance=0.7,labeldistance =1.1,radius=1.5);


# In[36]:


# Visualization of Top 10 products Purchased


# In[5]:


prod=sales_data['Item Purchased'].value_counts().head(10)
prod


# In[7]:


plt.figure(figsize=(12,6))
plt.barh(prod.index,prod.values,color='red',alpha=0.6)
plt.xlabel('Number of purchases')
plt.ylabel('Products')
plt.title('TOP 10 Products');


# In[57]:


#Coupon availability for users with more than 10 purchase


# In[58]:


eligible=sales_data[sales_data['Previous Purchases']>10]
num_eligible=len(eligible)
if num_eligible >0:
    print(num_eligible,'users are eligible for coupon code')
else:
    print("No users are eligible for a coupon.")


# In[59]:


# Highest and Least purchased item


# In[80]:


highest=sales_data['Item Purchased'].value_counts().head(1)
least=sales_data['Item Purchased'].value_counts().tail(1)
print("The highest",highest)
print("The least",least)


# In[178]:


#Identify most to least purchased product


# In[14]:


sort_data=sales_data.groupby('Item Purchased')['Purchase Amount (USD)'].count()
total_sort_data=sort_data.sort_values(ascending=False)
total_sort_data


# In[15]:


#30% off for combo of top 3 items Purchased


# In[17]:


def freq_items(jewelry_price,blouse_price,pants_price,discount=30):
    total_items={'Jewelry':jewelry_price,'Blouse':blouse_price,'Pants':pants_price}
    sum_total_items=sum(total_items.values())
    discount_total=sum_total_items*(1-discount/100)
    print("Total items purchased:",total_items)
    print("Cost of total purchase:$",sum_total_items)
    print("Discount price:$",discount_total)
freq_items(6000,3500,3000)


# In[18]:


#50% off for least purchased item
def least_items(jeans_price,gloves_price,discount=50):
    least_total={'Jeans':jeans_price,'Gloves':gloves_price}
    sum_least=sum(least_total.values())
    discount_total=sum_least*(1-discount/100)
    print("Total items purchased:",least_total)
    print("Cost of total purchase:$",sum_least)
    print("Discount price:$",discount_total)
least_items(3500,850)
    


# In[13]:


# 30% off for combo of most and least purchased item
def most_least_combo(blouse_price,jeans_price,discount=30):
    combo={'Blouse':blouse_price,'Jeans':jeans_price}
    price_combo=sum(combo.values())
    discount_price=price_combo*(1-discount/100)
    print("Total items Purchased:",combo)
    print("Cost of total Purchase: $",price_combo)
    print("Discount price:$",discount_price)
most_least_combo(6000,3650)


# # INSIGHTS:

# --> Target market is between the age group of 20 to 70 years in which priotize 60 years group as they are the largest growing customer segment.

# --> Male customers are  35% more than female customers.Increase items and category for male whereas focus female in marketing and sales strategies.

# --> Focus marketing in 'Alaska','Pennsylvania','Arizona' region as they have the high value customers.

# --> Regional trends for every region is identified based on which marketing and promotional activities can be planned.

# --> Focus on having higher stock in 'M' size has 45% of customers shop.

# --> Customers shop more during 'Winter' and 'Fall' compared to 'Spring' and 'Summer'.

# --> Clothing is the most popular category among the customers of all demographics.'Outerwear' is the least popular category so            markteing and promotional activities should be planned for it to increase the sales.

# --> Average review rating for all item category is same and equal to 3.7.

# --> Usage of promotional codes does not have significant impact on the purchasing behaviour.

# --> The most preferred payment method among the customers is 'PayPal'.

# --> 'Blouse' and 'Jewelry' are the highest purchased items by the customers.

# --> 'Coupon for more than 10 Purchases','Combo offer for most purchased item','Combo offer for least purchased item','Combo offer for most and least item' are some of the marketing strategies that can be applied to increase the overall sales.

# In[ ]:




