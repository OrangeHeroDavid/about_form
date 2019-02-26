from django.shortcuts import render, HttpResponse
from app1.forms import RegForm

# Create your views here.
def reg(request):
    name_error = ''
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if len(user) < 8:
            name_error = '用户名太短了，不能少于8位'
        else:
            return HttpResponse('注册成功')

    return render(request, 'reg.html', {'name_error': name_error})




def reg2(request):
    form_obj = RegForm()  # 实例化form对象
    print(form_obj.fields,type(form_obj.fields))

    if request.method == 'POST':
        form_obj = RegForm(data=request.POST)
        # print(form_obj.cleaned_data)
        if form_obj.is_valid():
            # 把数据保存在数据库中
            # cleaned_data  表示经过校验的合格的数据
            print(form_obj.cleaned_data)


    return render(request, 'reg2.html', {'form_obj': form_obj})
