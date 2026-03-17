import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(page_title="SaaS Revenue & Churn Dashboard", layout="wide")

@st.cache_data
def load_data():
    if not os.path.exists('data/customers.csv'):
        import generate_data
        generate_data.main()
    df = pd.read_csv('data/customers.csv')
    df['signup_date'] = pd.to_datetime(df['signup_date'])
    df['churn_date'] = pd.to_datetime(df['churn_date'])
    return df

df = load_data()

st.title("SaaS Revenue & Churn Analytics")
st.caption("Built by Vidit Malhotra | Python · Streamlit · Plotly · Pandas")

st.sidebar.header("Filters")
segments = st.sidebar.multiselect("Segment", options=df['segment'].unique(), default=list(df['segment'].unique()))
industries = st.sidebar.multiselect("Industry", options=df['industry'].unique(), default=list(df['industry'].unique()))
status_filter = st.sidebar.radio("Customer status", ["All", "Active", "Churned"])

filtered = df[df['segment'].isin(segments) & df['industry'].isin(industries)]
if status_filter != "All":
    filtered = filtered[filtered['status'] == status_filter]

active = filtered[filtered['status'] == 'Active']
churned = filtered[filtered['status'] == 'Churned']

total_arr = active['arr'].sum()
total_customers = len(active)
churn_rate = len(churned) / len(filtered) * 100 if len(filtered) > 0 else 0
avg_arr = active['arr'].mean() if len(active) > 0 else 0
nrr = ((active['arr'].sum() + active['expansion_arr'].sum()) / active['arr'].sum() * 100) if active['arr'].sum() > 0 else 0
avg_ltv = (active['mrr'].mean() / (churn_rate / 100)) if churn_rate > 0 else 0

st.subheader("Key metrics")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total ARR", f"£{total_arr:,.0f}", delta="Active customers only")
c2.metric("Active customers", f"{total_customers:,}")
c3.metric("Churn rate", f"{churn_rate:.1f}%")
c4.metric("Net revenue retention", f"{nrr:.1f}%")
c5.metric("Avg customer LTV", f"£{avg_ltv:,.0f}")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("ARR by segment")
    arr_seg = active.groupby('segment')['arr'].sum().reset_index()
    fig = px.bar(arr_seg, x='segment', y='arr', color='segment',
                 color_discrete_map={'SMB':'#534AB7','Mid-Market':'#378ADD','Enterprise':'#1D9E75'},
                 labels={'arr':'ARR (£)','segment':'Segment'})
    fig.update_layout(showlegend=False, height=320, margin=dict(t=20,b=20))
    fig.update_yaxes(tickprefix="£", tickformat=",")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Churn rate by segment")
    churn_seg = filtered.groupby('segment').apply(
        lambda x: (x['status'] == 'Churned').sum() / len(x) * 100
    ).reset_index()
    churn_seg.columns = ['segment', 'churn_rate']
    fig2 = px.bar(churn_seg, x='segment', y='churn_rate', color='segment',
                  color_discrete_map={'SMB':'#534AB7','Mid-Market':'#378ADD','Enterprise':'#1D9E75'},
                  labels={'churn_rate':'Churn rate (%)','segment':'Segment'})
    fig2.update_layout(showlegend=False, height=320, margin=dict(t=20,b=20))
    fig2.update_yaxes(ticksuffix="%")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
col3, col4 = st.columns(2)

with col3:
    st.subheader("Monthly churn trend")
    churned_trend = churned.copy()
    churned_trend['churn_month'] = churned_trend['churn_date'].dt.to_period('M').astype(str)
    monthly_churn = churned_trend.groupby('churn_month').size().reset_index(name='churned_customers')
    fig3 = px.line(monthly_churn, x='churn_month', y='churned_customers',
                   labels={'churn_month':'Month','churned_customers':'Customers churned'},
                   markers=True, line_shape='spline')
    fig3.update_traces(line_color='#E24B4A')
    fig3.update_layout(height=320, margin=dict(t=20,b=20))
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("ARR distribution")
    fig4 = px.histogram(active, x='arr', color='segment', nbins=40,
                        color_discrete_map={'SMB':'#534AB7','Mid-Market':'#378ADD','Enterprise':'#1D9E75'},
                        labels={'arr':'ARR (£)','count':'Customers'})
    fig4.update_layout(height=320, margin=dict(t=20,b=20), bargap=0.1)
    fig4.update_xaxes(tickprefix="£", tickformat=",")
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
col5, col6 = st.columns(2)

with col5:
    st.subheader("NPS score vs churn risk")
    fig5 = px.scatter(filtered, x='nps_score', y='support_tickets',
                      color='status', size='arr',
                      color_discrete_map={'Active':'#1D9E75','Churned':'#E24B4A'},
                      labels={'nps_score':'NPS score','support_tickets':'Support tickets','arr':'ARR'},
                      opacity=0.7)
    fig5.update_layout(height=320, margin=dict(t=20,b=20))
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    st.subheader("Revenue by industry")
    ind_arr = active.groupby('industry')['arr'].sum().sort_values(ascending=True).reset_index()
    fig6 = px.bar(ind_arr, x='arr', y='industry', orientation='h',
                  labels={'arr':'Total ARR (£)','industry':'Industry'},
                  color_discrete_sequence=['#378ADD'])
    fig6.update_layout(height=320, margin=dict(t=20,b=20))
    fig6.update_xaxes(tickprefix="£", tickformat=",")
    st.plotly_chart(fig6, use_container_width=True)

st.markdown("---")
st.subheader("Customer records")
st.dataframe(
    filtered[['customer_id','segment','industry','plan','arr','mrr','status','signup_date','churn_date','nps_score','support_tickets']].sort_values('arr', ascending=False),
    use_container_width=True,
    height=350
)

st.caption("Data is synthetically generated for portfolio demonstration purposes.")
