from django.shortcuts import render
import pandas as pd
import pickle

with open('predictor/attrition_model.pkl', 'rb') as file:
    model = pickle.load(file)

def home(request):
    result = None
    form_data = {}

    if request.method == 'POST':
        form_data = request.POST
        
        input_data = {
            'Location': [form_data.get('Location')],
            'Emp_Group': [form_data.get('Emp_Group')],
            'Function': [form_data.get('Function')],
            'Gender': [form_data.get('Gender')],
            'Tenure_Grp': [form_data.get('Tenure_Grp')],
            'Marital_Status': [form_data.get('Marital_Status')],
            'Hiring_Source': [form_data.get('Hiring_Source')],
            'PromotedNon_Promoted': [form_data.get('PromotedNon_Promoted')],
            'Job_Role_Match': [form_data.get('Job_Role_Match')],
            'Tenure': [float(form_data.get('Tenure'))],
            'Experience_YYMM': [float(form_data.get('Experience_YYMM'))],
            'Age_in_YY': [float(form_data.get('Age_in_YY'))]
        }
        df_input = pd.DataFrame(input_data)

        prediction = model.predict(df_input)[0]  

        if prediction == 1:
            result = "This employee is LIKELY TO LEAVE."
        else:
            result = "This employee is LIKELY TO STAY."

    return render(request, 'index.html', {'result': result, 'form_data': form_data})