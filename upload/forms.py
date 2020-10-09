from django import forms

from upload.models import Future

class FutureForm(forms.ModelForm):
    class Meta:
        model = Future
        fields = (
            # 'hotel_code',
            'file_name',
            )


from django.forms import ClearableFileInput
from upload.models import ImportFiles
class ImportFilesForm(forms.ModelForm):
    class Meta:
        model = ImportFiles
        fields = ['files']
        widgets = {
            'files': ClearableFileInput(attrs={'multiple': True}),
        }