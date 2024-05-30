import streamlit as st 
# streamlet se data apps ban jate hai 
import pandas as pd 
st.title('Amazon Analysis')

show_button=st.button('Show Data')
#read the data only once a cached function  
@st.cache_resource
def load_data():
    return pd.read_csv('Superstore.csv')

df = load_data()
if show_button:
    st.dataframe(df)

#function to get top n categories based on profit
def top(category, n):
    df=load_data()
    result=df.groupby(category).agg(
        highest_profit=('Profit','sum')
    ).sort_values('highest_profit', ascending=False).head(n)
    
st.header('Top N Category Profit')

cat=st.text_input('Enter the Category you want:')
topn=int(st.number_input('Top N', min_value=1,value=1,step=1))    

calculate=st.button('Calculate')
if calculate:
    var=top(cat, topn)
    st.dataframe(var)
    #plotting the bar chart
    st.bar_chart(var)
