import streamlit as st
import pandas as pd
import time

# SAYFA AYARI
st.set_page_config(
    page_title="Akıllı EKG Sistemi",
    layout="wide"
)

# TEMA
st.markdown("""
<style>

body {
    background-color: #0b1220;
}

.main {
    background-color: #0b1220;
    color: white;
}

h1, h2, h3 {
    color: white;
}

.stMetric {
    background-color: #111827;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #1f2937;
}

</style>
""", unsafe_allow_html=True)

# BAŞLIK
st.title("❤️ Akıllı EKG İzleme Sistemi")

st.markdown("### Gerçek Zamanlı Hasta Takip Paneli")

# GOOGLE SHEETS CSV LİNKİ
sheet_url = "https://docs.google.com/spreadsheets/d/1qy1Lg1u30yebc3EWIIlyVhKWhYAHzSTMGeVCS2E9yFE/export?format=csv"

# VERİYİ ÇEK
df = pd.read_csv(sheet_url)

# BPM sütununu temizle
df["BPM"] = pd.to_numeric(df["BPM"], errors="coerce")

# Boş verileri kaldır
df = df.dropna()

# Son BPM değeri
last_bpm = int(df["BPM"].iloc[-1])

# DURUM HESABI
if last_bpm < 60:
    durum = "Düşük"
elif last_bpm > 120:
    durum = "Yüksek"
else:
    durum = "Normal"

# ÜST KARTLAR
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="❤️ BPM",
        value=f"{last_bpm}"
    )

with col2:
    st.metric(
        label="📡 Durum",
        value=durum
    )

with col3:
    st.metric(
        label="🕒 Son Güncelleme",
        value=time.strftime("%H:%M:%S")
    )

# ÇİZGİ
st.markdown("---")

# GRAFİK
st.subheader("📈 Canlı BPM Grafiği")

st.line_chart(df["BPM"])

# TABLO
st.markdown("---")

st.subheader("📋 Son Ölçümler")

st.dataframe(df.tail(10))

# OTOMATİK YENİLEME
time.sleep(2)

st.rerun()
