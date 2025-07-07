from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
#from .forms import *
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
ListView,DetailView,
CreateView,DeleteView,
UpdateView)
from . import models
from .forms import *
from django.core.files.storage import FileSystemStorage

import time
import pandas as pd
import numpy as np

#from sklearn.linear_model import LogisticRegression
import pickle
import matplotlib.pyplot as plt

np.random.seed(123) #ensure reproduc
class dataUploadView(View):
    form_class = hkdForm
    success_url = reverse_lazy('success')
    template_name = 'create.html'
    failure_url = reverse_lazy('fail')
    filenot_url = reverse_lazy('filenot')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            # Extract POST input fields
            field_names = [
                'age',
                'sex_male',         
                'cp',              
                'trestbps',        
                'chol',             
                'fbs',              
                'restecg',         
                'thalach',          
                'exang',           
                'oldpeak',          
                'slope',            
                'ca',               
                'thal'   
            ]

            try:
                # Convert to floats and check for invalid/missing inputs
                input_values = []
                for field in field_names:
                    val = request.POST.get(field, '').strip()
                    if val == '':
                        raise ValueError(f"Missing value for {field}")
                    input_values.append(float(val))

                # Load trained model
                filename = 'Rathiga_LogisticRegression_HKD.sav'
                classifier = pickle.load(open(filename, 'rb'))

               # Load the scaler
                scaler_filename = 'sc_input.sav'
                sc_input = pickle.load(open(scaler_filename, 'rb'))
                
                # Convert input to DataFrame
                columns = ['age', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
           'exang', 'oldpeak', 'slope', 'ca', 'thal', 'sex_male']

                input_df = pd.DataFrame([input_values], columns=columns)

                    # Apply scaler
                input_scaled = sc_input.transform(input_df)

                    # Predict
                out = classifier.predict(input_scaled)

                

                # Map results back for template (key value pair same name we use in succ_msg.html)
                context = {
                    'data_age': input_values[0],
                    'data_sex': input_values[1],
                    'data_cp': input_values[2],
                    'data_tres': input_values[3],
                    'data_chol': input_values[4],
                    'data_fbs': input_values[5],
                    'data_restecg': input_values[6],
                    'data_thalach': input_values[7],
                    'data_exang': input_values[8],
                    'data_oldpeak': input_values[9],
                    'data_slope': input_values[10],
                    'data_ca': input_values[11],
                    'data_thal': input_values[12],
                    'out': out[0]
                }

                return render(request, "succ_msg.html", context)

            except ValueError as ve:
                return HttpResponse(f"Invalid input: {ve}")

            except FileNotFoundError:
                return redirect(self.filenot_url)

            except Exception as e:
                return HttpResponse(f"Unexpected error: {str(e)}")

        else:
            return redirect(self.failure_url)
