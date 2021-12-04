from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Photo, Posting


class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea,label="Message to poster")


class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ('title', 'price', 'description',)
        labels = {
            'title': _('Posting Title'),
            'price': _('Price (dollars)'),
        }

class PhotoForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Photo
        fields = ('image',)

PhotoFormSet = forms.modelformset_factory(Photo, form=PhotoForm, extra=5,)