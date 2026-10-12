import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import joblib

# 1. Memuat Dataset
# Pastikan nama file sesuai dengan yang ada di foldermu
df = pd.read_csv("score.csv")

# 2. Persiapan Data
X = df[['Hours']] # Variabel Independen
y = df['Scores']  # Variabel Dependen

# 3. Membagi Data (80% Latih, 20% Uji)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Pelatihan Model Regresi Linear
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Prediksi dan Evaluasi Model
predictions = model.predict(X_test)
rmse = np.sqrt(metrics.mean_squared_error(y_test, predictions))
r2 = metrics.r2_score(y_test, predictions)

print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R2): {r2:.2f}")

# 6. Menyimpan Model (Model Persistence)
joblib.dump(model, 'model_jam_belajar.pkl')
print("[SUCCESS] Model berhasil disimpan sebagai 'model_jam_belajar.pkl'")