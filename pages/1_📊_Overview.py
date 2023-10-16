import streamlit as st
import numpy as np
import pandas as pd

# data load

data_path = "data/"
data_file = "Online Retail.csv"
dim_country_file = "dim_country.csv"
data_df = pd.read_csv(data_path + data_file)
dim_country_df = pd.read_csv(data_path + dim_country_file)
dim_country_dict = dim_country_df.groupby("Region")["Country"].apply(list) \
    .to_dict()
data_df = pd.merge(data_df, dim_country_df, how = "left", on = "Country")
data_df["InvoiceDate"] = pd.to_datetime(data_df["InvoiceDate"],
                                        format = "%d/%m/%Y %H:%M")
data_df["InvoiceDay"] = pd.to_datetime(data_df["InvoiceDate"],
                                       format = "%d/%m/%Y %H:%M").dt.date
data_df["InvoiceLineTotal"] = data_df["Quantity"] * data_df["UnitPrice"]

sales_df = data_df.loc[data_df["Quantity"] > 0]
returns_df = data_df.loc[data_df["Quantity"] <= 0]

region_ls = list(data_df["Region"].unique())
country_ls = list(data_df["Country"].unique())

country_sales_df = sales_df.groupby(["InvoiceDay", "Region", "Country"],
                                    as_index = False) \
    .agg(totalQuantity = ("Quantity", np.sum),
         totalInvoices = ("InvoiceNo", pd.Series.nunique),
         totalInvoicesGBP = ("InvoiceLineTotal", np.sum))
    
country_returns_df = sales_df.groupby(["InvoiceDay", "Region", "Country"],
                                      as_index = False) \
      .agg(totalQuantity = ("Quantity", np.sum),
           totalInvoices = ("InvoiceNo", pd.Series.nunique),
           totalInvoicesGBP = ("InvoiceLineTotal", np.sum))

# overview

st.set_page_config(page_title = "Overview",
                   page_icon = ":bar_chart:")
    
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