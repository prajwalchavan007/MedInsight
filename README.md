
# **Med Insight | Hospital Orchestration & Command Centre**

**Med Insight** is a data-driven hospital command centre designed to give administrators real-time control over operations, patient flow, and resource allocation.

It acts as a centralized **operating layer for healthcare systems**, combining analytics, forecasting, and live capacity tracking into a single interface.

---

## **🚀 Mission**

Hospitals frequently face **Access Block** — where patients remain in emergency care due to unavailable beds in specialized wards.

**Med Insight addresses this by enabling live network visibility and proactive decision-making.**

Instead of reacting to bottlenecks, administrators can:

* Anticipate capacity constraints
* Optimize patient movement
* Coordinate across hospital networks

---

## **🧩 Core Modules**

### **1. Med Insight (Advanced Analytics)**

**Focus:** Clinical insights and operational metrics

* Analyze **Length of Stay (LOS)** trends
* Explore **patient demographics**
* Compare **payment modes** (Government, Private, Self-pay)
* Supports multi-sheet Excel ingestion

---

### **2. MedEvac Command**

**Focus:** Inter-hospital coordination & dispatch

* Real-time **bed availability tracking across hospitals**
* Simulated **ambulance dispatch system**
* **JSON-based persistence layer** ensures data survives reloads

---

### **3. Ward Capacity & Flow**

**Focus:** Bed management and throughput

* Tracks availability across departments (ICU, Cardiology, etc.)
* Computes **Net Bed Change = Admissions – Discharges**
* Helps prevent sudden capacity overloads

---

### **4. Predictive Intelligence**

**Focus:** Demand forecasting

* Uses historical admission data
* Predicts **weekly patient inflow trends**
* Enables smarter **staff and resource planning**

---

### **5. Pharmacy & Inventory**

**Focus:** Medical supply monitoring

* Tracks stock levels in real time
* Calculates **Days to Expiry**
* Generates alerts for expiring inventory

---

## **⚙️ Technical Stack**

### **Core Engine**

* **Python 3.10+** — application logic
* **Streamlit** — interactive frontend
* **Pandas + Openpyxl** — data processing & Excel ingestion

### **Visualization**

* **Plotly Graph Objects** — interactive, responsive charts
* Dual-axis and theme-adaptive visualizations

### **UI System**

* Custom **Glassmorphism design** via CSS injection
* Centralized styling through:

  * `styles.py`
  * `components.py`

---

## **🏗️ Architecture Highlights**

* **Unified Design System**
  Consistent UI across all modules

* **State Persistence**
  JSON-based storage simulates a lightweight live database

* **Resilient Data Engine**
  Fuzzy column matching prevents crashes from inconsistent datasets

---

## **📂 Project Structure**

```
med_insight_suite/
├── app.py                # Entry point & global KPIs dashboard
├── components.py         # Shared UI components
├── styles.py             # Global styles & themes
├── data_engine.py        # Data ingestion and processing
├── data/                 # Raw datasets & JSON persistence
└── pages/                # Feature modules
```

---

## **🛠️ Installation & Setup**

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd med_insight_suite
```

### 2. Install dependencies

```bash
pip install streamlit pandas plotly openpyxl
```

### 3. Run the application

```bash
streamlit run app.py
```

---

## **🎯 Key Differentiators**

* Moves hospitals from **reactive → predictive operations**
* Combines **analytics + orchestration + simulation**
* Designed for **real-world data inconsistencies**
* Lightweight, extensible, and deployable

---

## **📌 Context**

Developed as part of the **Infosys Springboard Internship 2026**, focused on building resilient, data-first healthcare systems.

---

## **🔮 Future Scope **

* Integration with **live hospital APIs / HL7 / FHIR standards**
* Machine learning models for **patient risk scoring**
* Real-time **alerting and escalation system**
* Multi-city hospital network simulation
