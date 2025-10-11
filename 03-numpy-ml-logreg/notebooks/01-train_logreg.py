from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# load dataset
iris = load_iris()
X, y = iris.data, iris.target # X = fitur, y = label

print("Fitur: ", iris.feature_names)
print("Kelas: ", iris.target_names)
print("Ukuran dataset: ", X.shape)

# Split data (Training dan Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inisiasi model (buat model)
model = LogisticRegression(max_iter=200)

# LATIH MODEL (fit) menggunakan data training
model.fit(X_train, y_train)

# PREDIKSI (predict) menggunakan model yang sudah dilatih
y_pred = model.predict(X_test) # minta jawaban dari otak
# evaluasi model
acc = accuracy_score(y_test, y_pred)
print("Akurasi:", acc)
