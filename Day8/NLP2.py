import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import nltk
from nltk.corpus import stopwords
import string

# Download NLTK stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load dataset
df = pd.read_csv("imdb_reviews.csv")


# Preprocessing
def clean_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


df['clean_review'] = df['review'].apply(clean_text)

# Features and labels
X = df['clean_review']
y = df['sentiment']

# Convert text to vectors
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# --- NEW: User input prediction ---
while True:
    user_input = input("\nEnter a movie review (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    # Clean and vectorize user input
    cleaned_input = clean_text(user_input)
    input_vec = vectorizer.transform([cleaned_input])

    # Predict sentiment
    prediction = model.predict(input_vec)[0]
    print(f"Predicted Sentiment: {prediction}")
