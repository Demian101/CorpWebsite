import xadmin
from .models import News
#from .models import IndexAd

# title = models.CharField("商品唯一货号", max_length=50, default="")
# content_brief = models.TextField("文章描述", max_length=500)
# content = models.CharField("文章内容", max_length=1000, )
# contents = UEditorField(verbose_name=u"内容", default='')
# click_num = models.IntegerField("点击数", default=0)
# add_time = models.DateTimeField("文章发表时间", default=datetime.now)
# class Meta:
#     verbose_name = '新闻模块'
#     verbose_name_plural = verbose_name

class NewsAdmin(object):
    # 显示的列
    #list_display = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
     #               "shop_price", "goods_brief", "goods_desc", "is_new", "is_hot", "add_time"]
    list_display = ["title", "content_brief",  "content",
                    "click_num", "add_time"]
    # 可以搜索的字段
    search_fields = ['title', ]
    ### 列表页可以直接编辑的
    ###list_editable = ["is_hot", ]
    # 过滤器
    list_display = ["title", "content_brief",  "content",
                    "click_num", "add_time"]
    # 富文本编辑器
    style_fields = {"contents": "ueditor"}
    #
    # # 在添加商品的时候可以添加商品图片
    # class GoodsImagesInline(object):
    #     model = GoodsImage
    #     exclude = ["add_time"]
    #     extra = 1
    #     style = 'tab'
    # inlines = [GoodsImagesInline]

# models 类 和 xadmin  类 , 绑定
xadmin.site.register(News, NewsAdmin)

# xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
# xadmin.site.register(Banner, BannerGoodsAdmin)
# xadmin.site.register(GoodsCategoryBrand, GoodsBrandAdmin)

### 注释掉的是 边栏一级目录 : 产品管理 的几个 band
#xadmin.site.register(HotSearchWords, HotSearchAdmin)
#xadmin.site.register(IndexAd, IndexAdAdmin)

#
# class GoodsCategoryAdmin(object):
#     list_display = ["name", "category_type", "parent_category", "add_time"]
#     list_filter = ["category_type", "parent_category", "name"]
#     search_fields = ['name', ]
#
#
# class GoodsBrandAdmin(object):
#     list_display = ["category", "image", "name", "desc"]
#
#     def get_context(self):
#         context = super(GoodsBrandAdmin, self).get_context()
#         if 'form' in context:
#             context['form'].fields['category'].queryset = GoodsCategory.objects.filter(category_type=1)
#         return context
#
#
# class BannerGoodsAdmin(object):
#     list_display = ["goods", "image", "index"]
#
#
# class HotSearchAdmin(object):
#     list_display = ["keywords", "index", "add_time"]
#
#
# class IndexAdAdmin(object):
#     list_display = ["category", "goods"]