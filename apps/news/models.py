from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField


class News(models.Model):
    """
    商品
    """
    title = models.TextField("文章标题", max_length=5000, default="")

    content_brief = models.TextField("文章描述", max_length=50000)
    content  = models.TextField("文章内容", max_length=101000,)
    contents = UEditorField(verbose_name=u"内容", default='')

    click_num = models.IntegerField("点击数", default=0)
    add_time = models.DateTimeField("文章发表时间", default=datetime.now)

    class Meta:
        verbose_name = '新闻模块'
        verbose_name_plural = verbose_name