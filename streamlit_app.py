import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title( 'My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🧁 Omega 3 & Blueberry')
streamlit.text('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🥝🍍Build Your Own Smoothie 🍌🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#add picklist
fruits_selected = streamlit.multiselect('Pick some Fruits:', list(my_fruit_list.index), ['Avocado','Strawberries'] )
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display
streamlit.dataframe(fruits_to_show)

#New section to display fruityvice API response
streamlit.header('Fruity Fruit Advice!') 

#create the repeatable code block
def get_fruityvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return fruityvice_normalized

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
  else:      
      back_from_function = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
 # except URLError as e: e.error()
except: ("Test") 

      
#stop executing past here while troubleshooting
#streamlit.stop()

#Snowflake related functions
def get_fruit_laod_list():
      with my_cnx.cursor() as my_cur:
            my_cur.execute("select * from fruit_load_list")
            return my_cur.fetchall()

#Add a buntton to load to fruit
if streamlit.button('Get Fruit Load List'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      my_data_rows = get_fruit_laod_list()
      my_cnx.close()
      streamlit.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
      with my_cnx.cursor() as my_cur:
            my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
#            my_cur.execute("insert into fruit_load_list values ('from streamlit2')")
            return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')      
if streamlit.button('Add a Fruit to the List'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      back_from_function = insert_row_snowflake(add_my_fruit)
#      streamlit.text(back_from_function)
      
      

      #import snowflake.connector
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_row = my_cur.fetchall()
#streamlit.header("The fruit load list contains: ")
#streamlit.dataframe(my_data_row)

#add_my_fruit = streamlit.text_input('What fruit would you like to add?','')
#streamlit.write('Thanks for adding ', add_my_fruit)
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")
