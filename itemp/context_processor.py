from .models import UserAccount,Module,ModuleProgress


def counter(request):
    count=0
    # user=UserAccount.objects.get(username=request.session['username'])
    # if user.role=="admin":
    var=UserAccount.objects.filter(role='developer',status=0)
    for v in var:
        count=count+1
    return {'count':count}
    # else:
    #     count=1
    #     var=Module.objects.filter(progress='pending')
    #     var1=Module.objects.filter(id=var.module_id,developer=request.session['username'])
    #     for v in var1:
    #         count=count+1
    #     return {'count':count}
