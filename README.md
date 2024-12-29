# Advancing Multimodal Idiomaticity Representation
## The Problem Definition
Idioms are a class of multi-word expressions (MWE), which pose a challenge for current state-of-the-art models because their meanings are often different from the individual words that compose them. 
For instance, "piece of cake." doesn't typically refer to an actual slice of cake; instead, it refers to something that is easy to do. These expressions may also generate confusion between the literal, surface meaning arising from their component words and the idiomatic meaning. These, among other characteristics, make them a valuable testing ground for examining how NLP models capture meaning.
### We present two subtasks:
-	Subtask A - Static Image: The model will be presented with a set of 5 images and a context sentence in which a particular potentially idiomatic nominal compound (NC) appears. The goal is to rank the images according to how well they represent the sense in which the NC is used in the given context sentence. 
   <img width="614" alt="image" src="https://github.com/user-attachments/assets/c04c425b-2d31-4246-9354-92983c83bcb4" />

-	Subtask B - Image Sequences (or Next Image Prediction): The model will be given a target expression and an image sequence from which the last of 3 images has been removed, and the objective will be to select the best fill from a set of candidate images. The NC sense being depicted (idiomatic or literal) will not be given, and this label should also be output.
  <img width="650" alt="image" src="https://github.com/user-attachments/assets/d337569d-4c1e-402c-bcbe-f0316aab0241" />

To see the full description in SemEval: https://semeval2025-task1.github.io/

## Evaluation metrics
-	Accuracy
-	F1 Score

## Students
- Musab Iskandar - 444003841
- Ahmad Arif - 444002984
- Yousef Koshak  - 444000774
