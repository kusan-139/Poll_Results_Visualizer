# 📊 Poll Results Visualizer

A **Data Science project** that collects, cleans, analyzes, and visualizes poll or survey data.
The project generates multiple charts, performs exploratory data analysis (EDA), and deploys an **interactive dashboard using Streamlit**.

This project demonstrates a **complete data pipeline** similar to real-world survey analytics systems used by platforms like Google Forms, SurveyMonkey, and Qualtrics.

---

# 🚀 Project Features

* Poll dataset analysis using **pandas**
* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Automatic **plot generation and saving**
* Word cloud visualization for feedback
* Gender vs tool preference analysis
* Interactive **Streamlit dashboard**
* Organized project structure

---

# 📁 Project Structure

```
poll_results_visualizer/
│
├── data/
│   ├── poll_data.csv                # Raw dataset (900+ responses)
│   └── cleaned_poll_data.csv       # Cleaned dataset after preprocessing
│
├── plots/                          # All generated charts saved here
│   ├── preferred_tools_bar_chart.png
│   ├── satisfaction_histogram.png
│   ├── daily_responses_line_chart.png
│   ├── feedback_wordcloud.png
│   ├── feedback_length_boxplot.png
│   ├── gender_vs_tool.png
│   └── gender_tool_heatmap.png
│
├── src/
│   ├── preprocess.py               # Data cleaning & preprocessing
│   └── eda_visualization.py        # EDA + chart generation
│
├── app.py                          # Streamlit dashboard
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation
```

---

# 📊 Dataset Information

The dataset contains poll responses with the following columns:

| Column             | Description               |
| ------------------ | ------------------------- |
| Timestamp          | Date and time of response |
| Age Group          | Respondent age category   |
| Gender             | Gender of respondent      |
| Preferred Tool     | Favorite data tool        |
| Satisfaction (1-5) | Rating from 1–5           |
| Feedback           | Text feedback from users  |

During preprocessing an additional column is created:

| Generated Column | Description             |
| ---------------- | ----------------------- |
| Feedback Length  | Length of feedback text |

---

# ⚙️ Installation

Clone or download the project and install dependencies.

```bash
pip install -r requirements.txt
```

Dependencies include:

* pandas
* numpy
* matplotlib
* seaborn
* wordcloud
* streamlit
* plotly (optional)
* nltk / scikit-learn (optional)

---

# ▶️ Running the Project

## Step 1 — Data Preprocessing

Clean the dataset and generate additional features.

```bash
python src/preprocess.py
```

Output generated:

```
data/cleaned_poll_data.csv
```

New features created:

* Date extracted from timestamp
* Feedback Length

---

## Step 2 — Exploratory Data Analysis (EDA)

Generate charts and save them into the **plots folder**.

```bash
python src/eda_visualization.py
```

The script automatically creates:

```
plots/
```

Charts generated:

* Preferred tools bar chart
* Satisfaction rating histogram
* Daily response trend line chart
* Feedback word cloud
* Feedback length vs satisfaction boxplot
* Gender vs tool preference chart
* Gender vs tool heatmap

---

## Step 3 — Launch Interactive Dashboard

Run the Streamlit app.

```bash
python -m streamlit run app.py
```

Open the dashboard in your browser:

```
http://localhost:8501
```

Dashboard features:

* Dataset preview
* Tool preference chart
* Satisfaction distribution
* Response trends
* Feedback word cloud
* Interactive filtering

---

# 📈 Example Insights

Using this project you can answer questions like:

* Which data tool is most popular?
* What is the average satisfaction rating?
* How do preferences differ by gender?
* Are responses increasing over time?
* What keywords appear most in feedback?

---

# 🧠 Skills Demonstrated

This project demonstrates key **Data Science skills**:

* Data cleaning & preprocessing
* Exploratory data analysis
* Data visualization
* Feature engineering
* Dashboard development
* Python data ecosystem

---

# 🌍 Real World Applications

Similar pipelines are used in:

* Market research surveys
* Employee feedback analysis
* Product satisfaction tracking
* Educational course feedback
* Public opinion polling

---

# 📌 Technologies Used

* Python
* pandas
* numpy
* matplotlib
* seaborn
* wordcloud
* Streamlit

---

# 👤 Author

**Kusan Chakraborty**
B.Tech – Computer Science & Engineering (Data Science)

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to:

- Use
- Modify
- Distribute

This software, provided proper credit is given to the author.

© 2026 Kusan Chakraborty
