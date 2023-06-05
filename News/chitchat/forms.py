from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Post


class PostForm(forms.ModelForm):
    # text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            # 'author',
            'post_category',
            'title',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title == text:
            raise ValidationError(
                _("Heading must not be identical to text.")
            )
        if len(text) <= 20:
            raise ValidationError(
                _("Text length cannot be less 20 than characters")
            )

        return cleaned_data
