from django.db import models


class User(models.Model):
    SEX = (
        ('M', '男'),
        ('F', '女'),
        ('U', '保密'),
    )

    nickname = models.CharField(max_length=64, unique=True, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)
    icon = models.ImageField()
    age = models.IntegerField()
    sex = models.CharField(max_length=8, choices=SEX)
    perm_id = models.IntegerField(default=1)

    @property
    def perm(self):
        if not hasattr(self, '_perm'):
            self._perm = Permission.objects.get(id=self.perm_id)
        return self._perm


class Permission(models.Model):
    '''
    权限表
    ====================
    id   name      level
    --   ----      -----
    1    guest         1
    5    user          2
    7    manager       3
    8    boss       9999
    9    leader        4
    '''
    name = models.CharField(max_length=16, unique=True)
    level = models.IntegerField(default=0)
