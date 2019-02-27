from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def check(value):
    if 'alex' in value:
        raise ValidationError('敏感词汇，不符合社会职业核心价值观')


class RegForm(forms.Form):
    user = forms.CharField(
        # disabled=True,
        label='用户名',
        # required=True,
        # min_length=8,
        # max_length=12,
        initial="张三",
        validators=[],
        error_messages={
            'required': '不能为空',
            'min_length': '长度不能小于8'
        }

    )
    email = forms.EmailField()
    pwd = forms.CharField(
        label='密码',
        widget=forms.PasswordInput()
    )

    re_pwd = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput()
    )

    # gender = forms.ChoiceField(
    #     choices=((1, '男'), (2, '女'), (3, 'alex')),
    #     widget=forms.RadioSelect()
    # )
    # phone = forms.CharField(
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$', '格式不正确')]
    # )
    #
    # hobby = forms.ChoiceField(choices=((1, "篮球"), (2, "足球"), (3, "双色球"),), widget=forms.SelectMultiple)

    def clean_user(self):
        value = self.cleaned_data.get('user')
        if 'alex' in value:
            raise ValidationError('不符合社会职业核心价值观')

        return value

    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        re_pwd = self.cleaned_data.get('re_pwd')

        if pwd != re_pwd:
            self.add_error('re_pwd', '两次密码不一致!!@!')
            raise ValidationError('两次密码不一致')
        return self.cleaned_data
