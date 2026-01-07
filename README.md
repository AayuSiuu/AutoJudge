# AutoJudge🧑‍⚖️🧠
## *Automatic Programming Problem Difficulty Predictor using NLP and ML 🤖*

### AutoJudge is a machine learning based system that uses only the textual description of the programmimg problem to automatically predict its difficulty. 
### By identifying patterns in previous problem statements, it removes manual bias in difficulty labeling.
### It predicts: 
- **Difficulty Class** 🏷️: Easy/Medium/Hard
- **Difficulty Score** 📊: Numerical Difficulty score out of 10

## 🤔💭 Why AutoJudge? 
### Online coding platforms (Codeforces, CodeChef, Kattis, etc.) typically assign problem difficulty based on human judgment and user submissions. AutoJudge demonstrates how Natural Language Processing (NLP) and Machine Learning can be used to automate this process before any submissions exist.

## 🤩 Key Features
- Uses only **textual description**
- Dual model pipeline:
  - **Classification** : easy/medium/hard
  - **Regression** : difficulty score
- Feature-engineered NLP approach (**TF-IDF + text statistics**)
- Simple **web interface** for **real time predictions**

## 📄 Dataset Overview
### Each problem entry contains:
- `title`
- `description`
- `input_description`
- `output_description`
- `sample_io`
- `problem_class` (Easy/Medium/Hard)
- `problem_score` (0–10 scale)
#### The dataset is pre-labeled and is used strictly for training and evaluation. No manual labeling is done.
#### The dataset link is provided for reference and reproducibility: https://github.com/AREEG94FAHAD/TaskComplexityEval-24

## 🧠 Methodology
### 🔹 Text Preprocessing
- Cleaned and normalized text  
- Combined all text fields into a single input  
- Handled missing values  

### 🔹 Feature Engineering
- TF-IDF vectorization  
- Text length statistics  
- Keyword frequency (e.g., *dp, graph, recursion*)  
- Mathematical symbol count  

### 🔹 Models Used

**Classification**
- Logistic Regression  
- Random Forest  
- Support Vector Machine (SVM)  

**Regression**
- Linear Regression  
- Random Forest Regressor  
- Gradient Boosting Regressor

### All these models were tryed out in the Jupyter Notebook
### Accuracy comparison in classifiers
<img width="541" height="204" alt="image" src="https://github.com/user-attachments/assets/7b37a7ab-979e-4e6f-aa40-6ceb063713ad" />

### Regression Model comparison
<img width="581" height="183" alt="image" src="https://github.com/user-attachments/assets/135ac35f-e889-442d-a643-6e5e50216391" />

## 📈 Evaluation & Model Selection
### Evaluation Metrics
- **Classification**: Accuracy, Confusion Matrix  
- **Regression**: MAE, RMSE  

### Final Model Selection
- **Classification**: Random Forest Classifier
- **Regression**: Ridge Regressor(L-2 regularized Linear Regressor) 

## 🌐 Web Application

A lightweight web UI allows users to paste a new programming problem and instantly obtain predictions.

**Users can:**
- Paste the problem description  
- Add input and output specifications  
- Click **Predict** to view:
  - Predicted difficulty class (Easy/Medium/Hard)
  - Predicted difficulty score (0–10 scale)
<img width="1918" height="1056" alt="image" src="https://github.com/user-attachments/assets/91cdb432-9806-48d9-9dd9-f392c3f89bf1" />
<img width="1919" height="910" alt="image" src="https://github.com/user-attachments/assets/5153ca53-d6b5-4b85-8fbb-814da6ccad76" />

## 🛠️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/AayuSiuu/AutoJudge.git
cd AutoJudge

# Install dependencies
pip install -r requirements.txt

# Run the web app
streamlit run app.py # or use : "python -m streamlit run app.py"
```
## 👩‍💻 Author

**Aayushi Sinha**  
🔗 GitHub: https://github.com/AayuSiuu

