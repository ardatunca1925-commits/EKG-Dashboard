import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# SAYFA AYARI
st.set_page_config(
    page_title="Akıllı EKG Sistemi",
    layout="wide"
)

# CSS TASARIM
st.markdown("""
<style>

.stApp {
    background-color: #050816;
    color: white;
}

/* Başlık */
.main-title {
    font-size: 42px;
    font-weight: bold;
    color: white;
    margin-bottom: 0px;
}

.sub-title {
    color: #9ca3af;
    font-size: 20px;
    margin-top: -10px;
}

/* Kartlar */
.card {
    background: linear-gradient(145deg,#0f172a,#111827);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #1f2937;
    box-shadow: 0 0 20px rgba(0,0,0,0.5);
}

/* Kart Başlığı */
.card-title {
    color: #9ca3af;
    font-size: 18px;
}

/* Büyük Değer */
.card-value {
    font-size: 45px;
    font-weight: bold;
    color: white;
}

/* Renkler */
.red {
    color: #ff4b4b;
}

.green {
    color: #00ff88;
}

.blue {
    color: #3b82f6;
}

.purple {
    color: #a855f7;
}

/* Alt kutular */
.footer-box {
    background-color: #0f172a;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #1f2937;
}

/* Grafik kutusu */
.graph-box {
    background-color: #0f172a;
    padding: 20px;
    border-radius: 20px;
    border: 1px solid #1f2937;
}

</style>
""", unsafe_allow_html=True)

# BAŞLIK
st.markdown("""
<div class="main-title">
❤️ AKILLI EKG İZLEME SİSTEMİ
</div>

<div class="sub-title">
Gerçek Zamanlı Hasta Takip Paneli
</div>
""", unsafe_allow_html=True)

st.write("")

# GOOGLE SHEETS CSV LİNKİ
sheet_url = "https://docs.google.com/spreadsheets/d/1qy1Lg1u30yebc3EWIIlyVhKWhYAHzSTMGeVCS2E9yFE/export?format=csv"

# VERİYİ ÇEK
df = pd.read_csv(sheet_url)

# BPM TEMİZLE
df["BPM"] = pd.to_numeric(df["BPM"], errors="coerce")

# BOŞ VERİLERİ SİL
df = df.dropna()

# SON BPM
last_bpm = int(df["BPM"].iloc[-1])

# DURUM
if last_bpm < 60:
    durum = "Düşük"
elif last_bpm > 120:
    durum = "Yüksek"
else:
    durum = "Normal"

# ÜST KARTLAR
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">❤️ BPM</div>
        <div class="card-value red">{last_bpm}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">📡 DURUM</div>
        <div class="card-value green">{durum}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">📊 ÖLÇÜM SAYISI</div>
        <div class="card-value blue">{len(df)}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">📶 BAĞLANTI</div>
        <div class="card-value purple">İYİ</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ALT KISIM
left, right = st.columns([2,1])

# GRAFİK
with left:

    st.markdown("""
    <div class="graph-box">
    """, unsafe_allow_html=True)

    st.subheader("📈 Canlı BPM Grafiği")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        y=df["BPM"],
        mode='lines+markers',
        line=dict(color='#ff4b4b', width=3),
        name="BPM"
    ))

    fig.update_layout(
        paper_bgcolor='#0f172a',
        plot_bgcolor='#0f172a',
        font_color='white',
        xaxis_title="Zaman",
        yaxis_title="BPM",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# TABLO
with right:

    st.markdown("""
    <div class="graph-box">
    """, unsafe_allow_html=True)

    st.subheader("📋 Son Ölçümler")

    st.dataframe(df.tail(10), use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# ALT BİLGİLER
f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="footer-box">
    <h4 style='color:#ff4b4b;'>🛡 GÜVENLİ SİSTEM</h4>
    <p>Veriler güvenli şekilde korunmaktadır.</p>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="footer-box">
    <h4 style='color:#3b82f6;'>☁ BULUT DEPOLAMA</h4>
    <p>Google Sheets üzerinde saklanıyor.</p>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="footer-box">
    <h4 style='color:#facc15;'>⚠ NOT</h4>
    <p>Bu sistem yalnızca bilgilendirme amaçlıdır.</p>
    </div>
    """, unsafe_allow_html=True)

# ALT DURUM
st.write("")
st.caption("🔴 Sistem canlı olarak çalışıyor")
