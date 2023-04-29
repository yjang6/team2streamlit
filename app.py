#!/usr/bin/env python
# coding: utf-8

# In[38]:


# Importing Important modules like - Altair, Pandas, NumPy, Streamlit etc
import altair as alt
import pandas as pd
import numpy as np
import streamlit as st
from vega_datasets import data


# In[39]:


data = pd.read_csv ('starbucks_drink.csv')


# In[113]:


scatter = alt.Chart(data).mark_point().encode(
    x='Calories',
    y='Sugars(g)',
    color = 'Category',
    tooltip=['Category', 'Name', 'Calories', 'Sugars(g)', 'Size']
).properties(
    title='Calories vs Sugars in Drinks',
    width = 600,
    height = 400
).interactive()

scatter2 = alt.Chart(data).mark_point().encode(
    x='Calories',
    y='Sugars(g)',
    color = 'Category',
    tooltip=['Category', 'Name', 'Calories', 'Sugars(g)']
).properties(
    title='Calories vs Sugars in Drinks with best fit line',
    width = 600,
    height = 400
)
corr = data[['Calories', 'Sugars(g)']].corr().iloc[0,1]

fit_best =scatter2 + scatter2.transform_regression('Calories', 'Sugars(g)').mark_line()



tab1, tab2, tab3, tab4, tab5= st.tabs(['Goal and Introduction of the Project','Comparison of two nutrient values', 'Bar Charts', 'Pie Chart', 'Conclusion'])

with tab1:
    st.title('Goal and Introduction of the Project')
    st.subheader('Introduction')
    st.write('Welcome to team 2s project. The people that have contributed to this project are Fernando Contreras-Juarez, Geetha Ghulekar, Anantnaval Gaikwad, and Youngjin Jang')
    st.subheader(':green[Inspiration]')
    st.write('We found inspiration from coffee. So we thought why not starbucks as it is the most popular coffee chain throughout the entirety of the world. Caffeine is very prevalent to most college students whether it be for early classes or staying up late to study. College students drink a lot of coffee and we even have a starbucks on campus. So we decided to use that as inspiration and see what kind of nutrients are inside there and to help visualize what you are drinking')
    st.subheader(':yellow[Goal]')
    st.write('The goal of this was to show you how healthy or unhealthy the drinks were at starbucks. Such as how much sugar goes into what, or how much cholesterol, overall calorie count and more. So throughout this project I hope we made it easy to visualize that.')
    st.subheader('Data Assumptions that were made and Questions of Interest')
    st.write('Some assumptions that were made by the team was that higher calorie drinks would have higher amounts of sugar cholesterol and caffeine. We also assumed that Espressos woudl have the highest caffeine value. We wanted to see the comparison between drinks with how much caffeine along with if there were any correlation between drinks. We also wanted to figure out what the highest sugar drink was at starbucks')
with tab2:
    st.title('Is there a correlation between nutrient values?')
    st.altair_chart(scatter, use_container_width = True)
    st.altair_chart(fit_best)
    st.write("Correlation =" ,corr)
    st.write('As you can see the correlation is very strong which answers our theory that higher the calories are the more calories it is. You can also see the correlation value in the top left of the graph which is 0.922 which signals a strong correlation. :cool:')

    scatter3 = alt.Chart(data).mark_circle().encode(
    x=alt.X('Calories', title='Calories'),
    y=alt.Y('Total Carbohydrate(g)', title='Total Carbohydrates (g)'),
    color = 'Category',
    tooltip=['Category', 'Name', 'Size', 'Calories', 'Total Carbohydrate(g)']
).properties(
    title='Calories vs Total Carbohydrates',
    width = 600,
    height = 400
)
    st.altair_chart(scatter3, use_container_width = True)
    fit_best = scatter3 + scatter3.transform_regression('Calories', 'Total Carbohydrate(g)').mark_line()
    st.altair_chart(fit_best)
    corr = data[['Calories', 'Total Carbohydrate(g)']].corr().iloc[0,1]
    st.write("Correlation =", corr)
    st.write("The correlation between Carbohydrates and Calories are also positive. It is also a strong correlation meaning that the higher the calories the more carbohydrates there are. You can see the best fit line running through the graph and even with the outlying factors it still follows the same trend")
    sugar_chol = alt.Chart(data).mark_point().encode(
    x = 'Cholesterol(mg)',
    y = 'Sugars(g)', color = 'Category').properties(title ='Sugar vs Cholesterol', width = 600, height = 400)
    best_fit = sugar_chol + sugar_chol.transform_regression('Cholesterol(mg)', 'Sugars(g)').mark_line()
    st.altair_chart(best_fit)
    corr = data[['Cholesterol(mg)', 'Sugars(g)']].corr().iloc[0,1]
    st.write('Correlation =' , corr)
    st.write('The correlation here is very weak, just by looking at the graph you can see that the plots are all over the place. This means that higher sugar does *NOT* equate to higher cholesterol and vice versa. This still does not mean starbucks is healthy')

    fat = alt.Chart(data).mark_circle().encode(
        x = 'Calories',
        y = 'Total Fat(g)', color = 'Category').properties(title = 'Does Higher Calories = Higher Total Fat?', width = 600, height = 400)
    best_fitting = fat + fat.transform_regression('Calories', 'Total Fat(g)').mark_line()
    st.altair_chart(best_fitting)
    corr = data[['Calories', 'Total Fat(g)']].corr().iloc[0,1]
    st.write('The correlation is = ', corr)
    st.write('There is obviously some correlation here but not as strong as the other graphs we saw. Which shows that the majority of calories do not actually come from higher total fat, but seems to come from carbohydrates and sugar content of the drink')

    






