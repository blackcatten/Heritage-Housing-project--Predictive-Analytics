import plotly.express as px
import numpy as np
import streamlit as st
from src.data_management import load_house_prices_data
import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps
sns.set_style("whitegrid")


def page_sale_price_analysis_body():

    # load data
    df = load_house_prices_data()
    # The variable most strongly correlated with Sale Price/target
    vars_to_study = ['OverallQual', 'GrLivArea',
                     'GarageArea', 'TotalBsmtSF', 'YearBuilt', '1stFlrSF']

    st.write("### Property Sale Price Analysis")
    st.success(
        f"The client wants to analyze the house sales data "
        f"to identify the key factors that are most strongly associated with SalePrice. \n"
    )

    # inspect data
    if st.checkbox("Inspect Sale Price Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")
        st.write(df.head(10))
        st.write(
            f"**Information on Categorical Features**\n\n"
            f"* Basement Exposure: Gd - Good Exposure, Av - Average Exposure, "
            f" Mn - Minimum Exposure, "
            f" No - No Exposure, None - No Basement.\n\n"
            f"* Basement Finish Type: GLQ - Good Living Quarters, ALQ - "
            f" Average"
            f" Living Quarters, BLQ - Below Average Living Quarters, REC - "
            f" Average Rec Room, LwQ - Low  Quality, Unf - Unfinished, None - "
            f" No Basement.\n\n"
            f"* Garage Finish: Fin - Finished, RFn - Rough Finish, "
            f" Unf - Unfinished, None - No Garage.\n\n"
            f"* Kitchen Quality: Ex - Excellent, Gd - Good, TA - "
            f" Typical/Average, Fa - Fair, Po - Poor.\n\n"
            f"* Overall Condition: 1 - Very Poor to 10 - Very Excellent.\n\n"
            f"* Overall Quality: 1 - Very Poor to 10 - Very Excellent.\n\n"
        )

    st.write("---")

    st.write("### Correlation Study")
    # Correlation Study Summary
    st.write(
        f"To gain deeper insights, a correlation analysis was performed "
        f"to examine how the variables relate to Sale Price. \n"
        f"The following heatmaps present the Pearson and Spearman correlation results. "
        f"For clarity, the features with the strongest correlations to Sale Price "
        f"are also summarized in a bar plot for each correlation type. "
        f"These visualizations highlight that the variables most strongly associated with Sale Price are: **{vars_to_study}**. \n"
        f"As a further step, scatterplots are provided to show the relationship "
        f"between each of these variables and Sale Price."

    )

    st.info(
        f"*** Heatmap and Barplot: Pearson Correlation *** \n\n"
        f"The Pearson Correlation assesses the degree of linear association "
        f"between two continuous variables, showing how closely their relationship "
        f"can be approximated by a straight line. \n"
        f"In the heatmap, the final row identifies the variables on the x-axis "
        f"that exhibit a linear correlation with Sale Price greater than 0.6. "
        f"These variables are then visualized separately in a bar plot.")


    if st.checkbox("Pearson Correlation"):
        calc_display_pearson_corr_heat(df)
        calc_display_pearson_corr_bar(df)

    st.info(
        f"*** Heatmap and Barplot: Spearman Correlation ***  \n\n"
        f"The Spearman correlation examines how variables change together in a consistent, "
        f"but not necessarily linear, manner.\n"
        f"As with the Pearson correlation, the last row of the heatmap shows the variables "
        f"on the x-axis with a Spearman correlation of 0.6 or above with Sale Price. "
        f"These variables are also summarized in a bar plot for easier interpretation.")


    if st.checkbox("Spearman Correlation"):
        calc_display_spearman_corr_heat(df)
        calc_display_spearman_corr_bar(df)

    st.info(
        f"*** Correlation Histogram- and Scatterplots *** \n\n"
        f"The correlation indicators show that Sale Price is most closely related to the following factors: \n"
        f"* Sale Price tends to rise with better Overall Quality (OverallQual). \n"
        f"* An increase in Groundlevel Living Area (GrLivArea) generally leads to a higher Sale Price. \n"
        f"* Larger Garage Area (GarageArea) is associated with increased Sale Price. \n"
        f"* Higher Total Basement Area (TotalBsmtSF) usually corresponds to a higher Sale Price. \n"
        f"* Newer homes (YearBuilt) often command a higher Sale Price. \n"
        f"* More 1st Floor Squarefootage (1stFlrSF) is linked to a higher Sale Price. \n\n"
        f"To visualize these relationships, scatterplots are provided. "
        f"Initially, a two-dimensional histogram plot shows the overall data distribution, "
        f"with darker blue areas indicating where data points are more densely concentrated. "
        f"Following this, scatterplots with reddish shading illustrate how each variable correlates with Sale Price. "
        f"These plots also reveal that homes with better Overall Quality tend to have higher Sale Prices. "
        f"Points are color-coded by Overall Quality, with darker hues representing higher quality. "
        f"Overall, the scatterplots confirm that improving Overall Quality consistently leads to higher Sale Prices."

    )

    # Correlation plots adapted from the Data Cleaning Notebook
    if st.checkbox("Correlation Plots of Variables vs Sale Price"):
        correlation_to_sale_price_hist_scat(df, vars_to_study)

    st.info(
        f"*** Heatmap and Barplot: Predictive Power Score (PPS) ***  \n\n"
        f"The Predictive Power Score (PPS) measures both linear and non-linear relationships "
        f"between variables. \n"
        f"The PPS value ranges from 0, indicating no predictive power, to 1, representing perfect predictive power. \n"
        f"To interpret the plot, locate the row labeled 'SalePrice' on the y-axis. "
        f"Examine this row to identify variables on the x-axis with a PPS greater than 0.15. "
        f"Among these, Overall Quality (OverallQual) demonstrates the strongest predictive power for Sale Price.")


    if st.checkbox("Predictive Power Score"):
        calc_display_pps_matrix(df)


