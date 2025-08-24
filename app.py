import streamlit as st
import pandas as pd

# Öneriler sözlüğü
oneriler = {
    "dil_gelisimi": "📚 Daha çok kitap okuma, konuşma etkinlikleri, sunumlar",
    "motor_beceri": "🥁 Hareket, müzik, ritm ve ince motor etkinlikleri",
    "sosyal_duygusal": "🎭 Drama, duyguları tanıma, sosyal beceri oyunları",
    "bilissel": "🧩 Yapboz, eşleştirme, resim bulma oyunları"
}

# Session state kullanarak öğrencileri kaydedelim
if "ogrenciler" not in st.session_state:
    st.session_state.ogrenciler = []

st.title("👩‍🏫 Öğrenci Gelişim Değerlendirme")

# Öğrenci bilgisi
ad_soyad = st.text_input("Öğrenci Ad Soyad:")

# Gelişim alanları için 1–5 arası seçim
dil = st.radio("Dil Gelişimi", [1,2,3,4,5], horizontal=True)
motor = st.radio("Motor Beceri", [1,2,3,4,5], horizontal=True)
sosyal = st.radio("Sosyal-Duygusal", [1,2,3,4,5], horizontal=True)
bilissel = st.radio("Bilişsel", [1,2,3,4,5], horizontal=True)

# Öğrenci ekleme
if st.button("Sonraki Öğrenci"):
    st.session_state.ogrenciler.append({
        "ad_soyad": ad_soyad,
        "dil_gelisimi": dil,
        "motor_beceri": motor,
        "sosyal_duygusal": sosyal,
        "bilissel": bilissel
    })
    st.experimental_rerun()

# Değerlendirmeyi bitirme
if st.button("Bitir"):
    df = pd.DataFrame(st.session_state.ogrenciler)

    st.subheader("📊 Öğrenci Gelişim Önerileri")
    for i, row in df.iterrows():
        st.markdown(f"### 👧 {row['ad_soyad']} için öneriler:")
        for alan in ["dil_gelisimi", "motor_beceri", "sosyal_duygusal", "bilissel"]:
            if row[alan] <= 3:  # düşük puanlı alanlar
                st.markdown(f"- **{alan.replace('_',' ').title()}**: {oneriler[alan]}")