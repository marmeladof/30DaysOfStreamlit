import streamlit as st
import numpy as np
import pandas as pd

# data load

data_path = "data/"
data_file = "Online Retail.csv"
dim_country_file = "dim_country.csv"
data_df = pd.read_csv(data_path + data_file)
dim_country_df = pd.read_csv(data_path + dim_country_file)
data_df = pd.merge(data_df, dim_country_df, how = "left", on = "Country")
data_df["InvoiceDate"] = pd.to_datetime(data_df["InvoiceDate"],
                                        format = "%d/%m/%Y %H:%M")
data_df["InvoiceDay"] = pd.to_datetime(data_df["InvoiceDate"],
                                       format = "%d/%m/%Y %H:%M").dt.date

sales_df = data_df.loc[data_df["Quantity"] > 0]
returns_df = data_df.loc[data_df["Quantity"] <= 0]

region_ls = list(data_df["Region"].unique())
country_ls = list(data_df["Country"].unique())

st.write(data_df.head())

country_sales_df = sales_df.groupby(["InvoiceDay", "Region", "Country"],
                                    as_index = False) \
    .agg(totalQuantity = ("Quantity", np.sum),
         totalInvoices = ("InvoiceNo", pd.Series.nunique))
    
country_returns_df = sales_df.groupby(["InvoiceDay", "Region", "Country"],
                                      as_index = False) \
    .agg(totalQuantity = ("Quantity", np.sum),
         totalInvoices = ("InvoiceNo", pd.Series.nunique))

# dashboard

st.title("Online Retail Dashboard")

st.header("About", divider = True)
st.write("This dashboard uses the online retail data available from  \n" + \
         "https://archive.ics.uci.edu/dataset/352/online+retail")
    
st.header("Overview", divider = True)

st.write("In this section the data will be explored to gather high level " + \
         "insights and to understand the underlying distributions of the " + \
             "data that's available.")

with st.container():
    col1, col2 = st.columns(2)
    col1.write("**Number of records:**")
    col2.write("**Number of marketplaces:**")

with st.container():
    col1, col2 = st.columns(2)
    col1.write(len(data_df))
    col2.write(len(data_df["Country"].unique()))

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    col1.write("**Number of different products sold:**")
    col2.write("**Number of customers served:**")
    col3.write("**Number of units sold:**")
    col4.write("**Number of invoices generated:**")

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    col1.write(len(sales_df["StockCode"].unique()))
    col2.write(len(sales_df["CustomerID"].unique()))
    col3.write(sales_df["Quantity"].sum())
    col4.write(len(sales_df["InvoiceNo"].unique()))

st.header("Sales", divider = True)


region_options = st.multiselect("Selected regions:",
                                region_ls,
                                region_ls)

chart_data_idx = country_sales_df["Region"].isin(region_options)
chart_data = country_sales_df.loc[chart_data_idx, :].reset_index(drop = True)

with st.container():
    st.write("**Units Sold by Marketplace**")
    if len(region_options) > 0:
        st.line_chart(chart_data, x = "InvoiceDay", y =  "totalQuantity",
                      color = "Country")
    else:
        st.write("*Select a region to generate chart*")

with st.container():
    st.write("**Invoices Generated by Marketplace**")
    if len(region_options) > 0:
        st.line_chart(chart_data, x = "InvoiceDay", y =  "totalInvoices",
                      color = "Country")
    else:
        st.write("*Select a region to generate chart*")