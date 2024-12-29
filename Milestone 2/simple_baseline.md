# Majority Baseline Implementation Documentation

## Overview
This implementation presents a simple majority baseline for a sequence prediction task. The baseline predicts the most frequently occurring sequence in the training data for all test instances. This serves as a basic performance benchmark against which more sophisticated models can be compared.

## Implementation Details
### Data Preprocessing
The implementation includes important  preprocessing step: The `convert_expected_order` function transforms the data format, converts string representations of lists to actual Python lists, maps image names to their numerical positions (1-5), and creates a consistent numerical representation of sequences

### Majority Baseline Model
The majority baseline is implemented through two main functions:
1. `create_majority_baseline(train_df)`
   - Converts sequence lists to tuples for hashability
   - Uses Counter to find the most common sequence
   - Returns the majority sequence as a list
   - This sequence will be used as the prediction for all test instances
2. `calculate_metrics(df, pred_sequence)`
   - Evaluates the performance of the majority baseline
   - Calculates accuracy by comparing predictions with true sequences
   - Generates a classification report using sklearn's classification_report
   - Handles zero division cases in metric calculations

## Sample output 
Most common sequence: [2, 5, 3, 1, 4]

Training accuracy: 4.29%

Classification Report:
|                 | precision | recall | f1-score | support |
|-----------------|-----------|---------|-----------|----------|
| [2, 4, 3, 5, 1] | 0.00      | 0.00    | 0.00      | 1        |
| [2, 4, 5, 1, 3] | 0.00      | 0.00    | 0.00      | 1        |
| [2, 5, 1, 3, 4] | 0.00      | 0.00    | 0.00      | 2        |
| [2, 5, 3, 1, 4] | 0.04      | 1.00    | 0.08      | 3        |

|                 | precision | recall | f1-score | support |
|-----------------|-----------|---------|-----------|----------|
| accuracy        |           |         | 0.04      | 70       |
| macro avg       | 0.00      | 0.02    | 0.00      | 70       |
| weighted avg    | 0.00      | 0.04    | 0.00      | 70       |
