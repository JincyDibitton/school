from django import forms
from django.forms import CheckboxInput
from django.forms.widgets import NumberInput 
from .models import Student,Courses,Department

purpose = (
    ("1", "Enquiry"),
    ("2", "Place Order"),
    ("3", "Return"),
    ("4", "Feedback"),
    ("5", "Queries"),
)
materials_choices = (
                    ('Notebook', 'Notebook'), 
                    ('Pen', 'Pen'),
                    ('Exam Papers', 'Exam Papers'),
                    ('Books', 'Books'))
gender_choices = (('M', 'Male'), ('F', 'Female'))

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
         
        widgets = { 'first_name': forms.TextInput(attrs={ 'class': 'form-control' }),
                   'last_name': forms.TextInput(attrs={ 'class': 'form-control' }),
                    'dob': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
                    'address':forms.TextInput(attrs={ 'class': 'form-control' }),
                    'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
                    
                    'age': forms.TextInput(attrs={ 'class': 'form-control' }),
                    'address': forms.TextInput(attrs={ 'class': 'form-control' }),
                    'department': forms.Select(attrs={'class': 'form-control'}),
                    'courses': forms.Select(attrs={'class': 'form-control'}),
                    'phoneNumber': forms.TextInput(attrs={'class': 'form-control'}),
                    
                    'gender': forms.RadioSelect
                    
                   
        } 
        
        purpose = forms.ChoiceField(choices=purpose)
        materials = forms.MultipleChoiceField(widget=forms.SelectMultiple,
                                             choices=materials_choices)
          
           
    #     widgets = {'gender': forms.RadioSelect}
        
    #     first_name = forms.CharField()  
    # last_name = forms.CharField()  
    # email = forms.EmailField()  
    # address = forms.CharField()  
    # dob = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))  
    # materials = forms.MultipleChoiceField(
    #         required=False,
    #         widget=forms.CheckboxSelectMultiple,
    #         choices=materials_choices,
    #     )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['courses'].queryset = Courses.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['courses'].queryset = Courses.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass    
        elif self.instance.pk:
            self.fields['courses'].queryset = self.instance.department.courses_set.order_by('name')