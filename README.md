# 🏥 Hybrid Patient Monitoring System using Machine Learning

## 📌 Overview
This project presents a **hybrid patient monitoring system** that integrates **rule-based clinical thresholds** with **unsupervised machine learning** to detect patient deterioration in real time.

The system is designed to **maximize patient safety** while **minimizing false alarms**, a critical challenge in modern clinical monitoring environments.

A separate deployment demo using **Flask and a web-based dashboard** is available in a dedicated branch.

---

## 🎯 Key Objectives
- Continuous monitoring of patient vital signs  
- Early detection of abnormal physiological patterns  
- Reduction of false alerts using hybrid decision logic  
- Clear separation between ML logic and deployment code  

---

## 🧠 System Architecture

### 1️⃣ Data Layer
- Simulated physiological signals:
  - Heart Rate  
  - SpO₂  
  - Body Temperature  
- Labeled scenarios:
  - Normal  
  - Deterioration  
  - Emergency  

### 2️⃣ Intelligence Layer
- Rule-based clinical threshold evaluation  
- Unsupervised anomaly detection using **Isolation Forest**  
- Hybrid decision engine combining rules and ML outputs  

### 3️⃣ Evaluation & Output Layer
- Alert generation and logging  
- Performance metrics:
  - Precision  
  - Recall  
  - F1-score  

---

## ⚙️ Machine Learning Approach

| Component | Description |
|--------|------------|
| Model Type | Unsupervised Anomaly Detection |
| Algorithm | Isolation Forest |
| Training Strategy | Trained only on normal physiological data |
| Features Used | Heart Rate, SpO₂, Temperature |

### Why Unsupervised Learning?
- Medical anomaly labels are scarce and expensive  
- Better generalization to unseen patient conditions  
- Reduced dependency on manual annotation  

---

## 🚨 Hybrid Alert Logic
An alert is generated if:

- Any **rule-based clinical threshold** is violated  
**OR**  
- The ML model detects **persistent anomalous behavior over time**

This ensures:
- **Safety** through deterministic rules  
- **Adaptability** through machine learning  

---

## 📊 Performance Summary
Hybrid model evaluation achieved:

- **Precision:** ~0.93  
- **Recall:** ~0.86  
- **F1-Score:** ~0.90  

These results demonstrate **effective anomaly detection** with **reduced false positives**.

---

## 🌿 Repository Structure & Branching Strategy

### `main` branch
Contains:
- Core machine learning implementation  
- Hybrid alert logic  
- Evaluation scripts  
- Data simulation utilities  

Does **NOT** contain:
- Flask application  
- Web UI files  

---

### `demo-ui` branch
Contains:
- Flask REST API (`app.py`)  
- Web dashboard (HTML, CSS, JavaScript)  
- Live charts and alert visualization  
- Audio alert simulation  

This separation keeps the main branch **clean, modular, and submission-ready**.

---

## 🖥️ Demo (Optional)
To run the interactive web demo:

```bash
git checkout demo-ui
pip install -r requirements.txt
python src/app.py
