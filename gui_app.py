import flet as ft
import pickle
import numpy as np
import os

# Model file paths
model_paths = {
    "Logistic Regression": "models/LogisticRegression_model.pkl",
    "Random Forest": "models/RandomForest_model.pkl",
    "Support Vector Machine": "models/SVC_model.pkl",
    "K-Nearest Neighbors": "models/KNeighbors_model.pkl"
}

# Pre-recorded test accuracy
model_accuracies = {
    "Logistic Regression": 91.11,
    "Random Forest": 97.78,
    "Support Vector Machine": 97.78,
    "K-Nearest Neighbors": 95.56
}

def main(page: ft.Page):
    page.title = "Iris Classifier"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 30
    page.theme_mode = ft.ThemeMode.DARK  # Set dark mode

    # Input fields
    sl = ft.TextField(label="Sepal Length", width=250)
    sw = ft.TextField(label="Sepal Width", width=250)
    pl = ft.TextField(label="Petal Length", width=250)
    pw = ft.TextField(label="Petal Width", width=250)

    # Model selector
    model_dropdown = ft.Dropdown(
        label="Choose Model",
        options=[ft.dropdown.Option(model) for model in model_paths.keys()],
        value="Logistic Regression",
        width=250
    )

    result_text = ft.Text(size=22, weight="bold", color=ft.colors.GREEN_ACCENT)
    accuracy_text = ft.Text(size=16, italic=True, color=ft.colors.GREY_400)

    def validate_inputs():
        try:
            vals = [float(sl.value), float(sw.value), float(pl.value), float(pw.value)]
            return np.array([vals])
        except ValueError:
            return None

    def predict(e):
        features = validate_inputs()
        if features is None:
            result_text.value = "❌ Please enter valid numbers."
            accuracy_text.value = ""
            page.update()
            return

        model_name = model_dropdown.value
        model_path = model_paths[model_name]

        if not os.path.exists(model_path):
            result_text.value = f"❌ Model not found: {model_path}"
            accuracy_text.value = ""
        else:
            with open(model_path, "rb") as f:
                model = pickle.load(f)
            prediction = model.predict(features)[0]
            iris_classes = ['Setosa', 'Versicolor', 'Virginica']
            result_text.value = f"Predicted: {iris_classes[prediction]} ({model_name})"
            accuracy_text.value = f"Test Accuracy: {model_accuracies.get(model_name, '?')}%"

        page.update()

    # Layout
    page.add(
        ft.Text("🌙 Iris Flower Classifier", size=28, weight="bold", color=ft.colors.CYAN_200),
        ft.Container(
            content=ft.Column([
                ft.Text("Enter Flower Measurements", size=18, weight="w600", color=ft.colors.WHITE),
                sl, sw, pl, pw,
                model_dropdown,
                ft.ElevatedButton("Predict", on_click=predict),
            ]),
            padding=20,
            border_radius=10,
            bgcolor=ft.colors.BLACK,
        ),
        result_text,
        accuracy_text,
        ft.Divider()
    )

ft.app(target=main)
