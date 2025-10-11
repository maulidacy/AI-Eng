from sklearn.metrics import confusion_matrix, classification_report

def evaluate_model(model, X_test, y_test, labels, report_path="report.txt"):
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred) # matrix konfusi (y_true, y_pred)
    report = classification_report(y_test, y_pred, target_names=labels)

    with open(report_path, "w") as f:
        f.write(report)

    return cm, report