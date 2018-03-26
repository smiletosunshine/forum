# coding: utf8

from django.shortcuts import render

from user.models import User, Permission


def check_perm(need_perm):
    def wrap1(view_func):
        def wrap2(request, *args, **kwargs):
            uid = request.session.get('uid')
            if uid is None:
                level = 1
            else:
                user = User.objects.get(id=uid)
                level = user.perm.level

            # 检查权限
            perm = Permission.objects.get(name=need_perm)  # 获取对应权限的实例
            if level >= perm.level:
                return view_func(request, *args, **kwargs)
            else:
                return render(request, 'blockers.html')
        return wrap2
    return wrap1
