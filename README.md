# 📊 Smart Investment Decision Support System

A beginner-friendly data visualization tool that helps users compare stocks, analyze risk vs return, and make smarter investment decisions using real-time market data.

---

## 🚀 Overview

The **Smart Investment Decision Support System** is an interactive dashboard designed to simplify stock analysis. It enables users to select multiple NSE stocks and visualize their performance using intuitive charts and metrics.

This project focuses on making financial data **easy to understand**, especially for beginners who struggle with complex investment platforms.

---

## ✨ Features

- 📊 Real-time stock data using Yahoo Finance  
- 📈 Price trend visualization (line charts)  
- ⚖️ Risk vs Return analysis (annualized volatility)  
- 📊 Returns comparison (bar charts)  
- 🟢 Portfolio allocation (pie chart)  
- 📌 KPI dashboard (avg return, risk, best performer)  
- 🎯 Beginner-friendly investment insights  
- ⚙️ Dynamic NSE stock selection  

---

## 🖼️ Demo

> Add screenshots of your app here  
> (Dashboard, Charts, Portfolio View)

---

## 🛠️ Tech Stack

- **Frontend/UI:** Streamlit  
- **Backend:** Python  
- **Data Source:** Yahoo Finance (`yfinance`)  
- **Data Processing:** Pandas, NumPy  
- **Visualization:** Plotly  

---

## 📂 Project Structure
Investment_Analyzer/
 - app.py
 - nse_stock_clean.csv
 - requirements.txt
 -  README.md


---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/investment-analyzer.git

# Navigate to project folder
cd investment-analyzer

# Create virtual environment (optional)
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

```

🎯 Use Case

Helps beginners understand stock performance
Enables quick comparison of multiple assets
Supports basic portfolio decision-making

⚠️ Challenges 

Fetching reliable NSE stock data
Cleaning and formatting stock symbols
Handling missing or empty datasets
Implementing accurate risk calculations
Designing an intuitive UI for better user experience


🔮 Future Scope
🤖 AI-based investment recommendations
📊 Portfolio optimization algorithms
🌍 Multi-market support (US, Crypto)
📱 Full web/mobile deployment
🧠 Personalized investment suggestions


📌 Disclaimer

This project is for educational purposes only and does not provide financial advice.
