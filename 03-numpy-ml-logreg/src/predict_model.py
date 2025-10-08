from sklearn.matrics import accuracy_score

def predict_and_evaluate(model, X_test, y_test):
    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)
    return acc