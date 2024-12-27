import pandas as pd
import matplotlib.pyplot as plt
from dataset_loader import load_dataset
from dataset_cleaner import clean_dataset

# Load and clean the dataset
raw_data = load_dataset()
if raw_data is not None:
    data = clean_dataset(raw_data)

    # Group data by attack type and calculate stats
    relevant_data = data[['attacktype1_txt', 'success']]
    attack_stats = relevant_data.groupby('attacktype1_txt').agg(
        total_incidents=('success', 'count'),
        successful_incidents=('success', 'sum')
    ).reset_index()

    attack_stats.sort_values(by='total_incidents', ascending=False, inplace=True)

    plt.figure(figsize=(12, 8))
    bar_width = 0.4
    x = range(len(attack_stats['attacktype1_txt']))
    plt.bar(x, attack_stats['total_incidents'], width=bar_width, label='Total Incidents', color='blue')
    plt.bar([i + bar_width for i in x], attack_stats['successful_incidents'], width=bar_width, label='Successful Incidents', color='orange')
    plt.xlabel('Attack Type')
    plt.ylabel('Number of Incidents')
    plt.title('Incident Frequency and Success Rate by Attack Type')
    plt.xticks([i + bar_width / 2 for i in x], attack_stats['attacktype1_txt'], rotation=45, ha='right')
    plt.legend()
    # Save the figure
    plt.savefig('Terrorism_Analysis_Project/figures_and_statistics/Attacktype_Frequency_And_Success.png', bbox_inches='tight')
