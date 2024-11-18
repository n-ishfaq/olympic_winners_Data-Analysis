#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import os
import time

def prepare_data(filepath):
    df = pd.read_excel(filepath, skiprows=1 ,engine="openpyxl")
    df.columns = ["Age", "Silver", "Bronze", "Athlete", "Date", "Gold", "Sport", "Country"]
    df['Gold'] = pd.to_numeric(df['Gold'], errors='coerce').fillna(0).astype(int)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
   
    return df


def create_pie_chart(df):
    selected=st.selectbox("Select the Gold,Silver,Bronze to filter with",["Gold","Silver","Bronze"])
    if selected=="Gold":
     gold_counts = df.groupby("Athlete")['Gold'].sum()
     gold_counts = gold_counts[gold_counts > 0]
     fig,ax=plt.subplots(figsize=(10,10))
     gold_counts.plot(kind="pie",
                     autopct="%.0f%%",  
                     figsize=(10, 10),  
                     wedgeprops=dict(width=0.9),  
                     pctdistance=0.85)
     plt.title("Gold Medal Distribution Among Athletes", fontweight="bold")  
    
     st.pyplot(fig)
    elif selected=="Silver":
     silver_counts = df.groupby("Athlete")['Silver'].sum()
     silver_counts = silver_counts[silver_counts > 0]
     fig,ax=plt.subplots(figsize=(10,10))
     silver_counts.plot(kind="pie",
                     autopct="%.0f%%",  
                     figsize=(10, 10),  
                     wedgeprops=dict(width=0.9),  
                     pctdistance=0.85)
     plt.title("Gold Medal Distribution Among Athletes", fontweight="bold")  
    
     st.pyplot(fig)
    plt.show()
def animated_bar_graph(data):
    data.set_index('Date', inplace=True)
    data= data.groupby([data.index, 'Athlete'])['Gold'].sum().groupby(level=1).cumsum().unstack().fillna(0)
    st.dataframe(data)
    # Select top 20 athletes with the most gold medals
    selected = data.iloc[-1].sort_values(ascending=False)[:20].index
    data = data[selected].round()
    max_value = data.max().max()

    # Create a Streamlit container for updating the animation
    placeholder = st.empty()

    # Loop through each frame
    for i in range(data.shape[0]):
        fig, ax = plt.subplots(figsize=(9.3, 5))
        ax.set_xlim(0, max_value * 1.1)  # Set x-axis limit
        bars = sns.barplot(y=data.columns, x=data.iloc[i], orient="h", ax=ax)
        ax.set_title(f"Gold Medals Over Time - Date: {data.index[i].date()}", fontsize=14)
        ax.set_xlabel("Gold Medals")
        ax.set_ylabel("Athletes")

        # Add bar value annotations
        for j, bar in enumerate(bars.patches):
            bar_value = data.iloc[i, j]
            ax.text(bar_value + max_value * 0.01, j, f"{bar_value:.0f}", va="center")

        # Display the figure in Streamlit
        with placeholder:
            st.pyplot(fig)

        # Pause for a short time before moving to the next frame
        time.sleep(0.2)
        plt.close(fig)


uploaded_file = st.file_uploader("Upload Olympic Data File", type=["xlsx"])
if uploaded_file:  # Ensure a file is uploaded
    df=prepare_data(uploaded_file)
    create_pie_chart(df)
    try:
        animated_bar_graph(df)
    except Exception as e:
        st.error(f"An error occuresd as {e}")







