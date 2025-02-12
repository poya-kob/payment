from django import forms


class LoginForm(forms.Form):
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'شماره تلفن  خود را وارد کنید', 'type': 'tel'})

    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمزعبور خود را وارد کنید'}),
    )


class RegisterForm(forms.Form):
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "شماره تلفن خود را وارد کنید", 'type': 'tel'}))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "نام خود را وارد کنید"}))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "نام خانوادگی خود را وارد کنید"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': "پسوورد خود را وارد کنید"}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': "پسوورد خود را مجدد وارد کنید"}))

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('کلمه عبور یکسان نیست')
        return password
