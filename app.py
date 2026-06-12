import streamlit as st, pandas as pd, plotly.express as px
st.set_page_config(page_title="APAC Airline Executive Dashboard",layout="wide")
st.title("✈️ APAC Airline Executive Dashboard (2015–2025)")
st.caption("Shreya Patle | IBR Final Review")
st.sidebar.title("Navigation")
page=st.sidebar.radio("Go to",["Overview","Trends","Statistics","Regression","Recommendations","Learnings"])
if page=="Overview":
 st.metric('Years',11); st.metric('Airlines',30); st.metric('R²',0.71)
 st.info('Operational efficiency emerged as the strongest determinant of profitability.')
elif page=="Trends":
 data={'Year':[2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025],'FSC':[2.8,3.2,3.8,4.1,4.5,-18.2,-45.8,-2,4.8,6.2,6.8],'LCC':[4.2,4.8,5.1,5.3,5.5,-42.5,-62.3,-8.5,5.2,7.1,7.8]}
 df=pd.DataFrame(data)
 fig=px.line(df,x='Year',y=['FSC','LCC'],markers=True,title='Net Profit Ratio')
 st.plotly_chart(fig,use_container_width=True)
 st.success('Growth → Pandemic → Recovery → Stabilisation')
elif page=="Statistics":
 st.table(pd.DataFrame({'Metric':['NPR','OM','ROA','D/E'],'Mean':[-4.71,-2.74,0.41,3.77]}))
elif page=="Regression":
 st.metric('R²',0.71); st.write('Operating Margin β=0.77 ✔️')
 st.write('ROA β=0.01')
 st.write('Debt-to-Equity β=-0.40')
elif page=="Recommendations":
 st.subheader('FSC'); st.write('Subscription memberships, cargo integration, AI disruption management')
 st.subheader('LCC'); st.write('Digital ecosystems, ancillary revenues, flexible capacity')
else:
 st.write('Profitability is driven by efficiency, not just revenue.')
 st.write('Data-driven decisions improve resilience.')
