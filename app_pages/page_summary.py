import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


def page_summary_body():

    image_main = plt.imread(f"media/sale.jpg")
    image_isu = plt.imread(f"media/sale.jpg")

    st.image(image_main, caption='Houses located in Ames, Iowa, USA')

    st.write("### Project Summary")

    st.info(
        f"**Project Terms & Jargon**\n\n"
        f"The primary purpose of this project is to create"
        f"a tool that enables clients to predict"
        f" the potential sale price of properties in Ames,"
        f"Iowa,by providing detailed and typical"
        f"information about the real estate in question."
        f"Specifically, a client has requested this app to"
        f"estimate the sale prices for several inherited "
        f"properties in Ames, Iowa. The client has"
        f"supplied a publicly available dataset, which is"
        f"used to train the machine learning model to"
        f"predict local real estate sale prices. \n \n"



        f"* **Client:** A person who uses this service.\n"
        f"* **Sale Price:** The estimated value of a home"
        f"as it might be realized in a typical and unencumbered"
        f"real estate transaction.\n"
        f"* **Property/Real Estate/House/Home:** Terms used"
        f"interchangeably to refer to the home whose value"
        f"is being estimated.\n "
        f"* **Features/Attributes:** Characteristics used "
        f"to describe the home.\n\n \n"
        f"**Project Dataset**\n"
        f"* The dataset can be accessed at"
        f"[Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)"  # noqa
        f"where it is hosted by Code Institute. \n"
        f"* The dataset includes records of approximately "
        f"1,500 real estate sales in"
        f"Ames, Iowa. Each record contains 23 features"
        f"detailing the house profile,such as Floor"
        f"Area, Basement, Garage, Kitchen, Lot, Porch, "
        f"Wood Deck, and Year Built. It also includes"
        f"the Sale Price. The dataset's features are extensive,"
        f"and more information can be found"
        f"on the Kaggle site."
    )

    st.success(
        f"**Business Requirements**"
        f"The project has three business requirements:\n"
        f"* 1. **Correlation Study:** The client"
        f"wants to analyze the correlation between a  "
        f"property's attributes/features and its sale price."
        f"This involves providing data  "
        f"visualizations that illustrate the relationship"
        f"between these variables and sale prices.\n"
        f"* 2. **Sale Price Prediction:** The client"
        f"seeks to predict potential sale prices for "
        f"properties in Ames, Iowa, with a specific "
        f"focus on estimating the value of "
        f"inherited properties. ?n"
        f"* 3. **Online Application:** The client"
        f"wishes to access the results conveniently  "
        f"through an online application. \n"
    )

    # Link to README file

    st.write(
        f"* For additional information on this project please consult the "
        f"[README](https://github.com/blackcatten/Heritage-Housing-project--Predictive-Analytics/tree/main)")  # noqa
