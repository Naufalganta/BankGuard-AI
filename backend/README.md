# 🛡️ BankGuard AI

> AI-powered Banking Security Log Analyzer using NVIDIA Llama 3.3 and FastAPI.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green)
![NVIDIA](https://img.shields.io/badge/NVIDIA-Llama%203.3-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Overview

BankGuard AI is a web-based Banking Security Log Analyzer powered by Large Language Models (LLM). The system analyzes security logs, detects potential cyber threats, assesses security risks, and generates intelligent recommendations to help security analysts respond to incidents more efficiently.

---

## ✨ Features

- 📂 Upload Security Log (.log, .txt, .csv)
- 🤖 AI-powered Log Analysis using NVIDIA Llama 3.3
- 🚨 Threat Detection
- 📊 Risk Assessment (LOW, MEDIUM, HIGH, CRITICAL)
- 📜 Analysis History
- 📄 PDF Report Generation
- 💾 SQLite Database
- 🌐 FastAPI Web Application

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| AI Model | NVIDIA Llama 3.3 70B |
| Database | SQLite |
| Template Engine | Jinja2 |
| Frontend | HTML, Tailwind CSS |
| PDF | ReportLab |
| Server | Uvicorn |

---

## 📂 Project Structure

```text
LLM/
│
├── backend/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── static/
│   ├── templates/
│   ├── .env.example
│   ├── config.py
│   ├── main.py
│   └── requirements.txt
│
├── LICENSE
└── README.md
```

---

## ⚙️ Installation

Clone repository

```bash
git clone https://github.com/Naufalganta/BankGuard-AI.git
```

Go to project

```bash
cd BankGuard-AI/backend
```

Create virtual environment

```bash
python -m venv venv
```

Linux / macOS

```bash
source venv/bin/activate
```

Windows

```powershell
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create `.env`

```env
NVIDIA_API_KEY=YOUR_NVIDIA_API_KEY
```

---

## ▶️ Run Application

```bash
python -m uvicorn main:app --reload
```

Open browser

```
http://127.0.0.1:8000
```

---

## 📸 Screenshots

### Dashboard

> *(Add screenshot here after UI redesign)*

### AI Analysis

> *(Add screenshot here after analysis result)*

### History

> *(Add screenshot here after history page)*

---

## 👨‍💻 Developer

**Moh Ade Ersa Nanda**

---

## 📄 License

This project is licensed under the MIT License.