import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
ps = PorterStemmer()
lemma = WordNetLemmatizer()
def transform_text(message):
     # Chuyển về chữ thường và tách từ
    message = message.lower()
    message = word_tokenize(message)
    
    # Lọc các từ: loại bỏ stopwords, dấu câu và chỉ giữ lại từ alphanumeric
    stop_words = set(stopwords.words('english'))
    filtered_message = [ps.stem(word) for word in message if word.isalnum() and word not in stop_words and word not in string.punctuation]
    
    # Trả về kết quả dưới dạng chuỗi
    return " ".join(filtered_message)
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
st.title("Email/SMS Spam Classifier")
input_sms = st.text_area("Enter the message")
if st.button('Predict'):
    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")