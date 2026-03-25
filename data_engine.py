import pandas as pd
import streamlit as st
import os

# ═══════════════════════════════════════════════════════════════
# 1. LEGACY ENGINE (Powers app.py and older modules)
# ═══════════════════════════════════════════════════════════════
@st.cache_data(ttl=600)
def get_system_data():
    """Loads and caches the primary system KPIs and demand data."""
    try:
        kpi = pd.read_csv('data/pulseops_healthcare_kpi_data.csv')
        demand = pd.read_csv('data/demand_data.csv')
        
        # Engineering New Metrics
        if 'bed_occupancy_pct' in kpi.columns and 'avg_doctor_utilization' in kpi.columns:
            kpi['wait_time_index'] = (kpi['bed_occupancy_pct'] * kpi['avg_doctor_utilization']) / 100
            
        # Compute a risk score for the overview page
        if 'risk_score' not in kpi.columns and 'bed_occupancy_pct' in kpi.columns and 'daily_admissions' in kpi.columns:
            kpi['risk_score'] = (kpi['bed_occupancy_pct'] * 0.6) + (kpi['daily_admissions'] * 0.4)
            
        return kpi, demand
    except FileNotFoundError as e:
        # Silently fail if old data is missing so app doesn't crash
        return pd.DataFrame(), pd.DataFrame()

def get_live_metrics():
    """Extracts the most recent day's metrics vs yesterday."""
    kpi, _ = get_system_data()
    if not kpi.empty:
        live = kpi.iloc[-1].copy()
        yesterday = kpi.iloc[-2].copy() if len(kpi) > 1 else live
        if hasattr(live['date'], 'strftime'):
            live['date'] = live['date'].strftime('%Y-%m-%d')
        return live, yesterday
    return {}, {}

@st.cache_data(ttl=600)
def get_utilization_data():
    try:
        return pd.read_csv('data/utilization_data.csv')
    except FileNotFoundError:
        return pd.DataFrame()

@st.cache_data(ttl=600)
def get_inventory_data():
    try:
        df = pd.read_csv('data/medical_inventory.csv')
        df["expiry_date"] = pd.to_datetime(df["expiry_date"], dayfirst=True, errors="coerce")
        df["days_to_expiry"] = (df["expiry_date"] - pd.Timestamp.now()).dt.days.astype("Int64")
        return df
    except FileNotFoundError:
        return pd.DataFrame()
        
@st.cache_data(ttl=600)
def get_patient_data():
    try:
        return pd.read_csv('data/patient_data.csv')
    except FileNotFoundError:
        return pd.DataFrame()


# ═══════════════════════════════════════════════════════════════
# 2. NEW COMPREHENSIVE ENGINE (Powers the New Dashboards)
# ═══════════════════════════════════════════════════════════════
@st.cache_data
def load_comprehensive_data():
    """
    Loads all Nexus datasets directly from the single Excel file, 
    cleans column names, and caches them.
    """
    excel_path = "data/final_healthcare_dataset.xlsx"
    
    # Map our internal keys to the exact Sheet Names in your Excel file
    sheet_map = {
        "patients": "Patients Data",
        "admissions": "Admissions Data",
        "satisfaction": "Satisfaction Data",
        "financial": "Financial Data",
        "bed_occupancy": "Bed Occupancy",
        "utilization": "Utilization Data",
        "safety": "Safety and Compliance",
        "staff": "Staff Data",
        "readmissions": "Readmission Data"
    }

    data_dict = {}
    
    if os.path.exists(excel_path):
        # Load the whole excel file into memory once (faster)
        try:
            xls = pd.ExcelFile(excel_path)
            
            for key, sheet_name in sheet_map.items():
                if sheet_name in xls.sheet_names:
                    df = pd.read_excel(xls, sheet_name=sheet_name)
                    # Standardize all columns: lowercase, strip spaces, replace spaces with underscores
                    df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')
                    data_dict[key] = df
                else:
                    st.warning(f"Sheet '{sheet_name}' not found in Excel file.")
                    data_dict[key] = pd.DataFrame()
        except Exception as e:
            st.error(f"Error reading Excel file: {e}")
    else:
        st.error(f"Excel file not found at {excel_path}. Please ensure it is inside the 'data/' folder.")
        # Fill with empty dataframes so the app doesn't hard crash
        for key in sheet_map.keys():
            data_dict[key] = pd.DataFrame()
            
    return data_dict

def get_safe_col(df, possible_names):
    """Helper function to find a column name even if it varies slightly."""
    if df is None or df.empty: return None
    for col in df.columns:
        for name in possible_names:
            if name in col:
                return col
    return None