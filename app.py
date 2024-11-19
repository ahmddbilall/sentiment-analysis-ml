import streamlit as st
import joblib
import pickle
import os

# model = joblib.load("model.pkl")
tfidf = joblib.load("tfidf.pkl")  
chunks = sorted(
        [os.path.join('model_chunks', f) for f in os.listdir('model_chunks') if f.startswith('chunk_')],
        key=lambda x: int(x.split('_')[-1].split('.')[0])
)

data = b''
for chunk in chunks:
    with open(chunk, 'rb') as chunk_file:
        data += chunk_file.read()

model = pickle.loads(data)

st.title("Text Classification App")

input_text = st.text_area("Enter the text to classify", "")

if st.button("Classify"):
    if input_text.strip():
        input_features = tfidf.transform([input_text])

        predicted_class = model.predict(input_features)[0]

        class_map = {-1: "Negative", 0: "Neutral", 1: "Positive"}
        st.write(f"The predicted class is: **{class_map.get(predicted_class, 'Unknown')}**")
    else:
        st.write("Please enter some text for classification.")
