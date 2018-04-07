from django import forms

from django.forms import ModelForm, Select, TextInput
from socialdb.models import QueryUser

'''
@Desc
    表单
@Author monkey
@Date 2018-04-03
'''
# ======  另一种写法  ========
''''''
CONDITION_CHOICES = (
    ('username', '用户名'),
    ('password', '密码'),
    ('chineseName', '姓名'),
    ('email', '邮箱'),
    ('QQ', 'QQ'),
    ('identity_number', '身份证'),
    ('cell_phone', '电话'),
    ('college', '大学'),
    ('source', '来源'),
)

# class QueryUserForm(forms.Form):
#     condition = forms.CharField(  # 也可以定义为 ChoiceField
#         max_length=20,
#         widget=forms.Select(choices=CONDITION_CHOICES,
#                             attrs={'class':"form-control",
#                                     'title':"query condition",
#                                     'name':'condition',
#                                     }),
#         localize=('username', '用户名')
#     )
#
#     queryContent = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control is-invalid',
#                                       'name': 'queryContent',
#                                       'placeholder': '请输入需要要查询的内容...'
#                                       }),
#         error_messages={'required': '查询内容不能为空 !'}
#     )


# 上面的代码等同于 下面的表单 QueryUserForm + 模型 QueryUser

class QueryUserForm(ModelForm):

    class Meta:
        model = QueryUser
        fields = ['condition', 'queryContent', ]
        # 指定呈现样式字段、指定 CSS 样式
        widgets = {
            'condition': Select(attrs={'class':"form-control",
                                    'title':"query condition",
                                    'name':'condition',
                                    }),
            'queryContent':TextInput(attrs={'class': 'form-control is-invalid',
                                      'name': 'queryContent',
                                      'placeholder': '请输入需要要查询的内容...'
                                      })
        }

        localized = {
            'condition':('username', '用户名'),
            'queryContent':123
        }

        # 自定义错误信息
        error_messages = {
            'queryContent':{
                'required': '查询内容不能为空 !',
            }
        }