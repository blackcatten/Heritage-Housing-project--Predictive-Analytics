import streamlit as st

def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from "02 - Churned Customer Study" notebook
    st.success(
        f"We propose that a property's sale price is strongly related "
        f"to a subset of the numerous features in the dataset. \n\n"
        f"* The correlation analysis of the dataset supports this hypothesis. \n\n"
        f"We believe that the strongest correlations are with typical home features "
        f"such as total square footage, overall condition, and overall quality. \n\n"
        f"* The correlation study validated this, revealing that Sale Price "
        f"has the strongest correlations with Overall Quality (OverallQual), "
        f"Groundlevel Living Area (GrLivArea), Garage Area (GarageArea), "
        f"Total Basement Area (TotalBsmtSF), Year Built (YearBuilt), and "
        f"1st Floor Squarefootage (1stFlrSF). These features are common to most properties. \n\n"
        f"We hypothesize that it is possible to predict the Sale Price with an "
        f"R² value of at least 0.8. \n\n"
        f"* The R² analysis for both training and test sets confirms this expectation."
    )
