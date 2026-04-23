import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Poll Results Visualizer",
    page_icon="📊",
    layout="wide"
)

# ─── Load Data ───────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv('data/cleaned_poll_data.csv')
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Date'] = df['Timestamp'].dt.strftime('%d-%m-%Y')
    return df

df = load_data()

# ─── Title ───────────────────────────────────────────────────────────────────
st.title("📊 Poll Results Visualizer")
st.markdown("Interactive dashboard for exploring poll survey data.")
st.markdown("---")

# ─── Sidebar Filters ─────────────────────────────────────────────────────────
st.sidebar.header("🔍 Filters")

selected_tools = st.sidebar.multiselect(
    "Preferred Tool",
    options=df['Preferred Tool'].unique(),
    default=df['Preferred Tool'].unique()
)

selected_genders = st.sidebar.multiselect(
    "Gender",
    options=df['Gender'].unique(),
    default=df['Gender'].unique()
)

selected_ages = st.sidebar.multiselect(
    "Age Group",
    options=df['Age Group'].unique(),
    default=df['Age Group'].unique()
)

# Apply filters
filtered_df = df[
    df['Preferred Tool'].isin(selected_tools) &
    df['Gender'].isin(selected_genders) &
    df['Age Group'].isin(selected_ages)
]

# ─── KPI Cards ───────────────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Responses", len(filtered_df))
col2.metric(
    "Avg Satisfaction",
    f"{filtered_df['Satisfaction (1-5)'].mean():.2f} / 5" if len(filtered_df) > 0 else "N/A"
)
col3.metric(
    "Most Popular Tool",
    filtered_df['Preferred Tool'].mode()[0] if len(filtered_df) > 0 else "N/A"
)
col4.metric(
    "Avg Feedback Length",
    f"{filtered_df['Feedback Length'].mean():.0f} chars" if len(filtered_df) > 0 else "N/A"
)

st.markdown("---")

# ─── Raw Data ────────────────────────────────────────────────────────────────
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df, use_container_width=True)
    st.markdown("---")

# ─── Preferred Tool Votes ────────────────────────────────────────────────────
st.subheader("🛠️ Preferred Tool Votes")
tool_counts = filtered_df["Preferred Tool"].value_counts().reset_index()
tool_counts.columns = ["Tool", "Votes"]

fig_tools = px.bar(
    tool_counts,
    x="Tool",
    y="Votes",
    color="Tool",
    title="Comparison Between Tools",
    text="Votes",
)
st.plotly_chart(fig_tools, use_container_width=True)

st.markdown("---")

# ─── Satisfaction Distribution ───────────────────────────────────────────────
st.subheader("⭐ Satisfaction Distribution")
fig_sat = px.histogram(
    filtered_df,
    x="Satisfaction (1-5)",
    nbins=5,
    color="Satisfaction (1-5)",
    title="Satisfaction Rating Distribution",
    text_auto=True
)
fig_sat.update_layout(
    xaxis_title="Satisfaction Rating",
    yaxis_title="Number of Responses"
)
st.plotly_chart(fig_sat, use_container_width=True)

st.markdown("---")

# ─── Responses Over Time ─────────────────────────────────────────────────────
st.subheader("📅 Responses Over Time")
# Uses filtered_df so the chart respects sidebar filters
daily = filtered_df.groupby('Date').size().reset_index(name='Responses')
daily['Date_DT'] = pd.to_datetime(daily['Date'], format='%d-%m-%Y')
daily = daily.sort_values('Date_DT')
fig_line = px.line(
    daily,
    x='Date',
    y='Responses',
    markers=True,
    title="Daily Poll Submissions"
)
st.plotly_chart(fig_line, use_container_width=True)

st.markdown("---")

# ─── Feedback Word Cloud ─────────────────────────────────────────────────────
st.subheader("💬 Feedback Word Cloud")
text = " ".join(filtered_df["Feedback"].dropna().astype(str))
if text.strip():
    wordcloud = WordCloud(
        width=900,
        height=450,
        background_color="white",
        colormap="viridis",
        max_words=100
    ).generate(text)
    fig_wc, ax_wc = plt.subplots(figsize=(10, 5))
    ax_wc.imshow(wordcloud, interpolation="bilinear")
    ax_wc.axis("off")
    st.pyplot(fig_wc, use_container_width=True)
else:
    st.warning("No feedback available to generate word cloud.")

st.markdown("---")

# ─── Gender vs Preferred Tool ────────────────────────────────────────────────
st.subheader("👥 Gender vs Preferred Tool")
gender_tool_bar = (
    filtered_df.groupby(["Preferred Tool", "Gender"])
    .size()
    .reset_index(name="Votes")
)
fig_gender = px.bar(
    gender_tool_bar,
    x="Preferred Tool",
    y="Votes",
    color="Gender",
    barmode="group",
    title="Tool Preference by Gender",
    text="Votes"
)
st.plotly_chart(fig_gender, use_container_width=True)

st.markdown("---")

# ─── Gender vs Tool Heatmap ──────────────────────────────────────────────────
st.subheader("🌡️ Gender vs Tool Heatmap")
gender_tool_pivot = pd.crosstab(
    filtered_df["Gender"],
    filtered_df["Preferred Tool"]
)
fig_heat = px.imshow(
    gender_tool_pivot,
    text_auto=True,
    color_continuous_scale="YlGnBu",
    aspect="auto",
    labels=dict(x="Preferred Tool", y="Gender", color="Votes"),
    title="Gender vs Tool Preference Heatmap"
)
st.plotly_chart(fig_heat, use_container_width=True)

st.markdown("---")

# ─── Age Group vs Preferred Tool ────────────────────────────────────────────
st.subheader("🎂 Age Group vs Preferred Tool")
age_tool = (
    filtered_df.groupby(["Preferred Tool", "Age Group"])
    .size()
    .reset_index(name="Votes")
)
fig_age = px.bar(
    age_tool,
    x="Preferred Tool",
    y="Votes",
    color="Age Group",
    barmode="group",
    title="Tool Preference by Age Group",
    text="Votes"
)
fig_age.update_layout(
    xaxis_title="Preferred Tool",
    yaxis_title="Number of Votes"
)
st.plotly_chart(fig_age, use_container_width=True)

st.markdown("---")

# ─── Satisfaction by Age Group ───────────────────────────────────────────────
st.subheader("📊 Satisfaction by Age Group")
fig_sat_age = px.box(
    filtered_df,
    x="Age Group",
    y="Satisfaction (1-5)",
    color="Age Group",
    title="Satisfaction Score Distribution by Age Group",
    points="all"
)
fig_sat_age.update_layout(
    xaxis_title="Age Group",
    yaxis_title="Satisfaction Rating (1-5)"
)
st.plotly_chart(fig_sat_age, use_container_width=True)