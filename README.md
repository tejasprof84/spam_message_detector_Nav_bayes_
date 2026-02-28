# 📩 Spam Message Detector (Naive Bayes + TF-IDF)

A Machine Learning web application that detects whether a message is **Spam** or **Not Spam** using:

* TF-IDF text vectorization
* Naive Bayes classification
* Streamlit web interface

---

## 🌐 Live App

👉 **Try the live project here:**
https://spammessagedetectornavbayesgit-obpzjxmk35xeca4n8cveim.streamlit.app/

---

## 📌 Features

✔ Text preprocessing and cleaning
✔ TF-IDF vectorization
✔ Naive Bayes spam classification
✔ Real-time prediction via web UI
✔ Trained model saved using pickle
✔ Deployed on Streamlit Cloud

---

## 🧠 Machine Learning Workflow

1. Load dataset (spam messages)
2. Clean and preprocess text
3. Convert text → numeric features using TF-IDF
4. Train Naive Bayes classifier
5. Save model and vectorizer (pickle)
6. Predict spam from new user input
7. Deploy using Streamlit

---

## 📂 Project Structure

```
spam_message_detector/
│
├── app.py
├── spam_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
└── notebooks (optional)
```

---

## 💻 How to Run Locally

### Step 1 — Clone repository

```
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

---

### Step 2 — Create virtual environment

Windows:

```
python -m venv myenv
.\myenv\Scripts\activate
```

Mac/Linux:

```
python3 -m venv myenv
source myenv/bin/activate
```

---

### Step 3 — Install dependencies

```
pip install -r requirements.txt
```

---

### Step 4 — Run Streamlit app

```
streamlit run app.py
```

OR (if command not recognized):

```
python -m streamlit run app.py
```

---

### Step 5 — Open browser

```
http://localhost:8501
```

---

## 📦 Requirements

* Python 3.8+
* Streamlit
* scikit-learn
* pandas
* numpy

Install all with:

```
pip install -r requirements.txt
```

---

## 🔮 Example Usage

Enter a message like:

```
Congratulations! You won a free prize. Click here now!
```

Prediction:

```
Spam
```

---

## 🚀 Deployment

This app is deployed using **Streamlit Cloud** connected to GitHub.

Deployment steps:

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Select `app.py`
4. Deploy

---

## 📊 Model Information

* Vectorizer: TF-IDF
* Algorithm: Naive Bayes (Bernoulli / Multinomial)
* Task: Binary classification (Spam / Ham)

---

## 📜 License

This project is for educational and portfolio purposes.

---

## 👨‍💻 Author

Machine Learning project demonstrating text classification and model deployment.
