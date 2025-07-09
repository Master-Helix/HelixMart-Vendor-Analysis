# HelixMart-Vendor-Analysis
This is a Data Analytics project targeted towards in depth analysis of various vendors and their performance registered on HelixMart 

## 📂 Repository Overview

This repository provides an end-to-end workflow for analyzing vendor transactions, including:

- Data cleansing and preparation
- Descriptive and diagnostic analysis
- Vendor statistical performance metrics
- Visualizations (Bar, Donut, Box plots)
- Actionable business insights using a Power BI Dashbaord
- Final Presentation showcasing key insights to stakeholders

---

## 📌 Project Objectives

- Identify top-performing vendors by purchase and sales contribution.
- Analyze unit purchase prices relative to order sizes.
- Evaluate stock turnover and unsold inventory.
- Generate actionable recommendations for supply chain diversification and inventory optimization.

---
## 📂 Dataset Link 
  - The raw csv files used in this project can be directly accesed using my drive link - https://drive.google.com/file/d/1B7pe6ziyPPaTX0_ecKBEUw3CYGOLbRwd/view?usp=sharing
  - These data files then can be ingested into the inventory database which we have created using the 'ingestion_db_script'.


---

## 🛠️ Tech Stack

- **Dataset:**  CSV Files (Excel workbooks)
- **Language:** Python (Pandas, NumPy)
- **Visualization:** Matplotlib, Seaborn
- **Database:** PostgreSQL
- **Reporting:** Power BI

---

## ✅ Steps to Perform Analysis

Below is the recommended sequence for running the analysis end-to-end:

1. **Data Ingestion:**
   - Run the 'ingestion_db_script.py' first in the Jupyter environment.
   - This loads raw vendor transaction dataset (utilised from the link above) into the internal create inventory.db database using SQLite engine.
   - This helps in storing the .csv files as dataframes inside the 'ingestion.db' database we have created.
   - Also check the timed logs for better time tracking in the respective named log files created inside the logs folder.


2. **Data Cleaning:**
   - Remove outliers and inconsistent data points
   - Execute and explore the specific cells in the 'Exploratory_Data_Analysis' notebook to get insights related to data inconsistencies present inside the data and how to clean it.
  
3. **Creating Custom Data Table for in-depth Vendor Analysis:**
   - Run the 'get_vendor_summary_script.py' to create a required and useful custom data table from the tables stored inside the inventory database.
   - Performing SQL Queries with CTE's to optimise loading efficiencies and get targeted columns and insights to finally create a summarised table named as 'vendor_sales_summary.csv'
   - Also check the timed logs for better time tracking in the respective named log files created inside the logs folder.

4. **Data Processing:**
   - Calculate aggregate metrics: Total Purchase Dollars, Gross Profit, Total Sales Dollars.
   - Compute derived columns: Unit Purchase Price, Order Size bins.
   - Solving key research questions which can be seen in detail in the notebook file named as 'Vendor_Performance_Analysis'.
   - Plotted various graphs like boxplot, bar graph, scatter plot, correlation heatmap and donut chart to showcase better insights towards the respective business case problems.

5. **Reporting:**
   - Build interactive Power BI dashboards.
   - Add dynamic filters to highlight top vendors.
   - Annotate charts with total contributions.

6. **Generate Business Insights:**
   - Interpret and collected key insights in a presentable document.
   - Document key findings and actionable recommendations to key stakeholders.

---

## 📈 Key Insights

- Top 10 vendors contribute ~65% of total purchases, indicating potential supply chain risks.
- Bulk purchasing reduces unit price significantly (~72% reduction).
- Slow-moving inventory ties up $2.71M in capital, highlighting a need for better turnover management.

---

## ✔️ Recommendations

- Diversify vendor base to mitigate supply chain risks.
- Leverage bulk discounts strategically.
- Optimize slow-moving inventory with clearance strategies.
- Enhance marketing for low-performing vendors.

---

## 🤝 Contribution

Contributions are welcome! Feel free to point out any improvements and if you liked it, hit a star and brighten up the repo!

---

## 📜 License

This project is licensed under the MIT License.

---

