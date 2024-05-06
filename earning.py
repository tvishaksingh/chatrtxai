from time import time_ns
import rtx_api_3_5 as rtx_api
import streamlit as st 
import os
from openbb import obb
import pandas as pd


if __name__ == '__main__':

    company_name = input("Enter company name: ")
    transformed_input = [
            f"Summarizing the key points from the earnings call transcript of {company_name}?",
            f"Please Extract financial metrics from the {company_name} call into a table, list, etc.",
            f"Quickly find out the risks, challenges, and opportunities mentioned in the calli of {company_name}?",
            f"Analyzing the overall sentiment of the earnings call of {company_name}?",
            f"What are the main questions asked by analysts in the earnings call transcript of {company_name}?",
            f"Summarize key takeaways from the most recent earnings call of  {company_name}?",
            "Identify the financial ratios highlighted during the earnings call and their implications.",
            "Discuss how the latest earnings results compare with Wall Street's expectations.",
            "Evaluate the impact of [Company Name]'s most recent earnings call on its stock price.",
            "Extract a summary of quarter-over-quarter (QoQ) and year-over-year (YoY) performance metrics from the latest earnings call",
            "Summarize the revenue streams discussed in the latest earnings call",
            "Discuss the implications of changes in gross margin as mentioned in the latest earnings call",
            "Identify any mentions of cost-cutting or operational efficiency measures.",
            "Analyze any changes in operating income and their potential causes in the last earnings call",
            "Extract mentions of free cash flow and its impact on the business in the last earnings call",
            "Discuss the company's budgeting and forecasting approaches mentioned in the earnings call.",
            "Extract any mentions of scenario planning or sensitivity analysis.",
            "Identify the metrics used for financial planning and their significance.",
            "Discuss any updates on return on investment (ROI) from the latest earnings call.",
        ]
    for query in transformed_input:
        print(query)
        out = rtx_api.send_message(query)
        print(out + "\n")