with tab3:
    chart = alt.Chart(data).mark_bar().encode(
    x= 'Name',
    y='Calories',
    color="Name"
).properties(
    width=1200,
    height=400,
    title="Calories by Drink Name"
).interactive()
    st.altair_chart(chart, use_container_width = True)
    # Sort the data by sugar content and select the drink with the highest sugar content
    highest_sugar = data.sort_values('Sugars(g)', ascending=True).iloc[0]

# Create a bar chart showing the sugar content for each drink
    chart = alt.Chart(data).mark_bar().encode(
    x=alt.X('Name', sort='-y'),
    y='Sugars(g)',
    color=alt.condition(
        alt.datum.Name == highest_sugar['Name'],
        alt.value('orange'),
        alt.value('steelblue')
    )
).properties(
    title=f"Highest sugar drink: {highest_sugar['Name']}"
)
# Filter the DataFrame to only include espresso drinks
    espresso_df = data[data["Category"] == "espresso"]

# Sort the DataFrame by sugar content in descending order
    sorted_df = espresso_df.sort_values(by=["Sugars(g)"], ascending=False)

# Get the drink with the highest sugar content
    highest_sugar_drink = sorted_df.iloc[1]

# Print the name of the drink and its sugar content
    st.subheader('What has the highest sugar content within the espresso category?')
    st.write(highest_sugar_drink["Name"]+' is the highest sugar drink in the espresso category')
    st.write('it has ' , highest_sugar_drink["Sugars(g)"] ,' grams of sugar')


# In[92]:


# Sort the drinks by calories in descending order
    sorted_drinks = data.sort_values(by='Calories', ascending=False)

# Create a bar chart of the calories for each drink
    bars = alt.Chart(sorted_drinks).mark_bar().encode(
    x=alt.X('Calories:Q', title='Calories'),
    y=alt.Y('Category:O', sort=alt.EncodingSortField('Calories', order='descending'), title=None)
)

# Add a title and axis labels
    chart = bars.properties(
    title='Calories per Starbucks Category',
    width=600,
    height=400
).configure_axis(
    grid=False
)
    st.altair_chart(chart, use_container_width = True)

with tab4:
   st.title('Breakdown of Calories by Drink type')
   pie_chart = alt.Chart(data).mark_arc().encode(
    theta = "Calories",
    color = "Category")
   st.altair_chart(pie_chart)
   st.subheader('What category has the most caffeine?')
   pie_chart = alt.Chart(data).mark_arc().encode(theta = 'Caffeine(mg)', color = 'Category')
   st.altair_chart(pie_chart)



with tab5:
    st.title('Conclusion')
    st.write('From looking and analyzing the graphs we see that there are a multitude of different nutrients that go in your daily drinks from starbucks. We can see that the majority of high calorie drinks belong in frappucino drinks. We also see a strong correlation between calories and sugar which means if your drink is tasting a bit sweet it probably has a lot of *calories*')
    st.subheader('Is starbucks *unhealthy*?')
    st.write('It all depends on what you get, there are definitely drinks there that are much better for you such as a black coffee, but there are many varying factors such as size, sodium and more. If you need your extra kick to start your day off do not be afraid to do so.')






























