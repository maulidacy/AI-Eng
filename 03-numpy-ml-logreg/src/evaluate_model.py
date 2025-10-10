from sklearn.metrics import confusion_matrix, classification_report

def evaluate_model(model, X_test, y_test, labels, report_path="report.txt"):
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)