def correlation_to_sale_price_hist_scat(df, vars_to_study):
    """ Display correlation plot between variables and sale price """
    target_var = 'SalePrice'
    for col in vars_to_study:
        fig, axes = plt.subplots(figsize=(8, 5))
        axes = sns.histplot(data=df, x=col, y=target_var)
        plt.title(f"{col}", fontsize=20, y=1.05)
        st.pyplot(fig)
        st.write("\n\n")

        fig, axes = plt.subplots(figsize=(8, 5))
        axes = sns.scatterplot(data=df, x=col, y=target_var, hue='OverallQual')
        # plt.xticks(rotation=90)
        plt.title(f"{col}", fontsize=20, y=1.05)
        st.pyplot(fig)
        st.write("\n\n")


def calc_display_pearson_corr_heat(df):
    """ Calcuate and display Pearson Correlation """
    df_corr_pearson = df.corr(method="pearson")
    heatmap_corr(df=df_corr_pearson, threshold=0.6,
                 figsize=(12, 10), font_annot=10)


def calc_display_spearman_corr_heat(df):
    """ Calcuate and display Spearman Correlation """
    df_corr_spearman = df.corr(method="spearman")
    heatmap_corr(df=df_corr_spearman, threshold=0.6,
                 figsize=(12, 10), font_annot=10)


def calc_display_pearson_corr_bar(df):
    """ Calcuate and display Pearson Correlation """
    corr_pearson = df.corr(method='pearson')['SalePrice'].sort_values(
        key=abs, ascending=False)[1:]
    fig, axes = plt.subplots(figsize=(6, 3))
    axes = plt.bar(x=corr_pearson[:5].index, height=corr_pearson[:5])
    plt.title("Pearson Correlation with Sale Price", fontsize=15, y=1.05)
    st.pyplot(fig)


def calc_display_spearman_corr_bar(df):
    """ Calcuate and display Spearman Correlation """
    corr_spearman = df.corr(method='spearman')['SalePrice'].sort_values(
        key=abs, ascending=False)[1:]
    fig, axes = plt.subplots(figsize=(6, 3))
    axes = plt.bar(x=corr_spearman[:5].index, height=corr_spearman[:5])
    plt.title("Spearman Correlation with Sale Price", fontsize=15, y=1.05)
    st.pyplot(fig)


def calc_display_pps_matrix(df):
    """ Calcuate and display Predictive Power Score """
    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(
        columns='x', index='y', values='ppscore')
    heatmap_pps(df=pps_matrix, threshold=0.15, figsize=(12, 10), font_annot=10)

    pps_topscores = pps_matrix.iloc[19].sort_values(
        key=abs, ascending=False)[1:6]

    fig, axes = plt.subplots(figsize=(6, 3))
    axes = plt.bar(x=pps_topscores.index, height=pps_topscores)
    plt.xticks(rotation=90)
    plt.title("Predictive Power Score for Sale Price", fontsize=15, y=1.05)
    st.pyplot(fig)


def heatmap_corr(df, threshold, figsize=(20, 12), font_annot=8):
    """ Heatmap for correlations from CI template"""
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=bool)
        mask[np.triu_indices_from(mask)] = True
        mask[abs(df) < threshold] = True
        fig, axes = plt.subplots(figsize=figsize)
        axes = sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                           mask=mask, cmap='viridis',
                           annot_kws={"size": font_annot},
                           ax=axes, linewidth=0.5
                           )
        axes.set_yticklabels(df.columns, rotation=0)
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)


def heatmap_pps(df, threshold, figsize=(20, 12), font_annot=8):
    """ Heatmap for predictive power score from CI template"""
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=bool)
        mask[abs(df) < threshold] = True
        fig, axes = plt.subplots(figsize=figsize)
        axes = sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                           mask=mask, cmap='rocket_r',
                           annot_kws={"size": font_annot},
                           linewidth=0.05, linecolor='grey')
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)