"""
Problem 1: UberPOOL and Commuting versus Non-Commuting Hours

This script compares commuting hours versus non-commuting hours in the control group
(i.e., with 2-minute wait times) for Uber Express POOL data.
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Set styling for plots
sns.set(style="whitegrid")
plt.rcParams.update({'font.size': 12})

# Load data
def load_data(file_path):
    """Load the CSV data with correct delimiter and decimal point formatting."""
    df = pd.read_csv(file_path, delimiter=';')
    
    # Convert columns that might have commas instead of dots as decimal separator
    if 'total_driver_payout' in df.columns:
        df['total_driver_payout'] = df['total_driver_payout'].str.replace(',', '.').astype(float)
    
    # Convert boolean columns
    if 'treat' in df.columns:
        df['treat'] = df['treat'].astype(bool)
    if 'commute' in df.columns:
        df['commute'] = df['commute'].astype(bool)
    
    return df

# Helper function for t-test analysis
def run_ttest(group1, group2):
    """
    Run t-test between two groups and return t-statistic, p-value, and significance at 5% level.
    """
    t_stat, p_val = stats.ttest_ind(group1, group2, equal_var=False)
    significant = p_val < 0.05
    return t_stat, p_val, significant

# Main analysis function
def analyze_problem1():
    # Load data
    df = load_data('data/switchbacks.csv')
    
    # Filter for control group (2-minute wait times)
    control_df = df[df['treat'] == False].copy()
    
    # Split control group by commute/non-commute
    commute_df = control_df[control_df['commute'] == True].copy()
    non_commute_df = control_df[control_df['commute'] == False].copy()
    
    # Print sample sizes
    print(f"Sample sizes: Commuting hours: {len(commute_df)}, Non-commuting hours: {len(non_commute_df)}")
    
    # 1. Compare number of ridesharing trips (Pool + Express)
    commute_df['total_rides'] = commute_df['trips_pool'] + commute_df['trips_express']
    non_commute_df['total_rides'] = non_commute_df['trips_pool'] + non_commute_df['trips_express']
    
    # 2. Calculate the difference
    mean_rides_commute = commute_df['total_rides'].mean()
    mean_rides_non_commute = non_commute_df['total_rides'].mean() 
    ride_difference = mean_rides_commute - mean_rides_non_commute
    
    # 3. Run t-test to check if difference is statistically significant
    t_stat_rides, p_val_rides, sig_rides = run_ttest(
        commute_df['total_rides'], 
        non_commute_df['total_rides']
    )
    
    # 4-6. Compare Express trip rates
    commute_df['express_share'] = commute_df['trips_express'] / commute_df['total_rides']
    non_commute_df['express_share'] = non_commute_df['trips_express'] / non_commute_df['total_rides']
    
    mean_express_share_commute = commute_df['express_share'].mean()
    mean_express_share_non_commute = non_commute_df['express_share'].mean()
    express_share_difference = mean_express_share_commute - mean_express_share_non_commute
    
    t_stat_express, p_val_express, sig_express = run_ttest(
        commute_df['express_share'], 
        non_commute_df['express_share']
    )
    
    # 7-8. Revenue comparison (assuming $12.5 for POOL, $10 for Express)
    commute_df['revenue'] = (commute_df['trips_pool'] * 12.5) + (commute_df['trips_express'] * 10)
    non_commute_df['revenue'] = (non_commute_df['trips_pool'] * 12.5) + (non_commute_df['trips_express'] * 10)
    
    mean_revenue_commute = commute_df['revenue'].mean()
    mean_revenue_non_commute = non_commute_df['revenue'].mean()
    revenue_difference = mean_revenue_commute - mean_revenue_non_commute
    
    t_stat_revenue, p_val_revenue, sig_revenue = run_ttest(
        commute_df['revenue'], 
        non_commute_df['revenue']
    )
    
    # 9-10. Profit per trip comparison
    commute_df['profit_per_trip'] = (commute_df['revenue'] - commute_df['total_driver_payout']) / commute_df['total_rides']
    non_commute_df['profit_per_trip'] = (non_commute_df['revenue'] - non_commute_df['total_driver_payout']) / non_commute_df['total_rides']
    
    mean_profit_per_trip_commute = commute_df['profit_per_trip'].mean()
    mean_profit_per_trip_non_commute = non_commute_df['profit_per_trip'].mean()
    profit_per_trip_difference = mean_profit_per_trip_commute - mean_profit_per_trip_non_commute
    
    t_stat_profit, p_val_profit, sig_profit = run_ttest(
        commute_df['profit_per_trip'], 
        non_commute_df['profit_per_trip']
    )
    
    # Print results
    print("\n===== PROBLEM 1: Comparing Commuting vs. Non-Commuting Hours (Control Group) =====\n")
    
    print("1. Do commuting hours experience a higher number of ridesharing trips compared to non-commuting hours?")
    print(f"Answer: {'YES' if mean_rides_commute > mean_rides_non_commute else 'NO'}")
    print(f"Mean trips during commuting hours: {mean_rides_commute:.2f}")
    print(f"Mean trips during non-commuting hours: {mean_rides_non_commute:.2f}")
    
    print("\n2. What is the difference in the number of ridesharing trips between commuting and non-commuting hours?")
    print(f"Answer: {ride_difference:.2f} trips")
    
    print("\n3. Is the difference statistically significant at the 5% confidence level?")
    print(f"Answer: {'YES' if sig_rides else 'NO'} (p-value: {p_val_rides:.4f}, t-statistic: {t_stat_rides:.4f})")
    
    print("\n4. Do riders use Express at higher rates during commuting hours compared to non-commuting hours?")
    print(f"Answer: {'YES' if mean_express_share_commute > mean_express_share_non_commute else 'NO'}")
    print(f"Express share during commuting hours: {mean_express_share_commute:.4f} ({mean_express_share_commute*100:.2f}%)")
    print(f"Express share during non-commuting hours: {mean_express_share_non_commute:.4f} ({mean_express_share_non_commute*100:.2f}%)")
    
    print("\n5. What is the difference in the share of Express trips between commuting and non-commuting hours?")
    print(f"Answer: {express_share_difference:.4f} (or {express_share_difference*100:.2f}%)")
    
    print("\n6. Is the difference statistically significant at the 5% confidence level?")
    print(f"Answer: {'YES' if sig_express else 'NO'} (p-value: {p_val_express:.4f}, t-statistic: {t_stat_express:.4f})")
    
    print("\n7. Assuming riders pay $12.5 on average for a POOL ride, and $10 for an Express ride.")
    print("What is the difference in revenues between commuting and non-commuting hours?")
    print(f"Answer: ${revenue_difference:.2f}")
    print(f"Mean revenue during commuting hours: ${mean_revenue_commute:.2f}")
    print(f"Mean revenue during non-commuting hours: ${mean_revenue_non_commute:.2f}")
    
    print("\n8. Is the difference statistically significant at the 5% confidence level?")
    print(f"Answer: {'YES' if sig_revenue else 'NO'} (p-value: {p_val_revenue:.4f}, t-statistic: {t_stat_revenue:.4f})")
    
    print("\n9. What is the difference in profits per trip between commuting and non-commuting hours?")
    print(f"Answer: ${profit_per_trip_difference:.4f}")
    print(f"Mean profit per trip during commuting hours: ${mean_profit_per_trip_commute:.4f}")
    print(f"Mean profit per trip during non-commuting hours: ${mean_profit_per_trip_non_commute:.4f}")
    
    print("\n10. Is the difference statistically significant at the 5% confidence level?")
    print(f"Answer: {'YES' if sig_profit else 'NO'} (p-value: {p_val_profit:.4f}, t-statistic: {t_stat_profit:.4f})")
    
    # Create visualizations
    create_visualizations(commute_df, non_commute_df)
    
    # Create a comprehensive summary table for the report
    create_summary_table(
        mean_rides_commute, mean_rides_non_commute, ride_difference, sig_rides, p_val_rides,
        mean_express_share_commute, mean_express_share_non_commute, express_share_difference, sig_express, p_val_express,
        mean_revenue_commute, mean_revenue_non_commute, revenue_difference, sig_revenue, p_val_revenue,
        mean_profit_per_trip_commute, mean_profit_per_trip_non_commute, profit_per_trip_difference, sig_profit, p_val_profit
    )
    
    # Return results as a dictionary for potential further use
    return {
        'ride_difference': ride_difference,
        'sig_rides': sig_rides,
        'express_share_difference': express_share_difference,
        'sig_express': sig_express,
        'revenue_difference': revenue_difference,
        'sig_revenue': sig_revenue,
        'profit_per_trip_difference': profit_per_trip_difference,
        'sig_profit': sig_profit
    }

def create_visualizations(commute_df, non_commute_df):
    """Create visualizations to support the analysis"""
    # Set up the plots
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # 1. Total rides comparison
    ax = axes[0, 0]
    data = [commute_df['total_rides'], non_commute_df['total_rides']]
    labels = ['Commute', 'Non-Commute']
    ax.boxplot(data, tick_labels=labels)  # Use tick_labels instead of labels
    ax.set_title('Total Ridesharing Trips')
    ax.set_ylabel('Number of Trips')
    
    # 2. Express share comparison
    ax = axes[0, 1]
    data = [commute_df['express_share'], non_commute_df['express_share']]
    ax.boxplot(data, tick_labels=labels)  # Use tick_labels instead of labels
    ax.set_title('Share of Express Trips')
    ax.set_ylabel('Express Trips / Total Trips')
    
    # 3. Revenue comparison
    ax = axes[1, 0]
    data = [commute_df['revenue'], non_commute_df['revenue']]
    ax.boxplot(data, tick_labels=labels)  # Use tick_labels instead of labels
    ax.set_title('Revenue')
    ax.set_ylabel('Revenue ($)')
    
    # 4. Profit per trip comparison
    ax = axes[1, 1]
    data = [commute_df['profit_per_trip'], non_commute_df['profit_per_trip']]
    ax.boxplot(data, tick_labels=labels)  # Use tick_labels instead of labels
    ax.set_title('Profit per Trip')
    ax.set_ylabel('Profit per Trip ($)')
    
    plt.tight_layout()
    plt.savefig('problem1_visualizations.png')
    print("\nVisualizations saved as 'problem1_visualizations.png'")
    
def create_summary_table(
    mean_rides_commute, mean_rides_non_commute, ride_difference, sig_rides, p_val_rides,
    mean_express_share_commute, mean_express_share_non_commute, express_share_difference, sig_express, p_val_express,
    mean_revenue_commute, mean_revenue_non_commute, revenue_difference, sig_revenue, p_val_revenue,
    mean_profit_per_trip_commute, mean_profit_per_trip_non_commute, profit_per_trip_difference, sig_profit, p_val_profit
):
    """Create a summary table for the report"""
    
    # Create a summary DataFrame
    summary_data = {
        'Metric': [
            'Total Rides', 
            'Express Share (%)', 
            'Revenue ($)', 
            'Profit per Trip ($)'
        ],
        'Commuting Hours': [
            f"{mean_rides_commute:.2f}",
            f"{mean_express_share_commute*100:.2f}%",
            f"${mean_revenue_commute:.2f}",
            f"${mean_profit_per_trip_commute:.4f}"
        ],
        'Non-Commuting Hours': [
            f"{mean_rides_non_commute:.2f}",
            f"{mean_express_share_non_commute*100:.2f}%",
            f"${mean_revenue_non_commute:.2f}",
            f"${mean_profit_per_trip_non_commute:.4f}"
        ],
        'Difference': [
            f"{ride_difference:.2f}",
            f"{express_share_difference*100:.2f}%",
            f"${revenue_difference:.2f}",
            f"${profit_per_trip_difference:.4f}"
        ],
        'Significant at 5%': [
            'YES' if sig_rides else 'NO',
            'YES' if sig_express else 'NO',
            'YES' if sig_revenue else 'NO',
            'YES' if sig_profit else 'NO'
        ],
        'p-value': [
            f"{p_val_rides:.4f}",
            f"{p_val_express:.4f}",
            f"{p_val_revenue:.4f}",
            f"{p_val_profit:.4f}"
        ]
    }
    
    # Create DataFrame and save to CSV
    summary_df = pd.DataFrame(summary_data)
    summary_df.to_csv('problem1_summary.csv', index=False)
    print("Summary table saved as 'problem1_summary.csv'")
    
    # Print the table to console in a formatted way
    print("\n===== SUMMARY TABLE =====")
    print(summary_df.to_string(index=False))

if __name__ == "__main__":
    analyze_problem1() 