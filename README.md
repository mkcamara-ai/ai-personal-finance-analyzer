# 💰 AI Personal Finance Analyzer

<p align="center">
  <b>Analyze spending. Track financial health. Make smarter financial decisions.</b>
</p>

<p align="center">
  Built by <b>mkcamara</b><br>
  Instagram: <a href="https://instagram.com/mkcamara_offical">@mkcamara_offical</a>
</p>

---

## 🚀 Overview

AI Personal Finance Analyzer is a lightweight financial intelligence API designed to help individuals understand their spending behavior and improve financial decision-making.

The system:

- Automatically categorizes transactions
- Calculates income, expenses, and net balance
- Generates financial insights
- Provides actionable saving recommendations
- Runs fully offline (no heavy AI models)

This project focuses on solving a real-world problem: lack of financial awareness.

---

## 🎯 The Problem

Many people:

- Do not track where their money goes
- Overspend without clear visibility
- Lack structured financial insights
- Have no measurable financial health indicator

This system provides clarity and structured analysis.

---

## ⚙️ Tech Stack

- **Python**
- **FastAPI**
- **Pandas**
- **Rule-Based Intelligence Engine**
- **Uvicorn**

Lightweight. Fast. Production-ready.

---

## 🧠 Core Features

- Transaction categorization engine
- Income vs expense breakdown
- Net balance calculation
- Category-level spending summary
- Financial advice generation
- REST API with Swagger documentation

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

## 🧪 Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-personal-finance-analyzer.git
cd ai-personal-finance-analyzer
````

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the server

```bash
uvicorn app.main:app --reload
```

### 5. Open in browser

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
    "entertainment": -53.98,
    "food": -94.10,
    "other": -552.30,
    "salary": 4000,
    "shopping": -821.88,
    "transport": -100.25
  },
  "advice": [
    "Your spending is under control."
  ]
}
```

---

## 🔮 Future Improvements

* Financial health scoring system (0–100)
* Monthly cash flow prediction
* Spending visualization dashboard
* Smarter recommendation engine
* Web-based user interface

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Connect

GitHub: [https://github.com/mkcamara-ai](https://github.com/mkcamara-ai)
Instagram: [https://instagram.com/mkcamara_offical](https://instagram.com/mkcamara_offical)

---

<p align="center">
  Building real-world systems that solve real financial problems.
</p>
