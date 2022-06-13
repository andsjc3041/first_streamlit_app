import streamlit

streamlit.title( 'My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🧁 Omega 3 & Blueberry')
streamlit.text('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🥝🍍Build Your Own Smoothie 🍌🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#add picklist
streamlit.multiselect('Pick some Fruits:', list(my_fruit_list.index), ['Avocado'], ['Strawberry'] )

#display
streamlit.dataframe(my_fruit_list)
