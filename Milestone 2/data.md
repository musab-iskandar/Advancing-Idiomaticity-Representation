# SemEval-2025 Task 1: AdMIRe Dataset

## Overview
The AdMIRe (Advancing Multimodal Idiomaticity Representation) dataset is designed for evaluating systems' ability to understand idioms and their visual representations. The dataset consists of two subtasks with annotated examples of expressions used both literally and idiomatically.

## Data Format

### Subtask A Format (`subtask_a_train.tsv`)
Tab-separated file containing:
- `compound`: Expression being analyzed 
- `subset`: Train/Sample designation
- `sentence_type`: "literal" or "idiomatic"
- `sentence`: Example usage
- `expected_order`: List of image filenames in preferred order
- `image[1-5]_name`: Filenames for associated images
- `image[1-5]_caption`: Detailed descriptions of each image

## Key Features
- Each entry has 5 associated images with detailed captions
- Expressions can be used literally or idiomatically
- Images provide visual context for understanding expressions
- Dataset split into training and sample subsets
- Focus on multimodal understanding of idiomaticity

## Purpose
Evaluate systems' ability to:
- Distinguish literal vs idiomatic usage
- Connect linguistic expressions to visual representations
- Order images by relevance to expression usage
- Process multimodal information effectively
