# 🎓 Student Score Predictor | Machine Learning Web App

Aplikasi berbasis web interaktif untuk memprediksi nilai ujian siswa berdasarkan jumlah jam belajar harian. Sistem ini dibangun menggunakan algoritma **Regresi Linear Sederhana (*Simple Linear Regression*)** yang diintegrasikan ke dalam antarmuka web menggunakan *framework* Flask.

Proyek ini dikembangkan untuk memenuhi **Tugas Akhir (TA-02 / TA-03) mata kuliah Pembelajaran Mesin**.

🚀 **Live Demo:** [son0908.pythonanywhere.com](https://son0908.pythonanywhere.com)
📺 **Video Presentasi:** https://youtu.be/P2-9DU6jWW0?si=pbAaslRjqAIj3_sF 

---

## ✨ Fitur Utama
* **Prediksi Instan:** Memasukkan jumlah jam belajar dan langsung mendapatkan estimasi nilai secara *real-time*.
* **Akurasi Tinggi:** Model *Machine Learning* telah dilatih dengan dataset historis dan mencapai tingkat akurasi (R-squared) sebesar **0.97**.
* **Antarmuka Intuitif:** Desain UI/UX yang sederhana, responsif, dan mudah digunakan oleh siapa saja.
* **Cloud Deployed:** Aplikasi telah di-*deploy* ke server *cloud* (PythonAnywhere) sehingga dapat diakses kapan saja melalui internet.

---

## 🛠️ Teknologi yang Digunakan
* **Bahasa Pemrograman:** Python 3.10
* **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib
* **Web Framework:** Flask
* **Frontend:** HTML5, CSS3
* **Deployment:** PythonAnywhere, Gunicorn

---

## 📊 Dataset
Dataset yang digunakan untuk melatih model ini bersumber dari Kaggle: [Student Study Hours / Student Scores](https://www.kaggle.com/datasets/himanshunakrani/student-study-hours). Dataset ini memuat dua variabel utama:
1. `Hours`: Jumlah jam belajar (Fitur / Variabel Independen)
2. `Scores`: Nilai ujian yang didapatkan (Target / Variabel Dependen)

---

## 💻 Cara Menjalankan Aplikasi Secara Lokal (Localhost)

Jika kamu ingin menjalankan aplikasi ini di komputermu sendiri, ikuti langkah-langkah berikut:

**1. Clone repositori ini**
```bash
git clone [https://github.com/sonimochleviansyah/student-score-predictor.git](https://github.com/sonimochleviansyah/student-score-predictor.git)
cd student-score-predictor
