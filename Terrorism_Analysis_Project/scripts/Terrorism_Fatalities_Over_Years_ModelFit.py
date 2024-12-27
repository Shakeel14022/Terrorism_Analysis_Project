import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dataset_loader import load_dataset
from dataset_cleaner import clean_dataset

# Load and clean the dataset
raw_data = load_dataset()
if raw_data is not None:
    data = clean_dataset(raw_data)

    # Aggregate fatalities by year
    yearly_data = data.groupby('iyear')['nkill'].sum().reset_index()

    # Extract year (X) and total fatalities (y)
    X = yearly_data['iyear'].values
    y = yearly_data['nkill'].values

    # Normalize year for numerical stability
    X_normalized = X - 1970

    # Log-transform fatalities for linear regression
    log_y = np.log(y)

    # Perform linear regression
    X_with_intercept = np.c_[np.ones(X_normalized.shape[0]), X_normalized]
    beta = np.linalg.inv(X_with_intercept.T @ X_with_intercept) @ X_with_intercept.T @ log_y

    # Extract parameters
    ln_a = beta[0]
    b = beta[1]
    a = np.exp(ln_a)

    # Generate predictions
    y_pred = a * np.exp(b * X_normalized)

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, alpha=0.7, label="Actual Fatalities", color='blue', marker='x')
    plt.plot(X, y_pred, color='orange', linewidth=2,
             label=f'Exponential Fit: y = {a:.2f} * e^({b:.4f} * (t - 1970))')
    plt.title("Exponential Model Fit: Year vs. Total Fatalities", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Total Fatalities", fontsize=12)
    plt.ylim(0, None)
    plt.legend()
    plt.grid(True)
        # Save the figure
    plt.savefig('Terrorism_Analysis_Project/figures_and_statistics/Terrorism_Fatalities_Over_Years_ModelFit.png', bbox_inches='tight')

    # Exponential model equation as a string
    model_equation = f"Exponential Model Equation: y(t) = {a:.2f} * e^({b:.4f} * (t - 1970))"

    # Print and append the model equation to the statistics file
    with open(statistics_file, 'a') as f:
        f.write("\n--- Exponential Model Equation ---\n")
        f.write(model_equation + "\n")
    

