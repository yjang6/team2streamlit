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
    st.write('Welcome to the project of team 2. Youngjin Jang, Geetha Ghulekar, Anantnaval Gaikwad, and Fernando Contreras-Juarez are the individuals who have contributed to this project.')
    st.subheader(':green[Inspiration]')
    st.write('We were inspired by coffee. Therefore, we thought, why not Starbucks, the most well-known coffee chain in the entire world. The majority of college students use a lot of caffeine, whether it is for early classes or studying late at night. College students consume a lot of coffee, and our campus even has its own Starbucks. In order to help you visualize what you are drinking, we decided to utilize it as inspiration and go inside to see what kind of nutrients are present.')
    st.subheader(':yellow[Goal]')
    st.write('This project was done to demonstrate to you how healthy or unhealthy  the drinks at Starbucks were. Information like  the amount of sugar, cholesterol, total calories, and other ingredients that are used were taken into account to make this analysis. I hope we were able to make that easy to visualize throughout this project.')
    st.subheader('Data Assumptions that were made and Questions of Interest')
    st.write('The team made some assumptions, such as that beverages with more calories would also include more sugar, cholesterol, and caffeine. Additionally, we assumed that espresso would contain the most caffeine. We were also interested in comparing the amounts of caffeine in various drinks as well as exploring whether there was a relationship between them. We also wanted to identify the Starbucks beverage with the most sugar.')
with tab2:
    st.title('Is there a correlation between nutrient values?')
    st.altair_chart(scatter, use_container_width = True)
    st.altair_chart(fit_best)
    st.write("Correlation =" ,corr)
    st.write('As you can see, there is a fairly strong correlation between the two, which supports our theory that foods with more sugar have higher calorie counts. Additionally, the correlation value of 0.922, which denotes a strong correlation, is visible in the graphs top left corner. :cool:')

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
    st.write("Carbohydrates and calories have a positive correlation as well. Additionally, there is a significant correlation between the two, so there are more carbohydrates the more calories there are. The best fit line can be seen crisscrossing the graph, and despite the outlying elements, it still exhibits the same pattern.")
    sugar_chol = alt.Chart(data).mark_point().encode(
    x = 'Cholesterol(mg)',
    y = 'Sugars(g)', color = 'Category').properties(title ='Sugar vs Cholesterol', width = 600, height = 400)
    best_fit = sugar_chol + sugar_chol.transform_regression('Cholesterol(mg)', 'Sugars(g)').mark_line()
    st.altair_chart(best_fit)
    corr = data[['Cholesterol(mg)', 'Sugars(g)']].corr().iloc[0,1]
    st.write('Correlation =' , corr)
    st.write('The link in this case is really shaky, and the plots are all over the place just by looking at the graph. Thus, a higher sugar intake does *NOT* translate into a higher cholesterol intake, and vice versa. This still does not imply that Starbucks is a healthy company.')

    fat = alt.Chart(data).mark_circle().encode(
        x = 'Calories',
        y = 'Total Fat(g)', color = 'Category').properties(title = 'Does Higher Calories = Higher Total Fat?', width = 600, height = 400)
    best_fitting = fat + fat.transform_regression('Calories', 'Total Fat(g)').mark_line()
    st.altair_chart(best_fitting)
    corr = data[['Calories', 'Total Fat(g)']].corr().iloc[0,1]
    st.write('The correlation is = ', corr)
    st.write('Clearly, there is some link present, but it is not as significant as it was in the previous plots. This demonstrates that the majority of calories do not actually come from more overall fat but rather from the beverage sugar and carbohydrate content.')

    






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
    st.subheader('What has the highest sugar content or calorie count within the espresso category?')
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
    st.write('We can tell from looking at and examining the graphs that there are many different nutrients that are included in your daily Starbucks cups. We can observe that the majority of calorie-dense beverages are appropriate for frappuccinos. Additionally, there is a significant correlation between calories and sugar, so if your beverage tastes a little sweet, it probably contains a lot of calories.')
    st.subheader('Is starbucks *unhealthy*?')
    st.write('It all depends on what you get, there are definitely drinks there that are much better for you such as a black coffee, but there are many varying factors such as size, sodium and more. Do not be afraid to take an extra boost in the morning if you need it.')






























