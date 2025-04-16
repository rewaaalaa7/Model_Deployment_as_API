# Iris Classifier API

## Overview

This project demonstrates a complete machine learning pipeline for classifying iris flower species using a trained model exposed via a Flask API. The system is containerized with Docker for portability and includes a user-friendly graphical interface built using Flet for real-time predictions.

The application receives iris flower features (sepal length, sepal width, petal length, and petal width) and returns the predicted class (Setosa, Versicolor, or Virginica). This project is designed for those interested in deploying ML models as scalable web APIs and integrating them with lightweight desktop/web GUIs.

## Approaches Used

- **Model Training:** A scikit-learn-based model was trained on the Iris dataset and serialized using `joblib`.
- **Flask REST API:** The trained model is deployed through a RESTful API using Flask, which listens for incoming prediction requests.
- **Dockerization:** A Dockerfile is provided to build and run the entire application in a consistent environment, ensuring platform independence.
- **Flet GUI Interface:** A Flet-based GUI is included to interact with the API, allowing users to enter input values and view predictions in real time.

## GUI Preview

Below is a screenshot of the GUI used to test the model:

![Flet GUI Preview](assets/gui_screenshot.png)
