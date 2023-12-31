from django import forms # import the forms library
#from django.forms import ModelForm # This allows me to set up a ModelForm
from .models import AllPosts # This is the class I need for ModelFOrm

class UserForm(forms.ModelForm):
    class Meta:
        model = AllPosts
        fields = [             
            'user_search_terms'
        ]
        labels = {
        "user_search_terms": ""  # This lets me override the model field name with something nicer or with nothing
        } 
        ### NOTE ####
        # I haven't figured out yet how to have both of these widgets combined
        
        # This will make the default input box longer, and will include a placeholder 
        widgets = {  
                    'user_search_terms': 
                    forms.Textarea
                    (attrs={'rows':2, 'cols':60,'placeholder': 'examples: OSU, Quicken, TOZO earbuds, chatgpt, Buffalo NAS device '}),
                     
                  }
      
  