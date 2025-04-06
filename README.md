# Uber Express POOL Analysis - Solutions

## Quick Links

- [Problem 1 Jupyter Notebook](Problem1_Solution.ipynb)
- [Problem 2 Jupyter Notebook](Problem2_Solution.ipynb)
- [Problem 1 Report](Problem1_Report.md)
- [Problem 2 Report](Problem2_Report.md)
- [Problem 1 Python Script](analyze_problem1.py)
- [Problem 2 Python Script](analyze_problem2.py)
- [Problem 1 Visualization](problem1_visualizations.png)
- [Problem 2 Visualization](problem2_visualizations.png)

## Problem 1: UberPOOL and Commuting versus Non-Commuting Hours

This analysis compares commuting hours versus non-commuting hours in the control group (i.e., with 2-minute wait times) from the Uber Express POOL switchback experiment.

### Answers

#### Question 1: Do commuting hours experience a higher number of ridesharing trips compared to non-commuting hours?

**Answer: YES**

- Mean trips during commuting hours: 5,046.00
- Mean trips during non-commuting hours: 3,763.40

#### Question 2: What is the difference in the number of ridesharing trips between commuting and non-commuting hours?

**Answer: 1,282.60 trips**

#### Question 3: Is the difference statistically significant at the 5% confidence level?

**Answer: YES**

- p-value: < 0.0001
- t-statistic: 7.7715

#### Question 4: Do riders use Express at higher rates during commuting hours compared to non-commuting hours?

**Answer: YES**

- Express share during commuting hours: 69.81%
- Express share during non-commuting hours: 64.80%

#### Question 5: What is the difference in the share of Express trips between commuting and non-commuting hours?

**Answer: 5.01%**

#### Question 6: Is the difference statistically significant at the 5% confidence level?

**Answer: YES**

- p-value: 0.0016
- t-statistic: 3.7599

#### Question 7: Assuming riders pay $12.5 on average for a POOL ride, and $10 for an Express ride. What is the difference in revenues between commuting and non-commuting hours?

**Answer: $13,310.97**

- Mean revenue during commuting hours: $54,256.25
- Mean revenue during non-commuting hours: $40,945.28

#### Question 8: Is the difference statistically significant at the 5% confidence level?

**Answer: YES**

- p-value: < 0.0001
- t-statistic: 7.6565

#### Question 9: What is the difference in profits per trip between commuting and non-commuting hours?

**Answer: -$0.6575** (lower during commuting hours)

- Mean profit per trip during commuting hours: $2.9421
- Mean profit per trip during non-commuting hours: $3.5996

#### Question 10: Is the difference statistically significant at the 5% confidence level?

**Answer: YES**

- p-value: 0.0003
- t-statistic: -4.4526

## Problem 2: Waiting Times and Commuting versus Non-Commuting Hours

This analysis estimates the effect of extending waiting times from 2 minutes (control group) to 5 minutes (treatment group) separately for commuting and non-commuting hours.

### Part 1: Commuting Hours Analysis

#### Question 1: What is the difference in the number of ridesharing trips between the treatment and control groups during commuting hours?

**Answer: -321.90 trips**

- Mean trips with 5-minute wait (treatment): 4,724.10
- Mean trips with 2-minute wait (control): 5,046.00

#### Question 2: Is the difference statistically significant at the 5% confidence level?

**Answer: NO**

- p-value: 0.1728
- t-statistic: -1.4197

#### Question 3: What is the difference in the number of rider cancellations between the treatment and control groups during commuting hours?

**Answer: 56.30 cancellations**

- Mean cancellations with 5-minute wait (treatment): 303.20
- Mean cancellations with 2-minute wait (control): 246.90

#### Question 4: Is the difference statistically significant at the 5% confidence level?

**Answer: YES**

- p-value: 0.0068
- t-statistic: 3.1953

#### Question 5: What is the difference in driver payout per trip between the treatment and control groups during commuting hours?

**Answer: -$0.2433**

- Mean driver payout per trip with 5-minute wait (treatment): $7.5693
- Mean driver payout per trip with 2-minute wait (control): $7.8126

#### Question 6: Is the difference statistically significant at the 5% confidence level?

**Answer: NO**

- p-value: 0.2838
- t-statistic: -1.1067

#### Question 7: What is the difference in overall match rate between the treatment and control groups during commuting hours?

**Answer: -1.47%**

