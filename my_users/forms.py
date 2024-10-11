from django import forms


class LoginForm(forms.Form):
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید', 'class': 'input-block-level'})

    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمزعبور خود را وارد کنید', 'class': 'input-block-level'}),
    )


class RegisterForm(forms.Form):
    phone_number = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder': "شماره تلفن خود را وارد کنید", 'class': "input-block-level"}))
    first_name = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder': "نام خود را وارد کنید", 'class': "input-block-level"}))
    last_name = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder': "نام خانوادگی خود را وارد کنید", 'type': 'tel', 'class': "input-block-level"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': "پسوورد خود را وارد کنید", 'class': "input-block-level"}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': "پسوورد خود را مجدد وارد کنید", 'class': "input-block-level"}))

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('کلمه عبور یکسان نیست')
        return password
