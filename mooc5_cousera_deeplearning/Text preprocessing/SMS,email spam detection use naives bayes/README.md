Đoạn mã bạn đưa ra là một ứng dụng web sử dụng **Streamlit** để phân loại tin nhắn (SMS hoặc Email) là **Spam** hay **Not Spam** (Không phải Spam). Mục tiêu của ứng dụng này là giúp người dùng xác định xem tin nhắn họ nhập vào có phải là spam hay không. Cụ thể, mã này thực hiện các bước sau:

### Các phần chính của ứng dụng:

1. **Import thư viện**:
   - **streamlit (st)**: Dùng để tạo giao diện người dùng đơn giản cho ứng dụng web.
   - **pickle**: Được sử dụng để tải mô hình và vectorizer đã được huấn luyện và lưu trữ trước đó.
   - **nltk (Natural Language Toolkit)**: Dùng để xử lý văn bản, bao gồm tokenization, loại bỏ stopwords, và stemming.
   - **string**: Dùng để làm việc với các ký tự đặc biệt và dấu câu.
   
2. **`transform_text()`**:
   - Hàm này dùng để xử lý văn bản nhập vào. Cụ thể, nó thực hiện các bước:
     - Chuyển tất cả các ký tự trong văn bản thành chữ thường (lowercase).
     - Tách văn bản thành các từ (tokens) bằng cách sử dụng `nltk.word_tokenize`.
     - Loại bỏ các ký tự không phải chữ hoặc số (sử dụng `isalnum()`).
     - Loại bỏ các từ dừng (stopwords) và dấu câu.
     - Áp dụng **stemming** (chuyển các từ về dạng gốc) bằng cách sử dụng `PorterStemmer` trong NLTK.
   
3. **`tfidf = pickle.load(open('vectorizer.pkl','rb'))`**:
   - Mã này tải **TF-IDF Vectorizer** đã được huấn luyện trước đó từ tệp `vectorizer.pkl` bằng `pickle`. TF-IDF vectorizer sẽ chuyển đổi văn bản đầu vào thành các vector số để mô hình có thể hiểu và xử lý.

4. **`model = pickle.load(open('model.pkl','rb'))`**:
   - Tải mô hình đã được huấn luyện (model.pkl) từ tệp. Mô hình này là mô hình phân loại (có thể là Naive Bayes, SVM, hoặc một mô hình khác) mà bạn đã huấn luyện từ trước.

5. **Streamlit giao diện người dùng**:
   - `st.title("Email/SMS Spam Classifier")`: Hiển thị tiêu đề của ứng dụng.
   - `input_sms = st.text_area("Enter the message")`: Tạo một ô nhập liệu để người dùng có thể nhập tin nhắn muốn phân loại.
   - `if st.button('Predict')`: Nếu người dùng nhấn nút "Predict", ứng dụng sẽ thực hiện các bước xử lý và phân loại tin nhắn.
     - **Bước 1: Tiền xử lý văn bản**: Dùng hàm `transform_text()` để xử lý văn bản tin nhắn nhập vào.
     - **Bước 2: Vector hóa văn bản**: Sử dụng **TF-IDF Vectorizer** để chuyển văn bản đã xử lý thành vector số.
     - **Bước 3: Dự đoán**: Dự đoán bằng mô hình đã được tải trước đó (`model.predict(vector_input)`).
     - **Bước 4: Hiển thị kết quả**: Nếu dự đoán là 1, hiển thị "Spam". Nếu dự đoán là 0, hiển thị "Not Spam".
   
6. **Kết quả**:
   - Nếu tin nhắn là **Spam**, ứng dụng sẽ hiển thị "Spam".
   - Nếu tin nhắn là **Not Spam**, ứng dụng sẽ hiển thị "Not Spam".

### Tóm tắt các bước xử lý:
1. Nhập tin nhắn.
2. Tiền xử lý văn bản (chuyển thành chữ thường, loại bỏ stopwords, token hóa, stemming).
3. Chuyển văn bản đã xử lý thành vector số bằng TF-IDF.
4. Dự đoán tin nhắn là Spam hay không bằng mô hình đã huấn luyện.
5. Hiển thị kết quả phân loại.

### Cách sử dụng
1. Mở ngay terminal trên file app.py
2. chạy streamlit run app.py

Ứng dụng này sẽ giúp người dùng nhanh chóng kiểm tra xem một tin nhắn có phải là spam hay không, rất hữu ích trong việc lọc tin nhắn rác.
