🏥 Disease Prediction System
🌟 Overview
The Disease Prediction System is a machine learning-powered web application that predicts potential diseases based on user-input symptoms. It utilizes a combination of Random Forest, Support Vector Machine (SVM), and Naïve Bayes models integrated via a weighted voting ensemble to ensure high prediction accuracy.

🔍 Features
✅ Multiple ML Models – Leverages the strengths of Random Forest, SVM, and Naïve Bayes.

✅ Weighted Voting System – Improves reliability by combining predictions from all models.

✅ Feature Selection – Focuses on the most informative symptoms to enhance prediction quality.

✅ Hyperparameter Tuning – Optimized via GridSearchCV for best performance.

✅ Streamlit Web Interface – Offers an intuitive and interactive UI for symptom input and disease prediction.

🛠 Setup Instructions
📥 1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/chaviva16/Disease_Prediction.git
cd Disease_Prediction
🧠 2. Model Training
The system trains three machine learning models using a structured dataset of symptoms and their corresponding diseases.
Key techniques include:

Oversampling (e.g., RandomOverSampler) to handle class imbalance

GridSearchCV for model tuning

The trained models include:

Random Forest

Support Vector Machine (SVM)

Naïve Bayes

📦 3. Download Pretrained Model
To reduce repository size, the Random Forest model is hosted externally.
➡️ Download here:
🔗 Download Random Forest Model

🚀 Usage
Run the Streamlit app locally:

bash
Copy
Edit
streamlit run app.py
This launches a web interface where users can select symptoms and receive disease predictions instantly.

🎯 Future Enhancements
📈 Expand Dataset – Incorporate more diverse and real-world clinical data

🧠 Add Deep Learning Models – Integrate Neural Networks or XGBoost for enhanced accuracy

🖱️ Improve UI/UX – Make symptom selection more intuitive and user-friendly

🌐 Deploy Online – Host the app on Streamlit Cloud, Render, or Heroku for public access

