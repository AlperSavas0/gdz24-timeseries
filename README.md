
# ⚡ GDZ Elektrik Arıza Tahmini Projesi

Bu proje, geçmiş verileri kullanarak bildirimsiz elektrik kesintilerini tahmin etmeyi amaçlayan bir zaman serisi analizidir. Çalışma, GDZ Elektrik Datathon 2024 kapsamında sunulan veriler üzerinde gerçekleştirilmiştir.

## Proje Yapısı

```
gdz24-timeseries/
├── data/               # Ham veri dosyaları (train.csv, test.csv, weather.csv, holidays.csv)
├── notebooks/          # Aşamalandırılmış analiz ve modelleme not defterleri
├── src/                # Yardımcı modüller (ör. model_utils.py)
├── submission/         # Üretilen tahmin çıktıları (CSV)
├── requirements.txt    # Gerekli Python paketleri
├── README.md           # Bu dosya
└── .gitignore
```

## Notebook'lar

- `01_exploratory_data_analysis.ipynb`: Veri analizi, istatistiksel özetler, mevsimsellik ve ilçelere göre kesinti dağılımları
- `02_feature_engineering.ipynb`: Özellik oluşturma (lag, rolling, takvim ve tatil bilgileri, hava durumu verisi birleştirme)
- `03_model_training.ipynb`: Cross-validation ile farklı modellerin kıyaslaması
- `04_prediction.ipynb`: Seçilen modellerle tam veriyle eğitim ve test verisi üzerinde tahmin yapılması

## Kullanılan Modeller

- Random Forest
- XGBoost
- LightGBM
- CatBoost

Tüm modeller, `src/model_utils.py` dosyasında tanımlanan `evaluate_model()` fonksiyonu kullanılarak zaman serisine uygun şekilde değerlendirilmiştir.

## Kullanım

1. Gerekli kütüphaneleri kurun:
    ```bash
    pip install -r requirements.txt
    ```

2. Not defterlerini sırasıyla çalıştırın:
    ```bash
    jupyter notebook
    ```

##  Notlar

- Notebook'lar birbirini takip edecek şekilde sıralanmıştır.
- `submission/` klasöründe her model için oluşturulan tahmin dosyaları yer alır.
- `src/` içindeki modüller, not defterlerinden doğrudan import edilerek kullanılır.
- Tahmin değerleri pozitif tam sayıya yuvarlanarak kaydedilmiştir.

---

Bu repo, veri analizi ve zaman serisi modelleme üzerine çalışmak isteyenler için örnek bir uygulama olarak yapılandırılmıştır.
