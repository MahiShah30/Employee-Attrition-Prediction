This project is an end-to-end machine learning application designed to predict whether an employee is likely to leave their job. It uses a dataset of historical employee information to train a classification model, which is then deployed as a user-friendly web application.

You can view and test the live, deployed application here:

[Live Demo] https://employee-attrition-prediction-pogn.onrender.com/

Features

Real-time Predictions:Enter an employee's details into the web form and get an instant prediction on whether they are likely to stay or leave.
Machine Learning Backend: Powered by a Logistic Regression model trained on over 900 employee records.
Clean, Responsive UI: A modern and attractive user interface for a great user experience.
Fully Deployed: The entire application is deployed on the cloud using Render.

Project Workflow

This project was built following a standard machine learning project lifecycle:

1. Machine Learning Model Development:

   - Loaded and explored the HR dataset.
   - Performed data cleaning, handled missing values, and preprocessed the data (encoding, normalization).
   - Trained and evaluated three different classification models: Logistic Regression, Decision Tree, and Naive Bayes.
   - Compared the models using metrics like Accuracy, Precision, Recall, and F1-Score.
   - Selected the best-performing model (Logistic Regression) for deployment.

2. Web App Development using Django:

   - Built a Django-based web interface with a form to collect employee information.
   - Integrated the trained .pkl model to perform real-time predictions.
   - Designed a user-friendly interface to display the prediction result.

3. Deployment:
   - The complete Django application was pushed to a GitHub repository.
   - The application was deployed to the cloud using Render for public access.

Technologies Used

- Backend: Python, Django
- Frontend: HTML, CSS
- Machine Learning: Scikit-learn, Pandas, NumPy
- Deployment: Git, GitHub, Render, Gunicorn, Whitenoise

How to Run Locally

To set up and run this project on your own machine, follow these steps:

Prerequisites:

- Python 3.8+
- Git

Local Setup:

1. Clone the repository:

   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. Create and activate a virtual environment:

   # Create the environment

   python -m venv venv

   # Activate on Windows

   venv\Scripts\activate

   # Activate on macOS/Linux

   source venv/bin/activate

3. Install the required dependencies:

   pip install -r requirements.txt

4. Run the initial database migrations:

   python manage.py migrate

5. Start the development server:

   python manage.py runserver

6. Open your web browser and go to 'http://127.0.0.1:8000/' to see the application running.
