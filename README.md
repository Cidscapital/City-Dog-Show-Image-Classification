# City-Dog-Show-Image-Classification
 
## Project Overview

This project focuses on using Python skills to enhance an image classifier for a citywide dog show. Participants submit images of their dogs along with biographical information, and our goal is to validate if the submissions are actual dogs. The provided Python classifier utilizes convolutional neural networks (CNNs) with different architectures (AlexNet, VGG, and ResNet) trained on ImageNet.

## Project Tasks

### 1. Identify the Best Classification Algorithm

Determine the most effective image classification algorithm for distinguishing between "dogs" and "not dogs."

### 2. Evaluate Breed Identification

Assess the chosen algorithm's performance in correctly identifying dog breeds based on submitted images.

### 3. Measure Algorithm Runtimes

Time the execution of each algorithm, considering the trade-off between accuracy and computational resources.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/city-dog-show-classification.git
   cd city-dog-show-classification
   ```

2. Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

3. Run the  program:

  ```bash
  python test_classifier.py
  ```
## Important Notes
- The project emphasizes Python programming skills, and actual classifiers are provided.
- CNNs are used for image classification, and the classifier function is available in `classifier.py`.
- Similar-looking dog breeds may pose a challenge; consider this when interpreting results.

## Project Structure
- `classifier.py`: Contains the provided classifier function for image classification.
- `test_classifier.py`: Example program demonstrating how to use the classifier function.
- `requirements.txt`: Dependencies required for running the project.
