#import dependencies
import streamlit as st
import pandas as pd

# import data
d={'Type':['Notebook','DVDs'],'Qty':[2,3],'Price':[100,200]}

df=pd.DataFrame(data=d)
st.dataframe(df)