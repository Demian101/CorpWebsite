from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = '用户管理'  # #app名字后台显示中文

    # def ready(self):
    #     import users.signals
