import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def page_summary_body():

    image_main = plt.imread(f"media/sale.jpg")
    image_isu = plt.imread(f"media/sale.jpg")

    st.image(image_main, caption='Houses located in Ames, Iowa, USA')

    st.write("### Project Summary")

    st.info(
        f"**Project Purpose and Motivation**\n\n"
        f" The primary purpose of this project is to create a tool that "
        f"enables clients to predict the potential sale price of properties"
        f" in Ames, Iowa, by providing detailed and typical information about"
        f" the real estate in question. Specifically, a client has requested"
        f" this app to estimate the sale prices for several inherited properties "
        f"in Ames, Iowa. The client has supplied a publicly available dataset, "
        f"which is used to train the machine learning model to predict local "
        f"real estate sale prices."
        f"**Project Terminology**\n\n"
        f"- **Client**: A person who uses this service or product."
        f"- **Sale Price**: The estimated value of a home as it"
        f" might be realized in a typical and unencumbered real estate transaction."
        f"- **Property/Real Estate/House/Home**: Terms used interchangeably to"
        f" refer to the home whose value is being estimated."
        f"- **Features/Attributes**: Characteristics used to describe the home."
        f"**Project Dataset**"
        f"- The dataset can be accessed at"
        f" [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)"
        f" where it is hosted by Code Institute."
        f"- The dataset includes records of approximately 1,500 real estate sales"
        f" in Ames, Iowa. Each record contains 23 features detailing the house profile,"
        f"such as Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, and Year"
        f" Built. It also includes the Sale Price. The dataset's features are extensive,"
        f" and more information can be found on the Kaggle site."
    )

    st.success(
        f"**Business Requirements**\n\n"
        f"The project has 3 business requirements:\n"
        f"1. **Correlation Study**: The client is interested"
        f" in understanding the correlation between a property's "
        f"attributes/features and the sale price. Therefore, the"
        f"client expects data visualization of the correlated "
        f"variables against the sale prices for illustration."
        f"2. **Sale Price Prediction**: The client wants to predict"
        f" potential sale prices for properties in Ames, Iowa, and "
        f"specifically determine the potential value of the "
        f"properties she inherited."
        f"3. **Online Application**: The client would like to access"
        f" the outcomes easily through an online application."
    )

    # Link to README file

    st.write(
        f"* For additional information on this project please consult the "
        f"[README](https://github.com/blackcatten/Heritage-Housing-project--Predictive-Analytics/tree/main)")


