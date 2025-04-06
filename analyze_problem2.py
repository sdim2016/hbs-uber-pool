"""
Problem 2: Waiting Times and Commuting versus Non-Commuting Hours

This script estimates the effect of extending waiting times from 2 minutes (control group) 
to 5 minutes (treatment group) separately for commuting and non-commuting hours.
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Set styling for plots
sns.set(style="whitegrid")
plt.rcParams.update({'font.size': 12})

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

def run_ttest(group1, group2):
    """
    Run t-test between two groups and return t-statistic, p-value, and significance at 5% level.
    """
    t_stat, p_val = stats.ttest_ind(group1, group2, equal_var=False)
    significant = p_val < 0.05
    return t_stat, p_val, significant

def calculate_match_rate(df):
    """Calculate the overall match rate for each observation."""
    return df['total_matches'] / (df['trips_pool'] + df['trips_express'])

def calculate_double_match_rate(df):
    """Calculate the double match rate for each observation."""
    return df['total_double_matches'] / (df['trips_pool'] + df['trips_express'])

def calculate_driver_payout_per_trip(df):
    """Calculate driver payout per trip for each observation."""
    return df['total_driver_payout'] / (df['trips_pool'] + df['trips_express'])

def analyze_waiting_times(commute_value=True):
    """
    Analyze the effect of extending waiting times for either commuting or non-commuting hours.
    
    Args:
        commute_value (bool): Whether to analyze commuting hours (True) or non-commuting hours (False)
    
    Returns:
        dict: Dictionary with analysis results
    """
    # Load data
    df = load_data('data/switchbacks.csv')
    
    # Filter data for selected commute hours
    filtered_df = df[df['commute'] == commute_value].copy()
    
    # Split into treatment and control groups
    treatment_df = filtered_df[filtered_df['treat'] == True].copy()  # 5-minute wait times
    control_df = filtered_df[filtered_df['treat'] == False].copy()   # 2-minute wait times
    
    # Print sample sizes
    print(f"Sample sizes: Treatment group: {len(treatment_df)}, Control group: {len(control_df)}")
    
    # Calculate metrics
    for df in [treatment_df, control_df]:
        df['total_rides'] = df['trips_pool'] + df['trips_express'] 
        df['match_rate'] = calculate_match_rate(df)
        df['double_match_rate'] = calculate_double_match_rate(df)
        df['driver_payout_per_trip'] = calculate_driver_payout_per_trip(df)
    
    # Store results
    results = {}
    
    # 1-2. Effect on total rides
    mean_rides_treatment = treatment_df['total_rides'].mean()
    mean_rides_control = control_df['total_rides'].mean()
    ride_difference = mean_rides_treatment - mean_rides_control
    
    t_stat_rides, p_val_rides, sig_rides = run_ttest(
        treatment_df['total_rides'], 
        control_df['total_rides']
    )
    
    results['ride_difference'] = ride_difference
    results['sig_rides'] = sig_rides
    results['p_val_rides'] = p_val_rides
    results['t_stat_rides'] = t_stat_rides
    
    # 3-4. Effect on rider cancellations
    mean_cancellations_treatment = treatment_df['rider_cancellations'].mean()
    mean_cancellations_control = control_df['rider_cancellations'].mean()
    cancellation_difference = mean_cancellations_treatment - mean_cancellations_control
    
    t_stat_cancellations, p_val_cancellations, sig_cancellations = run_ttest(
        treatment_df['rider_cancellations'], 
        control_df['rider_cancellations']
    )
    
    results['cancellation_difference'] = cancellation_difference
    results['sig_cancellations'] = sig_cancellations
    results['p_val_cancellations'] = p_val_cancellations
    results['t_stat_cancellations'] = t_stat_cancellations
    
    # 5-6. Effect on driver payout per trip
    mean_payout_treatment = treatment_df['driver_payout_per_trip'].mean()
    mean_payout_control = control_df['driver_payout_per_trip'].mean()
    payout_difference = mean_payout_treatment - mean_payout_control
    
    t_stat_payout, p_val_payout, sig_payout = run_ttest(
        treatment_df['driver_payout_per_trip'], 
        control_df['driver_payout_per_trip']
    )
    
    results['payout_difference'] = payout_difference
    results['sig_payout'] = sig_payout
    results['p_val_payout'] = p_val_payout
    results['t_stat_payout'] = t_stat_payout
    
    # 7-8. Effect on match rate
    mean_match_rate_treatment = treatment_df['match_rate'].mean()
    mean_match_rate_control = control_df['match_rate'].mean()
    match_rate_difference = mean_match_rate_treatment - mean_match_rate_control
    
    t_stat_match_rate, p_val_match_rate, sig_match_rate = run_ttest(
        treatment_df['match_rate'], 
        control_df['match_rate']
    )
    
    results['match_rate_difference'] = match_rate_difference
    results['sig_match_rate'] = sig_match_rate
    results['p_val_match_rate'] = p_val_match_rate
    results['t_stat_match_rate'] = t_stat_match_rate
    
    # 9-10. Effect on double match rate
    mean_double_match_rate_treatment = treatment_df['double_match_rate'].mean()
    mean_double_match_rate_control = control_df['double_match_rate'].mean()
    double_match_rate_difference = mean_double_match_rate_treatment - mean_double_match_rate_control
    
    t_stat_double_match_rate, p_val_double_match_rate, sig_double_match_rate = run_ttest(
        treatment_df['double_match_rate'], 
        control_df['double_match_rate']
    )
    
    results['double_match_rate_difference'] = double_match_rate_difference
    results['sig_double_match_rate'] = sig_double_match_rate
    results['p_val_double_match_rate'] = p_val_double_match_rate
    results['t_stat_double_match_rate'] = t_stat_double_match_rate
    
    # Store means for reporting
    results['mean_rides_treatment'] = mean_rides_treatment
    results['mean_rides_control'] = mean_rides_control
    results['mean_cancellations_treatment'] = mean_cancellations_treatment
    results['mean_cancellations_control'] = mean_cancellations_control
    results['mean_payout_treatment'] = mean_payout_treatment
    results['mean_payout_control'] = mean_payout_control
    results['mean_match_rate_treatment'] = mean_match_rate_treatment
    results['mean_match_rate_control'] = mean_match_rate_control
    results['mean_double_match_rate_treatment'] = mean_double_match_rate_treatment
    results['mean_double_match_rate_control'] = mean_double_match_rate_control
    
    return results

def print_commuting_results(results):
    """Print results for the commuting hours analysis."""
    print("\n===== PROBLEM 2: Part 1-11 - Effect of Waiting Times during Commuting Hours =====\n")
    
    print("1. What is the difference in the number of ridesharing trips between the treatment and control groups during commuting hours?")
    print(f"Answer: {results['ride_difference']:.2f} trips")
    print(f"Mean trips with 5-minute wait (treatment): {results['mean_rides_treatment']:.2f}")
    print(f"Mean trips with 2-minute wait (control): {results['mean_rides_control']:.2f}")
    
    print("\n2. Is the difference statistically significant at the 5% confidence level?")
    print(f"Answer: {'YES' if results['sig_rides'] else 'NO'} (p-value: {results['p_val_rides']:.4f}, t-statistic: {results['t_stat_rides']:.4f})")
    
    print("\n3. What is the difference in the number of rider cancellations between the treatment and control groups during commuting hours?")
    print(f"Answer: {results['cancellation_difference']:.2f} cancellations")
    print(f"Mean cancellations with 5-minute wait (treatment): {results['mean_cancellations_treatment']:.2f}")
    print(f"Mean cancellations with 2-minute wait (control): {results['mean_cancellations_control']:.2f}")
    
    print("\n4. Is the difference statistically significant at the 5% confidence level?")
    print(f"Answer: {'YES' if results['sig_cancellations'] else 'NO'} (p-value: {results['p_val_cancellations']:.4f}, t-statistic: {results['t_stat_cancellations']:.4f})")
    
    print("\n5. What is the difference in driver payout per trip between the treatment and control groups during commuting hours?")
    print(f"Answer: ${results['payout_difference']:.4f}")
    print(f"Mean driver payout per trip with 5-minute wait (treatment): ${results['mean_payout_treatment']:.4f}")
    print(f"Mean driver payout per trip with 2-minute wait (control): ${results['mean_payout_control']:.4f}")
    
    print("\n6. Is the difference statistically significant at the 5% confidence level?")
    print(f"Answer: {'YES' if results['sig_payout'] else 'NO'} (p-value: {results['p_val_payout']:.4f}, t-statistic: {results['t_stat_payout']:.4f})")
    
    print("\n7. What is the difference in overall match rate between the treatment and control groups during commuting hours?")
    print(f"Answer: {results['match_rate_difference']:.4f} (or {results['match_rate_difference']*100:.2f}%)")
    print(f"Mean match rate with 5-minute wait (treatment): {results['mean_match_rate_treatment']:.4f} ({results['mean_match_rate_treatment']*100:.2f}%)")
    print(f"Mean match rate with 2-minute wait (control): {results['mean_match_rate_control']:.4f} ({results['mean_match_rate_control']*100:.2f}%)")
    
    print("\n8. Is the difference statistically significant at the 5% confidence level?")
    print(f"Answer: {'YES' if results['sig_match_rate'] else 'NO'} (p-value: {results['p_val_match_rate']:.4f}, t-statistic: {results['t_stat_match_rate']:.4f})")
    
    print("\n9. What is the difference in double match rate between the treatment and control groups during commuting hours?")
    print(f"Answer: {results['double_match_rate_difference']:.4f} (or {results['double_match_rate_difference']*100:.2f}%)")
    print(f"Mean double match rate with 5-minute wait (treatment): {results['mean_double_match_rate_treatment']:.4f} ({results['mean_double_match_rate_treatment']*100:.2f}%)")
    print(f"Mean double match rate with 2-minute wait (control): {results['mean_double_match_rate_control']:.4f} ({results['mean_double_match_rate_control']*100:.2f}%)")
    
    print("\n10. Is the difference statistically significant at the 5% confidence level?")
    print(f"Answer: {'YES' if results['sig_double_match_rate'] else 'NO'} (p-value: {results['p_val_double_match_rate']:.4f}, t-statistic: {results['t_stat_double_match_rate']:.4f})")
    
    # Evaluate question 11
    positive_metrics = 0
    if results['ride_difference'] > 0 and results['sig_rides']:
        positive_metrics += 1
    if results['cancellation_difference'] < 0 and results['sig_cancellations']:
        positive_metrics += 1
    if results['payout_difference'] < 0 and results['sig_payout']:
        positive_metrics += 1
    if results['match_rate_difference'] > 0 and results['sig_match_rate']:
        positive_metrics += 1
    if results['double_match_rate_difference'] > 0 and results['sig_double_match_rate']:
        positive_metrics += 1
    
    # Determine recommendation for question 11
    recommendation = ""
    if positive_metrics >= 4:
        recommendation = "Yes, the data provides clear support for extending waiting times."
    elif positive_metrics >= 2:
        recommendation = "No, the data provides mixed evidence for extending waiting times."
    else:
        recommendation = "No, the data provides clear evidence against extending waiting times."
    
    print("\n11. Does the analysis support extending waiting times to 5 minutes for commuting hours?")
    print(f"Answer: {recommendation}")
    print(f"Explanation: {positive_metrics} out of 5 key metrics support extending waiting times.")

def print_non_commuting_results(results):
    """Print results for the non-commuting hours analysis."""
    print("\n===== PROBLEM 2: Part 12-22 - Effect of Waiting Times during Non-Commuting Hours =====\n")
    
    print("12. What is the difference in the number of ridesharing trips between the treatment and control groups during non-commuting hours?")
    print(f"Answer: {results['ride_difference']:.2f} trips")
    print(f"Mean trips with 5-minute wait (treatment): {results['mean_rides_treatment']:.2f}")
    print(f"Mean trips with 2-minute wait (control): {results['mean_rides_control']:.2f}")
    
    print("\n13. Is the difference statistically significant at the 5% confidence level?")
    print(f"Answer: {'YES' if results['sig_rides'] else 'NO'} (p-value: {results['p_val_rides']:.4f}, t-statistic: {results['t_stat_rides']:.4f})")
    
    print("\n14. What is the difference in the number of rider cancellations between the treatment and control groups during non-commuting hours?")
    print(f"Answer: {results['cancellation_difference']:.2f} cancellations")
    print(f"Mean cancellations with 5-minute wait (treatment): {results['mean_cancellations_treatment']:.2f}")
    print(f"Mean cancellations with 2-minute wait (control): {results['mean_cancellations_control']:.2f}")
    
    print("\n15. Is the difference statistically significant at the 5% confidence level?")
    print(f"Answer: {'YES' if results['sig_cancellations'] else 'NO'} (p-value: {results['p_val_cancellations']:.4f}, t-statistic: {results['t_stat_cancellations']:.4f})")
    
    print("\n16. What is the difference in driver payout per trip between the treatment and control groups during non-commuting hours?")
    print(f"Answer: ${results['payout_difference']:.4f}")
    print(f"Mean driver payout per trip with 5-minute wait (treatment): ${results['mean_payout_treatment']:.4f}")
    print(f"Mean driver payout per trip with 2-minute wait (control): ${results['mean_payout_control']:.4f}")
    
    print("\n17. Is the difference statistically significant at the 5% confidence level?")
    print(f"Answer: {'YES' if results['sig_payout'] else 'NO'} (p-value: {results['p_val_payout']:.4f}, t-statistic: {results['t_stat_payout']:.4f})")
    
    print("\n18. What is the difference in overall match rate between the treatment and control groups during non-commuting hours?")
    print(f"Answer: {results['match_rate_difference']:.4f} (or {results['match_rate_difference']*100:.2f}%)")
    print(f"Mean match rate with 5-minute wait (treatment): {results['mean_match_rate_treatment']:.4f} ({results['mean_match_rate_treatment']*100:.2f}%)")
    print(f"Mean match rate with 2-minute wait (control): {results['mean_match_rate_control']:.4f} ({results['mean_match_rate_control']*100:.2f}%)")
    
    print("\n19. Is the difference statistically significant at the 5% confidence level?")
    print(f"Answer: {'YES' if results['sig_match_rate'] else 'NO'} (p-value: {results['p_val_match_rate']:.4f}, t-statistic: {results['t_stat_match_rate']:.4f})")
    
    print("\n20. What is the difference in double match rate between the treatment and control groups during non-commuting hours?")
    print(f"Answer: {results['double_match_rate_difference']:.4f} (or {results['double_match_rate_difference']*100:.2f}%)")
    print(f"Mean double match rate with 5-minute wait (treatment): {results['mean_double_match_rate_treatment']:.4f} ({results['mean_double_match_rate_treatment']*100:.2f}%)")
    print(f"Mean double match rate with 2-minute wait (control): {results['mean_double_match_rate_control']:.4f} ({results['mean_double_match_rate_control']*100:.2f}%)")
    
    print("\n21. Is the difference statistically significant at the 5% confidence level?")
    print(f"Answer: {'YES' if results['sig_double_match_rate'] else 'NO'} (p-value: {results['p_val_double_match_rate']:.4f}, t-statistic: {results['t_stat_double_match_rate']:.4f})")
    
    # Evaluate question 22
    positive_metrics = 0
    if results['ride_difference'] > 0 and results['sig_rides']:
        positive_metrics += 1
    if results['cancellation_difference'] < 0 and results['sig_cancellations']:
        positive_metrics += 1
    if results['payout_difference'] < 0 and results['sig_payout']:
        positive_metrics += 1
    if results['match_rate_difference'] > 0 and results['sig_match_rate']:
        positive_metrics += 1
    if results['double_match_rate_difference'] > 0 and results['sig_double_match_rate']:
        positive_metrics += 1
    
    # Determine recommendation for question 22
    recommendation = ""
    if positive_metrics >= 4:
        recommendation = "Yes, the data provides clear support for extending waiting times."
    elif positive_metrics >= 2:
        recommendation = "No, the data provides mixed evidence for extending waiting times."
    else:
        recommendation = "No, the data provides clear evidence against extending waiting times."
    
    print("\n22. Does the analysis support extending waiting times to 5 minutes for non-commuting hours?")
    print(f"Answer: {recommendation}")
    print(f"Explanation: {positive_metrics} out of 5 key metrics support extending waiting times.")

def create_summary_tables(commuting_results, non_commuting_results):
    """Create and save summary tables for both analyses."""
    # Create summary for commuting hours
    commuting_summary = pd.DataFrame({
        'Metric': [
            'Total Rides', 
            'Rider Cancellations',
            'Driver Payout per Trip ($)',
            'Match Rate (%)',
            'Double Match Rate (%)'
        ],
        '5-min Wait (Treatment)': [
            f"{commuting_results['mean_rides_treatment']:.2f}",
            f"{commuting_results['mean_cancellations_treatment']:.2f}",
            f"${commuting_results['mean_payout_treatment']:.4f}",
            f"{commuting_results['mean_match_rate_treatment']*100:.2f}%",
            f"{commuting_results['mean_double_match_rate_treatment']*100:.2f}%"
        ],
        '2-min Wait (Control)': [
            f"{commuting_results['mean_rides_control']:.2f}",
            f"{commuting_results['mean_cancellations_control']:.2f}",
            f"${commuting_results['mean_payout_control']:.4f}",
            f"{commuting_results['mean_match_rate_control']*100:.2f}%",
            f"{commuting_results['mean_double_match_rate_control']*100:.2f}%"
        ],
        'Difference': [
            f"{commuting_results['ride_difference']:.2f}",
            f"{commuting_results['cancellation_difference']:.2f}",
            f"${commuting_results['payout_difference']:.4f}",
            f"{commuting_results['match_rate_difference']*100:.2f}%",
            f"{commuting_results['double_match_rate_difference']*100:.2f}%"
        ],
        'Significant at 5%': [
            'YES' if commuting_results['sig_rides'] else 'NO',
            'YES' if commuting_results['sig_cancellations'] else 'NO',
            'YES' if commuting_results['sig_payout'] else 'NO',
            'YES' if commuting_results['sig_match_rate'] else 'NO',
            'YES' if commuting_results['sig_double_match_rate'] else 'NO'
        ],
        'p-value': [
            f"{commuting_results['p_val_rides']:.4f}",
            f"{commuting_results['p_val_cancellations']:.4f}",
            f"{commuting_results['p_val_payout']:.4f}",
            f"{commuting_results['p_val_match_rate']:.4f}",
            f"{commuting_results['p_val_double_match_rate']:.4f}"
        ]
    })
    
    # Create summary for non-commuting hours
    non_commuting_summary = pd.DataFrame({
        'Metric': [
            'Total Rides', 
            'Rider Cancellations',
            'Driver Payout per Trip ($)',
            'Match Rate (%)',
            'Double Match Rate (%)'
        ],
        '5-min Wait (Treatment)': [
            f"{non_commuting_results['mean_rides_treatment']:.2f}",
            f"{non_commuting_results['mean_cancellations_treatment']:.2f}",
            f"${non_commuting_results['mean_payout_treatment']:.4f}",
            f"{non_commuting_results['mean_match_rate_treatment']*100:.2f}%",
            f"{non_commuting_results['mean_double_match_rate_treatment']*100:.2f}%"
        ],
        '2-min Wait (Control)': [
            f"{non_commuting_results['mean_rides_control']:.2f}",
            f"{non_commuting_results['mean_cancellations_control']:.2f}",
            f"${non_commuting_results['mean_payout_control']:.4f}",
            f"{non_commuting_results['mean_match_rate_control']*100:.2f}%",
            f"{non_commuting_results['mean_double_match_rate_control']*100:.2f}%"
        ],
        'Difference': [
            f"{non_commuting_results['ride_difference']:.2f}",
            f"{non_commuting_results['cancellation_difference']:.2f}",
            f"${non_commuting_results['payout_difference']:.4f}",
            f"{non_commuting_results['match_rate_difference']*100:.2f}%",
            f"{non_commuting_results['double_match_rate_difference']*100:.2f}%"
        ],
        'Significant at 5%': [
            'YES' if non_commuting_results['sig_rides'] else 'NO',
            'YES' if non_commuting_results['sig_cancellations'] else 'NO',
            'YES' if non_commuting_results['sig_payout'] else 'NO',
            'YES' if non_commuting_results['sig_match_rate'] else 'NO',
            'YES' if non_commuting_results['sig_double_match_rate'] else 'NO'
        ],
        'p-value': [
            f"{non_commuting_results['p_val_rides']:.4f}",
            f"{non_commuting_results['p_val_cancellations']:.4f}",
            f"{non_commuting_results['p_val_payout']:.4f}",
            f"{non_commuting_results['p_val_match_rate']:.4f}",
            f"{non_commuting_results['p_val_double_match_rate']:.4f}"
        ]
    })
    
    # Save to CSV
    commuting_summary.to_csv('problem2_commuting_summary.csv', index=False)
    non_commuting_summary.to_csv('problem2_non_commuting_summary.csv', index=False)
    
    # Print to console
    print("\n===== COMMUTING HOURS SUMMARY =====")
    print(commuting_summary.to_string(index=False))
    
    print("\n===== NON-COMMUTING HOURS SUMMARY =====")
    print(non_commuting_summary.to_string(index=False))
    
    print("\nSummary tables saved as 'problem2_commuting_summary.csv' and 'problem2_non_commuting_summary.csv'")

def create_visualizations(commuting_results, non_commuting_results):
    """Create visualizations comparing the treatment and control groups."""
    # Setup
    fig, axes = plt.subplots(5, 2, figsize=(18, 24))
    
    # Variables to visualize
    variables = [
        ('Total Rides', 'mean_rides_treatment', 'mean_rides_control'),
        ('Rider Cancellations', 'mean_cancellations_treatment', 'mean_cancellations_control'),
        ('Driver Payout per Trip ($)', 'mean_payout_treatment', 'mean_payout_control'),
        ('Match Rate (%)', 'mean_match_rate_treatment', 'mean_match_rate_control'),
        ('Double Match Rate (%)', 'mean_double_match_rate_treatment', 'mean_double_match_rate_control')
    ]
    
    # Create bar charts for each metric
    for i, (title, treat_key, control_key) in enumerate(variables):
        # Commuting hours
        ax = axes[i, 0]
        data = [commuting_results[treat_key], commuting_results[control_key]]
        bars = ax.bar(['5-min Wait', '2-min Wait'], data, color=['skyblue', 'lightgreen'])
        ax.set_title(f'{title} - Commuting Hours')
        ax.grid(True, alpha=0.3)
        
        # Add labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                  f'{height:.2f}', ha='center', va='bottom', fontweight='bold')
        
        # Non-commuting hours
        ax = axes[i, 1]
        data = [non_commuting_results[treat_key], non_commuting_results[control_key]]
        bars = ax.bar(['5-min Wait', '2-min Wait'], data, color=['skyblue', 'lightgreen'])
        ax.set_title(f'{title} - Non-Commuting Hours')
        ax.grid(True, alpha=0.3)
        
        # Add labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                  f'{height:.2f}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('problem2_visualizations.png')
    print("\nVisualizations saved as 'problem2_visualizations.png'")

def main():
    # Analyze for commuting hours
    print("Analyzing commuting hours...")
    commuting_results = analyze_waiting_times(commute_value=True)
    print_commuting_results(commuting_results)
    
    # Analyze for non-commuting hours
    print("\nAnalyzing non-commuting hours...")
    non_commuting_results = analyze_waiting_times(commute_value=False)
    print_non_commuting_results(non_commuting_results)
    
    # Create summary tables
    create_summary_tables(commuting_results, non_commuting_results)
    
    # Create visualizations
    create_visualizations(commuting_results, non_commuting_results)

if __name__ == "__main__":
    main() 