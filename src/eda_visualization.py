import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Resolve paths relative to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'cleaned_poll_data.csv')
PLOTS_DIR = os.path.join(BASE_DIR, 'plots')


def main():
    # Create plots folder
    os.makedirs(PLOTS_DIR, exist_ok=True)

    # Load dataset
    if not os.path.exists(DATA_PATH):
        print(f"[ERROR] Cleaned data not found at: {DATA_PATH}")
        print("   Run 'python src/preprocess.py' first.")
        return

    df = pd.read_csv(DATA_PATH)
    print(f"[INFO] Loaded {len(df)} rows from cleaned_poll_data.csv")

    # -------------------------------
    # 1. Bar Chart – Preferred Tools
    # -------------------------------
    plt.figure(figsize=(8, 5))
    sns.countplot(x='Preferred Tool', data=df, hue='Preferred Tool', palette='Set2', legend=False)
    plt.title('Most Preferred Tools')
    plt.xlabel('Tool')
    plt.ylabel('Number of Votes')
    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.savefig(os.path.join(PLOTS_DIR, "preferred_tools_bar_chart.png"))
    plt.close()
    print(f"[OK] Saved: preferred_tools_bar_chart.png")

    # ---------------------------------------
    # 2. Histogram – Satisfaction Distribution
    # ---------------------------------------
    plt.figure(figsize=(6, 4))
    sns.histplot(df['Satisfaction (1-5)'], bins=5, kde=True, color='skyblue')
    plt.title('Satisfaction Rating Distribution')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.tight_layout()

    plt.savefig(os.path.join(PLOTS_DIR, "satisfaction_histogram.png"))
    plt.close()
    print(f"[OK] Saved: satisfaction_histogram.png")

    # -----------------------------------
    # 3. Line Plot – Daily Poll Responses
    # -----------------------------------
    # Use the pre-computed 'Date' column from preprocessing
    daily = df.groupby('Date').size()
    daily.index = pd.to_datetime(daily.index, format='%d-%m-%Y')
    daily = daily.sort_index()
    daily.index = daily.index.strftime('%d-%m-%Y')

    plt.figure(figsize=(8, 4))
    daily.plot(kind='line', marker='o')
    plt.title('Daily Poll Submissions')
    plt.xlabel('Date')
    plt.ylabel('Number of Responses')
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(os.path.join(PLOTS_DIR, "daily_responses_line_chart.png"))
    plt.close()
    print(f"[OK] Saved: daily_responses_line_chart.png")

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

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Common Words in Feedback")

    plt.savefig(os.path.join(PLOTS_DIR, "feedback_wordcloud.png"))
    plt.close()
    print(f"[OK] Saved: feedback_wordcloud.png")

    # -----------------------------------
    # 5. Boxplot – Feedback Length vs Rating
    # -----------------------------------
    # Use the pre-computed 'Feedback Length' column from preprocessing
    plt.figure(figsize=(7, 5))
    sns.boxplot(x='Satisfaction (1-5)', y='Feedback Length', data=df, hue='Satisfaction (1-5)', palette='coolwarm', legend=False)
    plt.title('Feedback Length by Satisfaction Level')
    plt.tight_layout()

    plt.savefig(os.path.join(PLOTS_DIR, "feedback_length_boxplot.png"))
    plt.close()
    print(f"[OK] Saved: feedback_length_boxplot.png")

    # -----------------------------------
    # 6. Gender vs Preferred Tool
    # -----------------------------------
    plt.figure(figsize=(8, 5))

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

    plt.savefig(os.path.join(PLOTS_DIR, "gender_vs_tool.png"))
    plt.close()
    print(f"[OK] Saved: gender_vs_tool.png")

    # -----------------------------------
    # 7. Heatmap: Gender vs Preferred Tool
    # -----------------------------------
    gender_tool = pd.crosstab(df["Gender"], df["Preferred Tool"])

    plt.figure(figsize=(8, 5))

    sns.heatmap(
        gender_tool,
        annot=True,
        cmap="YlGnBu",
        fmt="d"
    )

    plt.title("Gender vs Preferred Tool")
    plt.xlabel("Preferred Tool")
    plt.ylabel("Gender")
    plt.tight_layout()

    plt.savefig(os.path.join(PLOTS_DIR, "gender_tool_heatmap.png"))
    plt.close()
    print(f"[OK] Saved: gender_tool_heatmap.png")

    # -----------------------------------
    # 8. Age Group vs Preferred Tool
    # -----------------------------------
    plt.figure(figsize=(8, 5))

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

    plt.savefig(os.path.join(PLOTS_DIR, "age_group_vs_tool.png"))
    plt.close()
    print("[OK] Saved: age_group_vs_tool.png")

    print("\n[DONE] All 8 plots saved inside the 'plots/' folder.")


if __name__ == "__main__":
    main()