# app/inventory/forms.py

# Import django/third parties modules
from django import forms 

# Import from locals
from app.inventory.models import Category, SubCategory

# Create your form here

class CategoryForm(forms.ModelForm):
	class Meta:
		model=Category
		fields=['description','state']
		label={'description':'Description of the Category','state':'State'}
		widget={'description': forms.TextInput}

	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    for field in iter(self.fields):
	    	self.fields[field].widget.attrs.update({
	    		'class':'form-control'
	    	})


class SubCategoryForm(forms.ModelForm):
	class Meta:
		model=SubCategory
		fields=['category','description','state']
		label={'description':'Description of the Sub Category','state':'State'}
		widget={'description': forms.TextInput}

	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    for field in iter(self.fields):
	    	self.fields[field].widget.attrs.update({
	    		'class':'form-control'
	    	})
	    self.fields["category"].empty_label - "Select Category"