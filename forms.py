from django import forms
from .models import hkdModel

class hkdForm(forms.ModelForm):
    class Meta:
        model = hkdModel
        fields = [
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

        widgets = {
            'sex_male': forms.Select(choices=[(1, 'Male'), (0, 'Female')]),
            'fbs': forms.Select(choices=[(1, 'True'), (0, 'False')]),
            'exang': forms.Select(choices=[(1, 'Yes'), (0, 'No')]),
            'cp': forms.Select(choices=[(0, 'Type 0'), (1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')]),
            'restecg': forms.Select(choices=[(0, 'Normal'), (1, 'Abnormal'), (2, 'Hypertrophy')]),
            'slope': forms.Select(choices=[(0, 'Upsloping'), (1, 'Flat'), (2, 'Downsloping')]),
            'ca': forms.Select(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')]),
            'thal': forms.Select(choices=[(1, 'Normal'), (2, 'Fixed Defect'), (3, 'Reversible Defect')]),
        }