- Mean match rate with 5-minute wait (treatment): 73.38%
- Mean match rate with 2-minute wait (control): 74.85%

#### Question 8: Is the difference statistically significant at the 5% confidence level?

**Answer: NO**

- p-value: 0.6417
- t-statistic: -0.4737

#### Question 9: What is the difference in double match rate between the treatment and control groups during commuting hours?

**Answer: 2.97%**

- Mean double match rate with 5-minute wait (treatment): 38.23%
- Mean double match rate with 2-minute wait (control): 35.26%

#### Question 10: Is the difference statistically significant at the 5% confidence level?

**Answer: NO**

- p-value: 0.2798
- t-statistic: 1.1159

#### Question 11: Does the analysis support extending waiting times to 5 minutes for commuting hours?

**Answer: No, the data provides clear evidence against extending waiting times.**

- Only 0 out of 5 key metrics support extending waiting times.
- The significant increase in rider cancellations is a strong negative factor.

### Part 2: Non-Commuting Hours Analysis

#### Question 12: What is the difference in the number of ridesharing trips between the treatment and control groups during non-commuting hours?

**Answer: -42.57 trips**

- Mean trips with 5-minute wait (treatment): 3,720.83
- Mean trips with 2-minute wait (control): 3,763.40

#### Question 13: Is the difference statistically significant at the 5% confidence level?

**Answer: NO**

- p-value: 0.5511
- t-statistic: -0.5981

#### Question 14: What is the difference in the number of rider cancellations between the treatment and control groups during non-commuting hours?

**Answer: 18.83 cancellations**

- Mean cancellations with 5-minute wait (treatment): 168.79
- Mean cancellations with 2-minute wait (control): 149.96

#### Question 15: Is the difference statistically significant at the 5% confidence level?

**Answer: YES**

- p-value: 0.0001
- t-statistic: 4.2183

#### Question 16: What is the difference in driver payout per trip between the treatment and control groups during non-commuting hours?

**Answer: -$0.4027**

- Mean driver payout per trip with 5-minute wait (treatment): $6.8777
- Mean driver payout per trip with 2-minute wait (control): $7.2804

#### Question 17: Is the difference statistically significant at the 5% confidence level?

**Answer: YES**

- p-value: 0.0006
- t-statistic: -3.5404

#### Question 18: What is the difference in overall match rate between the treatment and control groups during non-commuting hours?

**Answer: -3.86%**

- Mean match rate with 5-minute wait (treatment): 60.36%
- Mean match rate with 2-minute wait (control): 64.22%

#### Question 19: Is the difference statistically significant at the 5% confidence level?

**Answer: YES**

- p-value: 0.0024
- t-statistic: -3.1158

#### Question 20: What is the difference in double match rate between the treatment and control groups during non-commuting hours?

**Answer: 2.68%**

- Mean double match rate with 5-minute wait (treatment): 34.27%
- Mean double match rate with 2-minute wait (control): 31.59%

#### Question 21: Is the difference statistically significant at the 5% confidence level?

**Answer: YES**

- p-value: 0.0250
- t-statistic: 2.2744

#### Question 22: Does the analysis support extending waiting times to 5 minutes for non-commuting hours?

**Answer: No, the data provides mixed evidence for extending waiting times.**

- Only 2 out of 5 key metrics support extending waiting times.
- While the double match rate significantly improves, there are significant negative impacts on cancellations, driver payout, and overall match rate.

### Files in this Repository

- `analyze_problem1.py`: Python script that performs the analysis for Problem 1
- `analyze_problem2.py`: Python script that performs the analysis for Problem 2
- `Problem1_Report.md`: Detailed report with analysis and business implications for Problem 1
- `Problem2_Report.md`: Detailed report with analysis and business implications for Problem 2
- `Problem1_Solution.ipynb`: Jupyter notebook with the solution and visualizations for Problem 1
- `Problem2_Solution.ipynb`: Jupyter notebook with the solution and visualizations for Problem 2
- `problem1_visualizations.png`: Visualization of key metrics for Problem 1
- `problem2_visualizations.png`: Visualization of key metrics for Problem 2
- `problem1_summary.csv`: Summary table with results for Problem 1
- `problem2_commuting_summary.csv`: Summary table with results for Problem 2 (commuting hours)
- `problem2_non_commuting_summary.csv`: Summary table with results for Problem 2 (non-commuting hours)
