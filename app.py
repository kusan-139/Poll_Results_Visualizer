
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import plotly.express as px

df = pd.read_csv('data/cleaned_poll_data.csv')

st.title("Poll Results Visualizer")

st.sidebar.header("Filters")
tool = st.sidebar.multiselect(
    "Preferred Tool",
    df['Preferred Tool'].unique(),
    default=df['Preferred Tool'].unique()
)

filtered_df = df[df['Preferred Tool'].isin(tool)]

if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)

st.markdown("---")
st.subheader("Preferred Tool Votes")
tool_counts = filtered_df["Preferred Tool"].value_counts().reset_index()
tool_counts.columns = ["Tool", "Votes"]

fig = px.bar(
    tool_counts,
    x="Tool",
    y="Votes",
    color="Tool",
    title="Comparison Between Tools",
    text="Votes",
)
st.plotly_chart(fig, use_container_width=True)


st.markdown("---")
st.subheader("Satisfaction Distribution")
fig = px.histogram(
    filtered_df,
    x="Satisfaction (1-5)",
    nbins=5,
    color="Satisfaction (1-5)",
    title="Satisfaction Rating Distribution",
    text_auto=True
)
fig.update_layout(
    xaxis_title="Satisfaction Rating",
    yaxis_title="Number of Responses"
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("Responses Over Time")
df['Date'] = pd.to_datetime(df['Timestamp']).dt.date
daily = df.groupby('Date').size()
st.line_chart(daily)

st.markdown("---")
st.subheader("Feedback Word Cloud")

text = " ".join(filtered_df["Feedback"].dropna().astype(str))
if text:
    wordcloud = WordCloud(
        width=900,
        height=450,
        background_color="white",
        colormap="viridis",
        max_words=100
    ).generate(text)
    fig_wc, ax_wc = plt.subplots(figsize=(10,5))
    ax_wc.imshow(wordcloud, interpolation="bilinear")
    ax_wc.axis("off")
    st.pyplot(fig_wc, use_container_width=True)
else:
    st.warning("No feedback available to generate word cloud.")

st.markdown("---")
st.subheader("Gender vs Preferred Tool")

gender_tool = (
    filtered_df.groupby(["Preferred Tool", "Gender"])
    .size()
    .reset_index(name="Votes")
)

fig = px.bar(
    gender_tool,
    x="Preferred Tool",
    y="Votes",
    color="Gender",
    barmode="group",
    title="Tool Preference by Gender",
    text="Votes"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("Gender vs Tool Heatmap")

gender_tool = pd.crosstab(
    filtered_df["Gender"],
    filtered_df["Preferred Tool"]
)

fig_heat = px.imshow(
    gender_tool,
    text_auto=True,
    color_continuous_scale="YlGnBu",
    aspect="auto",
    labels=dict(x="Preferred Tool", y="Gender", color="Votes"),
)

fig_heat.update_layout(
    title="Gender vs Tool Preference"
)

st.plotly_chart(fig_heat, use_container_width=True)