from django import forms
from django.contrib.auth.forms import BaseUserCreationForm
from .models import User



class SignupForm(BaseUserCreationForm):
    def __init__(self, *args, **kwargs):    # overriding 해서 커스텀하기 (필수 입력란)
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True  
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


    # 기본 폼에 더 추가할 사항(커스텀)
    class Meta(BaseUserCreationForm.Meta):
        model = User # 우리 앱에 있는 user모델로 변경해주어야함
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_email(self):
        pass