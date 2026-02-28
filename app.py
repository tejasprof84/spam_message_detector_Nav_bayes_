import streamlit as st
import pickle

# load model
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("Spam Message Detector")

msg = st.text_input("Enter message")

if st.button("Predict"):
    data = vectorizer.transform([msg])
    result = model.predict(data)

    if result[0] == "spam":
        st.error("Spam message")
    else:
        st.success("Not spam")