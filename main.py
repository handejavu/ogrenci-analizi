import pandas as pd

# Örnek veri
data = {
    "ogrenci": ["Elif", "Deniz", "Mert", "Asya"],
    "dil_gelisimi": [4, 2, 3, 5],
    "motor_beceri": [3, 4, 2, 5],
    "sosyal_duygusal": [5, 3, 2, 4],
    "bilissel": [4, 2, 3, 5]
}

df = pd.DataFrame(data)

# Öneri sözlüğü
oneriler = {
    "dil_gelisimi": "📚 Daha çok kitap okuma, konuşma etkinlikleri, sunumlar",
    "motor_beceri": "🥁 Hareket, müzik, ritm ve ince motor etkinlikleri",
    "sosyal_duygusal": "🎭 Drama, duyguları tanıma, sosyal beceri oyunları",
    "bilissel": "🧩 Yapboz, eşleştirme, resim bulma oyunları"
}

# Öğrencilere göre öneriler
for i, row in df.iterrows():
    print(f"\n👧 {row['ogrenci']} için öneriler:")
    for alan in ["dil_gelisimi", "motor_beceri", "sosyal_duygusal", "bilissel"]:
        if row[alan] <= 3:  # düşük puanlı alanlar
            print(f"- {alan.replace('_', ' ').title()}: {oneriler[alan]}")
