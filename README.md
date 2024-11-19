# **Streamlit Text Classification App**

This project is a simple web application built with **Streamlit** to classify text as **Positive**, **Neutral**, or **Negative**. It uses a trained machine learning model stored in a `.pkl` file, along with a TF-IDF vectorizer for feature extraction.

---

## **Features**

1. **Interactive User Interface**:

   - Input text directly in the text box.
   - Click a button to classify the text.

2. **Text Classification**:

   - Predicts the sentiment of the entered text as Positive, Neutral, or Negative.

3. **Pre-trained Model**:
   - The app uses a pre-trained model saved in a `.pkl` file for predictions.

---

## **Technologies Used**

- **Python**: Core programming language.
- **Streamlit**: Framework for creating the web application.
- **scikit-learn**: Used for training the model and preprocessing data.
- **joblib**: For saving and loading the trained model and TF-IDF vectorizer.

---

## **Installation**

### **Prerequisites**

1. Python 3.8 or higher installed on your system.
2. Install the required Python libraries:
   ```bash
   pip install streamlit scikit-learn joblib
   ```

---

## **Setup Instructions**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ahmddbilall/sentiment-analysis-ml
   cd sentiment-analysis-ml
   ```

2. **Place the Model Files**:
   Ensure the following files are in the project directory:

   - `model.pkl` (The trained classification model)
   - `tfidf.pkl` (The TF-IDF vectorizer used during training)

3. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## **Usage**

1. Open the application in your browser (Streamlit will provide a local URL after running).
2. Enter any text you want to classify in the text box.
3. Click the **Classify** button.
4. The app will display the predicted class: **Positive**, **Neutral**, or **Negative**.

---

## **Model Training Overview**

The text classification model was trained using a supervised machine learning approach. Here's a brief overview of the steps involved:

1. **Dataset**:

   - A dataset containing labeled text data was used for training.
   - Labels: `-1` (Negative), `0` (Neutral), `1` (Positive).

2. **Text Preprocessing**:

   - Converting text to lowercase.
   - Removing special characters and stopwords.
   - Lemmatization or stemming for standardizing words.

3. **Feature Extraction**:

   - TF-IDF vectorizer was used to convert text into numerical features.

4. **Model Training**:

   - Multiple models were trained and compared, including Logistic Regression, SVM, Random Forest, Gradient Boosting, and Naive Bayes.
   - The best-performing model was selected and saved as `best_model.pkl`.

5. **Exporting Artifacts**:
   - The trained model and TF-IDF vectorizer were saved using the `joblib` library for future use.

---

## **Directory Structure**

```plaintext
streamlit-text-classification/
├── app.py                  # Streamlit app code
├── model.pkl               # Trained classification model
├── tfidf.pkl               # TF-IDF vectorizer
├── model.ipynb             # notebook
├── requirements.txt        # Python dependencies (optional)
├── .gitignore              #
└── README.md               # Project documentation
```

---

## **Future Enhancements**

- Add more models for comparison and allow dynamic model selection in the app.
- Enhance the UI with additional features like confidence scores and model explanations.
- Implement multi-language support for text classification.
- Allow users to upload a file containing multiple texts for batch classification.
