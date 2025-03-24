import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from dataset import questions_data

# Prepare dataset from dataset.py
questions = []
followups = []

# Convert question data into a format suitable for ML
for category_questions in questions_data.values():
    for i in range(len(category_questions) - 1):
        questions.append(category_questions[i]["question"])
        followups.append(category_questions[i + 1]["question"])

# Convert text into numerical data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)
y = followups

# Train Logistic Regression Model
model = LogisticRegression()
model.fit(X, y)

# Save the trained model & vectorizer
joblib.dump(model, "followup_model.pkl")
joblib.dump(vectorizer, "followup_vectorizer.pkl")

print("✅ Model training completed! Files saved as 'followup_model.pkl' and 'followup_vectorizer.pkl'")
