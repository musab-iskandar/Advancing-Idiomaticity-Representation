

# **Evaluation Metrics: Accuracy and F1-Score**

## **1. Definitions**

### **Accuracy**
Accuracy is a measure of how close the predicted values are to the original values.
$$ 
\text{Accuracy} = \frac{\text{Number of Correct Predictions}}{\text{Total Predictions}}
$$

- It is a simple and intuitive evaluation metric for classification tasks.
- **Higher values are better**.

### **F1-Score (Macro-Averaged)**
The **F1-Score** is the mean of precision and recall:
$$ 
\text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
$$

For multi-class classification, the **macro-average F1-Score** is used, which calculates the F1-score for each class and then averages them equally.
- **Higher values are better**.

---

### **Command-line Usage**
```bash
python score.py system_output.txt gold_standard.txt
```
- **`system_output.txt`**: File containing the predicted values.  
- **`gold_standard.txt`**: File containing the true (original) labels.

---

## **2. Example**

### Input Files
**system_output.txt**:
```
A
B
A
C
```

**gold_standard.txt**:
```
A
B
C
C
```

### Run the Script
```bash
python score.py system_output.txt gold_standard.txt
```

### Output
```
Accuracy: 0.75
F1-Score (Macro): 0.7222
```

---

## **3. Relevant Citations**
- **Accuracy**: A standard metric for classification tasks ([Wikipedia - Accuracy](https://en.wikipedia.org/wiki/Accuracy_and_precision)).  
- **F1-Score**: Widely used for imbalanced classification tasks ([Wikipedia - F1 Score](https://en.wikipedia.org/wiki/F-score)).

---

## **4. Clarification**
- **Higher scores are better** for both Accuracy and F1-Score.  
- The macro-averaged F1-Score ensures equal importance is given to each class.