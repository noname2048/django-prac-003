from django.forms import ModelForm
from . import models


class PostForm:
    class Meta:
        model = models.Post
        fields = [
            "message",
            "is_public",
        ]
