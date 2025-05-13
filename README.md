# 🏥 Disease Prediction System  

## 🌟 Overview  
The **Disease Prediction System** is a machine learning-powered web application that predicts diseases based on user input symptoms. It leverages **Random Forest, SVM, 
and Naïve Bayes** models combined with a **weighted voting system** for enhanced accuracy.

## 🔍 Features  
✔ **Machine Learning Models** – Uses **Random Forest, SVM, and Naïve Bayes** for predictions.  
✔ **Weighted Voting System** – Combines predictions from different models for better reliability.  
✔ **Feature Selection** – Identifies key symptoms for improved disease classification.  
✔ **Hyperparameter Tuning** – Optimized settings using **GridSearchCV**.  
✔ **Streamlit Web App** – Provides an interactive **web-based interface** for easy user interaction.  

## 🛠 Setup Instructions  
### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/chaviva16/Disease_Prediction.git
cd Disease_Prediction

📊 Model Training
This project trains three machine learning models:

Random Forest

Support Vector Machine (SVM)

Naïve Bayes

The models are trained on a structured disease dataset containing symptoms mapped to different illnesses.
 Oversampling techniques such as RandomOverSampler are used to balance the data.

Download the Random Forest Model
Since the Random Forest model is large, it has been uploaded separately to Google Drive. Download it here:
https://drive.google.com/file/d/1kM3tHz1DsbWnCLx9c_hfmbn9AS-nZ95s/view?usp=sharing

## 🎯 Future Work & Improvements
✅ Get More Data – Expand the dataset with real-world medical cases for better generalization.
 ✅ Integrate Deep Learning – Implement Neural Networks or XGBoost for improved accuracy.
 ✅ Enhance User Interface – Make symptom selection more interactive and intuitive.
 ✅ Deploy Online – Host the Streamlit app using Streamlit Cloud or Render for public access.
