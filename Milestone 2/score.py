
import sys
from sklearn.metrics import accuracy_score, f1_score

def load_labels(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def evaluate(predicted_values, original_values):
    predictions = load_labels(predicted_values)
    ground_truth = load_labels(original_values)
    accuracy = accuracy_score(ground_truth, predictions)
    f1 = f1_score(ground_truth, predictions, average='macro')
    print(f"Accuracy: {accuracy:.4f}")
    print(f"F1-Score (Macro): {f1:.4f}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python score.py <system_output.txt> <gold_standard.txt>")
        sys.exit(1)
    evaluate(sys.argv[1], sys.argv[2])
