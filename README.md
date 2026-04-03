# 🌍 Gender Attitudes Explorer

Interactive dashboard built with **Python, Streamlit and Plotly** to explore gender-related attitudes across European countries using survey data.

👉 **Live app:**  
https://gender-attitudes-explorer.streamlit.app/

---

## 📊 Project Overview

This application allows users to explore how individuals perceive gender roles, equality, and social norms across Europe.

It is based on microdata from the **European Social Survey (ESS)** and focuses on:

- attitudes toward gender equality
- perceptions of fairness and discrimination
- support for gender-related policies
- beliefs and social norms

The app enables dynamic exploration by:

- variable selection
- comparison by gender
- comparison by country
- comparison by age group

---

## ⚙️ Features

- Interactive visualizations (Plotly)
- Clean and responsive layout (Streamlit)
- Variable descriptions integrated in the interface
- Multiple comparison views:
  - by gender
  - by country
  - by gender and country
  - by age and gender

---

## 🧠 Analytical Approach

The project is based on:

- recoding and harmonization of survey variables
- handling missing values based on codebook
- transformation into categorical/ordinal formats
- descriptive statistical analysis
- comparative visualization

---

## 📁 Data

Source: **European Social Survey (ESS)**

The dataset was pre-processed to:
- clean missing values
- recode variables according to official codebooks
- generate labelled variables (`_lab`)

---

## 🛠️ Tech Stack

- Python
- Pandas
- Plotly
- Streamlit

---

## 🚀 How to run locally

```bash
git clone https://github.com/adrianacera80-byte/gender-attitudes-explorer.git
cd gender-attitudes-explorer
pip install -r requirements.txt
streamlit run app.py
