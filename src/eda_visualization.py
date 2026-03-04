import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Create plots folder
os.makedirs("plots", exist_ok=True)

# Load dataset
df = pd.read_csv("data/cleaned_poll_data.csv")

# -------------------------------
# 1. Bar Chart – Preferred Tools
# -------------------------------
plt.figure(figsize=(8,5))
sns.countplot(x='Preferred Tool', data=df, palette='Set2')
plt.title('Most Preferred Tools')
plt.xlabel('Tool')
plt.ylabel('Number of Votes')
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("plots/preferred_tools_bar_chart.png")
plt.close()


# ---------------------------------------
# 2. Histogram – Satisfaction Distribution
# ---------------------------------------
plt.figure(figsize=(6,4))
sns.histplot(df['Satisfaction (1-5)'], bins=5, kde=True, color='skyblue')
plt.title('Satisfaction Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.tight_layout()

plt.savefig("plots/satisfaction_histogram.png")
plt.close()


# -----------------------------------
# 3. Line Plot – Daily Poll Responses
# -----------------------------------
df['Date'] = pd.to_datetime(df['Timestamp']).dt.date
daily = df.groupby('Date').size()

plt.figure(figsize=(8,4))
daily.plot(kind='line', marker='o')
plt.title('Daily Poll Submissions')
plt.xlabel('Date')
plt.ylabel('Number of Responses')
plt.grid(True)
plt.tight_layout()

plt.savefig("plots/daily_responses_line_chart.png")
plt.close()


# -----------------------------------
# 4. Word Cloud – Feedback Text
# -----------------------------------
text = " ".join(df['Feedback'].astype(str))

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    colormap='tab10'
).generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Common Words in Feedback")

plt.savefig("plots/feedback_wordcloud.png")
plt.close()


# -----------------------------------
# 5. Boxplot – Feedback Length vs Rating
# -----------------------------------
df['Feedback Length'] = df['Feedback'].astype(str).apply(len)

plt.figure(figsize=(7,5))
sns.boxplot(x='Satisfaction (1-5)', y='Feedback Length', data=df, palette='coolwarm')
plt.title('Feedback Length by Satisfaction Level')
plt.tight_layout()

plt.savefig("plots/feedback_length_boxplot.png")
plt.close()

print("✅ All plots saved inside the 'plots/' folder.")

# -----------------------------------
# 6. Gender vs Preferred Tool
# -----------------------------------

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="Preferred Tool",
    hue="Gender",
    palette="Set1"
)

plt.title("Tool Preference by Gender")
plt.xlabel("Preferred Tool")
plt.ylabel("Number of Votes")
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("plots/gender_vs_tool.png")
plt.close()

# -----------------------------------
#7. Heatmap: Gender vs Preferred Tool
# -----------------------------------

gender_tool = pd.crosstab(df["Gender"], df["Preferred Tool"])

plt.figure(figsize=(8,5))

sns.heatmap(
    gender_tool,
    annot=True,
    cmap="YlGnBu",
    fmt="d"
)

plt.title("Gender vs Preferred Tool")
plt.xlabel("Preferred Tool")

# ----------------------------------
# 8. Age Group vs Preferred Tool
# -----------------------------------

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="Preferred Tool",
    hue="Age Group",
    palette="Set2"
)

plt.title("Tool Preference by Age Group")
plt.xlabel("Preferred Tool")
plt.ylabel("Number of Votes")
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("plots/age_group_vs_tool.png")
plt.close()
plt.ylabel("Gender")

plt.tight_layout()

plt.savefig("plots/gender_tool_heatmap.png")
plt.close()
