# 💰 AI Personal Finance Analyzer

<p align="center">
  <b>Analyze spending. Track financial health. Make smarter money decisions.</b>
</p>

<p align="center">
  Built with ❤️ by <b>mkcamara</b><br>
  Instagram: <a href="https://instagram.com/mkcamara_offical">@mkcamara_offical</a>
</p>

---

## 🚀 Overview

AI Personal Finance Analyzer is a lightweight financial intelligence API that:

- Automatically categorizes transactions
- Calculates income, expenses, and net balance
- Generates financial insights
- Provides actionable saving advice
- Works fully offline (no heavy AI models)

This project focuses on **real-world problem solving** — helping individuals understand and improve their financial behavior.

---

## 🎯 The Problem

Most people:
- Don’t know where their money goes
- Overspend without realizing it
- Lack structured financial insights
- Have no measurable financial health indicator

This system solves that.

---

## ⚙️ Tech Stack

- **FastAPI**
- **Python**
- **Pandas**
- **Rule-based Intelligence Engine**
- **Uvicorn**

Lightweight. Fast. Production-ready.

---

## 🧠 Features

✅ Transaction categorization  
✅ Income vs expense breakdown  
✅ Net balance calculation  
✅ Spending insights  
✅ Financial advice engine  
✅ REST API (Swagger documentation included)  

---

## 📸 Demo

### API Running

![API Demo](https://media.giphy.com/media/l0HlQ7LRalQqdWfao/giphy.gif)

### Swagger Documentation

![Swagger Demo](https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif)

> Replace these GIFs later with your own screen recording for maximum professionalism.

---

## 📂 Project Structure

```

ai-personal-finance-analyzer/
│
├── app/
│   ├── main.py
│   ├── analyzer.py
│   └── categorizer.py
│
├── data/
│   └── sample_transactions.csv
│
├── requirements.txt
├── .gitignore
└── README.md

````

---

## 🧪 How To Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ai-personal-finance-analyzer.git
cd ai-personal-finance-analyzer
````

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start server

```bash
uvicorn app.main:app --reload
```

### 5️⃣ Open in browser

```
http://127.0.0.1:8000/docs
```

---

## 📊 Example Output

```json
{
  "total_income": 4800,
  "total_expense": -2422.51,
  "net_balance": 2377.49,
  "category_breakdown": {
    "shopping": -821.88,
    "transport": -100.25,
    "food": -94.1
  },
  "advice": [
    "Your spending is under control."
  ]
}
```

---

## 🔮 Future Improvements

* Financial Health Score (0–100)
* Monthly cashflow prediction
* Spending visualization dashboard
* AI-driven smart saving recommendations
* Web dashboard interface

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Connect

GitHub: [https://github.com/mkcamara-ai](https://github.com/mkcamara-ai)
Instagram: [https://instagram.com/mkcamara_offical](https://instagram.com/mkcamara_offical)

---

<p align="center">
  <b>Building real-world AI systems that solve real problems.</b>
</p>
