from django import forms
class LoginForms(forms.Form):
    username=forms.CharField(label="Kullancı Adı",max_length=50,)
    password=forms.CharField(label="Parola", max_length=20, widget=forms.PasswordInput)
    

class RegisterForms(forms.Form):
    username=forms.CharField(max_length=50, label="Kullancı Adı")
    password=forms.CharField(max_length=20,label="Parola",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=20,label="Parolayı Dogurla",widget=forms.PasswordInput)
    
    def clean(self):
       username=self.cleaned_data.get("username")
       password=self.cleaned_data.get("password")
       confirm=self.cleaned_data.get("confirm")
       if password and confirm and password!=confirm:
           raise forms.ValidationError("Parolalar Eşleşmiyor")
       values={"username": username,
               "password": password
               }
       return values