from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def train_logreg(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    return model, X_test, y_test

