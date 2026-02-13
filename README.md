# 🏥 Patient Monitoring System using Hybrid ML Approach

## 📌 Overview
This project implements a **hybrid patient monitoring system** that combines **rule-based clinical thresholds** with **unsupervised machine learning** to detect patient deterioration in real time.  
The system is designed to **reduce false alarms** while maintaining **high sensitivity** to critical conditions.

A separate deployment demo using **Flask and a web dashboard** is provided in a dedicated branch.

---

## 🎯 Key Objectives
- Continuous monitoring of patient vital signs
- Early detection of abnormal physiological patterns
- Reduction of false alerts through hybrid decision logic
- Clear separation between core ML logic and deployment code

---

## 🧠 System Architecture
The system consists of three layers:

1. **Data Layer**
   - Simulated physiological data (heart rate, SpO₂, temperature)
   - Labeled scenarios: normal, deterioration, emergency

2. **Intelligence Layer**
   - Rule-based evaluation using clinical thresholds
   - Unsupervised anomaly detection using Isolation Forest
   - Hybrid decision mechanism combining both approaches

3. **Evaluation & Output Layer**
   - Performance metrics (precision, recall, F1-score)
   - Alert generation and logging

---

## ⚙️ Machine Learning Approach
- **Model Type:** Unsupervised anomaly detection  
- **Algorithm:** Isolation Forest  
- **Training Strategy:** Trained only on normal physiological data  
- **Features Used:**  
  - Heart Rate  
  - SpO₂  
  - Temperature  

### Why Unsupervised Learning?
- Medical anomaly labels are scarce and costly
- Better generalization to unseen patient conditions
- Reduced dependency on manual annotation

---

## 🚨 Hybrid Alert Logic
An alert is generated if:
- A rule-based clinical threshold is violated **OR**
- The ML model detects consistent anomalies over time

This approach ensures:
- Safety through rules
- Adaptability through machine learning

---

## 📊 Performance Summary
Hybrid model evaluation achieved:

- **Precision:** ~0.93  
- **Recall:** ~0.86  
- **F1-Score:** ~0.90  

This demonstrates effective anomaly detection with reduced false alarms.

---

## 🌿 Repository Structure & Branching Strategy

### `main` branch
Contains:
- Core machine learning implementation
- Hybrid alert logic
- Evaluation scripts
- Data simulation utilities

❌ Does NOT contain:
- Flask application
- Web UI files

### `demo-ui` branch
Contains:
- Flask REST API (`app.py`)
- Web dashboard (HTML, CSS, JavaScript)
- Live charts and alert visualization
- Audio alert simulation

> This separation keeps the main branch clean and submission-ready while preserving a full deployment demo.

---

## 🖥️ Demo (Optional)
To view the interactive web demo:
1. Switch to the `demo-ui` branch
2. Install dependencies
3. Run the Flask application

```bash
python src/app.py
