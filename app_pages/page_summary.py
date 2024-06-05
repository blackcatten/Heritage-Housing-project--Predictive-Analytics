import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def page_summary_body():

    image_main = plt.imread(f"media/sale.jpg")
    image_isu = plt.imread(f"media/sale.jpg")

    st.image(image_main, caption='Houses located in Ames, Iowa, USA')

    st.write("### Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Purpose and Motivation**\n\n"
        f" The general pupose of this project is to provide a tool that allows"
        f" a client to predict the potential sale price of a property in"
        f" Ames, Iowa, by providing detailed and typical information on the"
        f" real estate in question.\n\n"
        f" Specifically, a client has requested this app in order"
        f" to estimate the sale price for several inherited properties in "
        f" Ames, Iowa. The client has provided a publically available data set"
        f" which is used to train the machine learning model and "
        f" predict local real estate sale prices. \n \n"
        f"**Project Terminology**\n"
        f"* A **client** is a person who uses this service or product.\n"
        f"* The **sale price** is the estimated value of a home as it"
        f" might be realized in a typical and unencumbered real estate"
        f" transaction. \n"
        f"* The home, the value of which is being estimated, may be refered to"
        f" as **property, real estate, house, or home**. \n"
        f"* The **features** or **attributes** of a home are characteristics"
        f" used to describe the home. \n \n"
        f"**Project Dataset**\n"
        f"* The data set can be accessed at "
        f"[Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)"  # noqa
        f" where it is hosted by Code Institute.\n"
        f"* The dataset represents a record of approx. 1500 real estate "
        f" sales in Ames, Iowa. Each record contains 23 features indicating"
        f" the house profile, such as Floor Area, Basement, Garage, "
        f" Kitchen, Lot,"
        f" Porch, Wood Deck, and Year Built. It also contains the Sale Price."
        f" The features are extensive, so please visit the site for more"
        f" information.")

    # copied from README file - "Business Requirements" section
    st.success(
        f"**Business Requirements**\n\n"
        f"The project has 3 business requirements:\n"
        f"* 1. The client is interested in understanding the correlation "
        f" between a properties attributes/features and the sale price."
        f" Therefore, the client expects data visualization of the correlated"
        f" variables against the sale prices for illustration. \n"
        f"* 2. The client is interested in predicting the potential sale "
        f" prices"
        f" for properties in Ames, Iowa, and specifically, she wants to"
        f" determine a potential value for the properties she inherited. \n"
        f"* 3. The client would like to access the outcomes easily using"
        f" an online application."
    )

    # Link to README file, so the users can have access to full
    # project documentation
    st.write(
        f"* For additional information on this project please consult the "
        f"[README](https://github.com/blackcatten/Heritage-Housing-project--Predictive-Analytics/tree/main)")

   

