from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Memuat model yang sudah disimpan sebelumnya
model = joblib.load('model_jam_belajar.pkl')


@app.route('/')
def home():
    # Menampilkan halaman utama
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Mengambil input dari form HTML
        jam_belajar = float(request.form['jam_belajar'])

        # Melakukan prediksi (model LinearRegression dari sklearn butuh input 2D array)
        prediksi = model.predict(np.array([[jam_belajar]]))

        # Membulatkan hasil prediksi agar lebih rapi
        hasil = round(prediksi[0], 2)

        # Mengembalikan hasil ke halaman web
        return render_template('index.html', hasil_prediksi=hasil, jam_input=jam_belajar)


if __name__ == '__main__':
    app.run(debug=True)
