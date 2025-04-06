# Problem 2: Waiting Times and Commuting versus Non-Commuting Hours Analysis

## Introduction

This report analyzes the effect of extending waiting times from 2 minutes (control group) to 5 minutes (treatment group) in Uber's Express POOL service. We examine these effects separately for commuting and non-commuting hours to determine if the impact of longer wait times differs based on the time of day.

## Dataset Overview

The dataset contains data from a switchback experiment run in Boston between February 19, 2018, and March 5, 2018. Each day was divided into 9 time periods of 160 minutes each. During the experiment, the Express POOL matching algorithm alternated between letting riders wait up to 2 minutes (control) and up to 5 minutes (treatment) before being matched to a driver.

**Sample sizes:**

- **Commuting hours:**
  - Treatment group (5-min wait): 10 observation periods
  - Control group (2-min wait): 10 observation periods
- **Non-commuting hours:**
  - Treatment group (5-min wait): 53 observation periods
  - Control group (2-min wait): 53 observation periods

## Part 1: Effect of Waiting Times During Commuting Hours

### 1-2. Impact on Total Rides

**Question 1-2:** What is the difference in the number of ridesharing trips between the treatment and control groups during commuting hours?

- Mean trips with 5-minute wait (treatment): 4,724.10
- Mean trips with 2-minute wait (control): 5,046.00
- **Difference: -321.90 trips**
- This difference is **not statistically significant** (p-value: 0.1728)

During commuting hours, extending wait times appears to reduce the number of total rides, though this reduction is not statistically significant. This suggests that longer wait times may slightly discourage ridership during peak hours, but the evidence is not strong enough to draw definitive conclusions.

### 3-4. Impact on Rider Cancellations

**Question 3-4:** What is the difference in the number of rider cancellations between the treatment and control groups during commuting hours?

- Mean cancellations with 5-minute wait (treatment): 303.20
- Mean cancellations with 2-minute wait (control): 246.90
- **Difference: 56.30 cancellations**
- This difference is **statistically significant** (p-value: 0.0068)

Longer wait times during commuting hours lead to a statistically significant increase in rider cancellations. This indicates that riders are less willing to tolerate longer wait times during rush hours, possibly due to tighter schedules and time constraints.

### 5-6. Impact on Driver Payout per Trip

**Question 5-6:** What is the difference in driver payout per trip between the treatment and control groups during commuting hours?

- Mean driver payout per trip with 5-minute wait (treatment): $7.5693
- Mean driver payout per trip with 2-minute wait (control): $7.8126
- **Difference: -$0.2433**
- This difference is **not statistically significant** (p-value: 0.2838)

Driver payout per trip appears slightly lower with longer wait times, but this difference is not statistically significant during commuting hours. This suggests that extending wait times may not substantially impact driver earnings per trip during peak hours.

### 7-8. Impact on Match Rate

**Question 7-8:** What is the difference in overall match rate between the treatment and control groups during commuting hours?

- Mean match rate with 5-minute wait (treatment): 73.38%
- Mean match rate with 2-minute wait (control): 74.85%
- **Difference: -1.47%**
- This difference is **not statistically significant** (p-value: 0.6417)

The match rate (percentage of trips matched with at least one other rider) is slightly lower with longer wait times during commuting hours, but this difference is not statistically significant. This suggests that extending wait times does not substantially improve the ability to match riders during peak hours.

### 9-10. Impact on Double Match Rate

**Question 9-10:** What is the difference in double match rate between the treatment and control groups during commuting hours?

- Mean double match rate with 5-minute wait (treatment): 38.23%
- Mean double match rate with 2-minute wait (control): 35.26%
- **Difference: 2.97%**
- This difference is **not statistically significant** (p-value: 0.2798)

The double match rate (percentage of trips matched with at least two other riders) is slightly higher with longer wait times, but this difference is not statistically significant during commuting hours. This suggests that extending wait times might marginally improve the ability to create triple matches, but the evidence is not strong enough.

### 11. Overall Assessment for Commuting Hours

**Question 11:** Does the analysis support extending waiting times to 5 minutes for commuting hours?

**Answer: No, the data provides clear evidence against extending waiting times.**

Of the five key metrics analyzed:

- Total rides: Negative impact (not significant)
- Rider cancellations: Negative impact (significant)
- Driver payout per trip: Negative impact (not significant)
- Match rate: Negative impact (not significant)
- Double match rate: Positive impact (not significant)

Only the double match rate shows a positive impact from longer wait times, and this impact is not statistically significant. Meanwhile, rider cancellations significantly increase with longer wait times. The data suggests that extending wait times during commuting hours would likely have negative consequences without sufficient offsetting benefits.

## Part 2: Effect of Waiting Times During Non-Commuting Hours

### 12-13. Impact on Total Rides

**Question 12-13:** What is the difference in the number of ridesharing trips between the treatment and control groups during non-commuting hours?

- Mean trips with 5-minute wait (treatment): 3,720.83
- Mean trips with 2-minute wait (control): 3,763.40
- **Difference: -42.57 trips**
- This difference is **not statistically significant** (p-value: 0.5511)

During non-commuting hours, extending wait times has a minimal effect on the total number of rides, and this effect is not statistically significant. This suggests that during off-peak hours, riders may be more tolerant of longer wait times, resulting in less impact on ridership.

