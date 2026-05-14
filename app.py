import streamlit as st
import pandas as pd

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
}

.sub-title {
    color: #9ca3af;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Kartlar */
.card {
    background: linear-gradient(145deg,#0f172a,#111827);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #1f2937;
    margin-bottom: 20px;
}

/* Kart başlığı */
.card-title {
    color: #9ca3af;
    font-size: 18px;
}

/* Kart değeri */
.card-value {
    font-size: 40px;
    font-weight: bold;
    color: white;
}

/* Grafik kutusu */
.graph-box {
    background-color: #0f172a;
    padding: 20px;
    border-radius: 20px;
    border: 1px solid #1f2937;
}

/* Alt kutular */
.footer-box {
    background-color: #0f172a;
    padding: 20px;
    border-radius: 15px;
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

# GOOGLE SHEETS LİNKİ
sheet_url = "https://docs.google.com/spreadsheets/d/1qy1Lg1u30yebc3EWIIlyVhKWhYAHzSTMGeVCS2E9yFE/export?format=csv"

# VERİYİ ÇEK
try:
    df = pd.read_csv(sheet_url)

    # BPM sütununu temizle
    df["BPM"] = pd.to_numeric(df["BPM"], errors="coerce")

    # Boş satırları sil
    df = df.dropna()

    # Eğer veri yoksa hata verme
    if df.empty:
        st.error("Google Sheets içinde veri bulunamadı.")
        st.stop()

    # SON BPM
    last_bpm = int(df["BPM"].iloc[-1])

except Exception as e:
    st.error("Veri okunurken hata oluştu.")
    st.write(e)
    st.stop()

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
        <div class="card-value">{last_bpm}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">📡 DURUM</div>
        <div class="card-value">{durum}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">📊 ÖLÇÜM SAYISI</div>
        <div class="card-value">{len(df)}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <div class="card-title">📶 BAĞLANTI</div>
        <div class="card-value">İYİ</div>
    </div>
    """, unsafe_allow_html=True)

# GRAFİK VE TABLO
left, right = st.columns([2,1])

# GRAFİK
with left:

    st.markdown("""
    <div class="graph-box">
    """, unsafe_allow_html=True)

    st.subheader("📈 Canlı BPM Grafiği")

    st.line_chart(df["BPM"])

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

# ALT KISIM
f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="footer-box">
    <h4>🛡 GÜVENLİ SİSTEM</h4>
    <p>Veriler güvenli şekilde korunmaktadır.</p>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="footer-box">
    <h4>☁ BULUT DEPOLAMA</h4>
    <p>Google Sheets üzerinde saklanıyor.</p>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="footer-box">
    <h4>⚠ NOT</h4>
    <p>Bu sistem yalnızca bilgilendirme amaçlıdır.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.caption("🔴 Sistem aktif olarak çalışıyor")
