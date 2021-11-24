from django import forms
from .models import Photo, Posting


class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)


class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ('title', 'rent', 'distance_time', 'distance_mode', 'description',)

class PhotoForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Photo
        fields = ('image', 'alt_text',)

PhotoFormSet = forms.modelformset_factory(Photo, form=PhotoForm, extra=5,)