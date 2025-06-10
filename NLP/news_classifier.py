import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import nltk
from nltk.corpus import stopwords
import string

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load dataset
df = pd.read_csv("ag_news.csv")

# Clean text
def clean_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

df['clean_title'] = df['title'].apply(clean_text)

# Features and labels
X = df['clean_title']
y = df['category']

# Vectorize text
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# User input prediction
while True:
    user_input = input("\nEnter a news headline (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    cleaned_input = clean_text(user_input)
    input_vec = vectorizer.transform([cleaned_input])
    prediction = model.predict(input_vec)[0]
    print(f"Predicted Category: {prediction}")