### 14-15. Impact on Rider Cancellations

**Question 14-15:** What is the difference in the number of rider cancellations between the treatment and control groups during non-commuting hours?

- Mean cancellations with 5-minute wait (treatment): 168.79
- Mean cancellations with 2-minute wait (control): 149.96
- **Difference: 18.83 cancellations**
- This difference is **statistically significant** (p-value: 0.0001)

Similar to commuting hours, longer wait times during non-commuting hours also lead to a statistically significant increase in rider cancellations. However, the absolute increase is smaller than during commuting hours (18.83 vs. 56.30), suggesting that riders are somewhat more tolerant of longer wait times during off-peak hours.

### 16-17. Impact on Driver Payout per Trip

**Question 16-17:** What is the difference in driver payout per trip between the treatment and control groups during non-commuting hours?

- Mean driver payout per trip with 5-minute wait (treatment): $6.8777
- Mean driver payout per trip with 2-minute wait (control): $7.2804
- **Difference: -$0.4027**
- This difference is **statistically significant** (p-value: 0.0006)

During non-commuting hours, extending wait times leads to a statistically significant reduction in driver payout per trip. This could be due to shorter trip distances or other changes in trip characteristics resulting from the longer matching window.

### 18-19. Impact on Match Rate

**Question 18-19:** What is the difference in overall match rate between the treatment and control groups during non-commuting hours?

- Mean match rate with 5-minute wait (treatment): 60.36%
- Mean match rate with 2-minute wait (control): 64.22%
- **Difference: -3.86%**
- This difference is **statistically significant** (p-value: 0.0024)

Surprisingly, the match rate is significantly lower with longer wait times during non-commuting hours. This counterintuitive result suggests that extending the matching window does not achieve its primary purpose of increasing rider matching during off-peak hours, and may actually reduce it.

### 20-21. Impact on Double Match Rate

**Question 20-21:** What is the difference in double match rate between the treatment and control groups during non-commuting hours?

- Mean double match rate with 5-minute wait (treatment): 34.27%
- Mean double match rate with 2-minute wait (control): 31.59%
- **Difference: 2.68%**
- This difference is **statistically significant** (p-value: 0.0250)

The double match rate is significantly higher with longer wait times during non-commuting hours. This is one positive outcome of extending wait times, indicating that the longer matching window does enable more triple matches outside of peak hours.

### 22. Overall Assessment for Non-Commuting Hours

**Question 22:** Does the analysis support extending waiting times to 5 minutes for non-commuting hours?

**Answer: No, the data provides mixed evidence for extending waiting times.**

Of the five key metrics analyzed:

- Total rides: Negative impact (not significant)
- Rider cancellations: Negative impact (significant)
- Driver payout per trip: Negative impact (significant)
- Match rate: Negative impact (significant)
- Double match rate: Positive impact (significant)

While the increase in double match rate is significant during non-commuting hours, it comes with significant negative impacts on rider cancellations, driver payout, and overall match rate. The mixed results do not provide clear support for extending wait times during non-commuting hours.

## Comparative Analysis and Business Implications

Comparing the effects of longer wait times across commuting and non-commuting hours reveals several key insights:

1. **Rider Sensitivity to Wait Times**: Riders are sensitive to wait times both during commuting and non-commuting hours, as evidenced by increased cancellations in both periods. However, the sensitivity is greater during commuting hours (56.30 additional cancellations vs. 18.83 during non-commuting hours).

2. **Efficiency Trade-offs**: While extending wait times might theoretically improve matching efficiency, the data shows minimal to negative impacts on match rates. Only the double match rate shows improvement with longer wait times, and this is only statistically significant during non-commuting hours.

3. **Driver Economics**: Longer wait times appear to negatively impact driver payouts, with a larger and statistically significant reduction during non-commuting hours. This could affect driver satisfaction and retention.

4. **Stronger Statistical Evidence During Non-Commuting Hours**: More metrics show statistically significant differences during non-commuting hours, likely due to the larger sample size (53 observations vs. 10 for commuting hours).

## Recommendations

Based on the analysis, we recommend:

1. **Maintain 2-Minute Wait Times During Commuting Hours**: The data shows clear evidence against extending wait times during peak hours, with significant increases in cancellations and no statistically significant benefits.

2. **Consider Alternative Approaches for Non-Commuting Hours**: While extending wait times during non-commuting hours has mixed results, the negative impacts (increased cancellations, lower match rates, lower driver payouts) likely outweigh the benefit of increased double matches. We recommend exploring alternative approaches to improve matching efficiency.

3. **Segment-Specific Strategies**: Consider developing different strategies for different times of day rather than a one-size-fits-all approach to wait times.

4. **Further Research**: Conduct additional experiments with intermediate wait times (e.g., 3 or 4 minutes) or with more sophisticated, dynamic wait time algorithms that adjust based on real-time demand and supply conditions.

## Methodology

The analysis was conducted using Python with pandas for data manipulation, scipy for statistical testing, and matplotlib/seaborn for visualization. Two-sample t-tests assuming unequal variances were used to assess the statistical significance of differences between metrics for the treatment (5-minute wait) and control (2-minute wait) groups, with a significance level of 5%.

The complete code and detailed analysis is available in the `analyze_problem2.py` script.
