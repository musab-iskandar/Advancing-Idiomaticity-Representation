%%capture
!wget https://raw.githubusercontent.com/musab-iskandar/Advancing-Multimodal-Idiomaticity-Representation/refs/heads/main/Milestone%202/data/train/subtask_a_train.csv
!git clone https://github.com/musab-iskandar/Advancing-Multimodal-Idiomaticity-Representation.git

# Libraries
import numpy as np
import pandas as pd
import ast
from sklearn.metrics import classification_report
from collections import Counter

# change the values of expected_output col to be lists of numbers of images instead of its names
def convert_expected_order(df):
    # convert the string representation of list to actual list
    df['expected_order'] = df['expected_order'].apply(ast.literal_eval)

    # create a mapping dictionary for each row
    def get_image_positions(row):
        # create a dictionary mapping image names to their positions (1-5)
        image_map = {
            row[f'image{i}_name']: i for i in range(1, 6)
        }

        return [image_map[img_name] for img_name in row['expected_order']]
    df['expected_order'] = df.apply(get_image_positions, axis=1)
    return df

# implement a simple baseline (majority baseline)
def create_majority_baseline(train_df):
    # convert lists to tuples
    order_sequences = [tuple(order) for order in train_df['expected_order']]

    majority_sequence = Counter(order_sequences).most_common(1)[0][0]
    return list(majority_sequence)

def calculate_metrics(df, pred_sequence):
    # convert sequences to string format
    y_true = [str(seq) for seq in df['expected_order']]
    y_pred = [str(pred_sequence) for _ in range(len(df))]

    accuracy = sum(1 for true_seq in df['expected_order'] if list(true_seq) == pred_sequence) / len(df)
    report = classification_report(y_true, y_pred, zero_division=0)

    return accuracy, report

# Usage
data_url = 'https://raw.githubusercontent.com/musab-iskandar/Advancing-Multimodal-Idiomaticity-Representation/refs/heads/main/Milestone%202/data/train/subtask_a_train.csv'
df = pd.read_csv(data_url)
convert_expected_order(df)

majority_sequence = create_majority_baseline(df)
print(f"Most common sequence: {majority_sequence}")

accuracy, report = calculate_metrics(df, majority_sequence)
print(f"Training accuracy: {accuracy:.2%}")
print("Classification Report:")
print(report)
