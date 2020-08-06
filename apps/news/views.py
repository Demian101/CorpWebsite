from rest_framework.response import Response
from rest_framework import filters
from rest_framework import generics
from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .serializers import NewsSerializer
#from .filters import GoodsFilter
from .models import News


class NewsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list: 商品分类列表数据
    """
    #queryset = News.objects.filter(category_type=1)
    #queryset = News.objects.get_queryset()   # 找出符合筛选的条件的所有对象中的第一项。
    queryset = News.objects.all()  # 找出符合筛选的条件的所有对象中的第一项。

    serializer_class = NewsSerializer
    pagination_class = None

    # 2020-08-06 新增
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            response = self.retrieve(request, *args, **kwargs)
        else:
            # mixins提供的list方法的响应对象是Response，想将该对象格式化为APIResponse
            response = self.list(request, *args, **kwargs)
        # response的数据都存放在response.data中
        return APIResponse(results=response.data)

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        return APIResponse(results=response.data)

class NewsPagination(PageNumberPagination):
    """
    商品列表自定义分页
    """

    # 默认每页显示的个数
    page_size = 10
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100

#
# class NewsListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     """
#     list:
#         商品列表数据
#     """
#     queryset = Goods.objects.all().order_by("id")
#     pagination_class = GoodsPagination
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
#     filter_class = GoodsFilter
#     # 设置filter的类为我们自定义的类
#     serializer_class = GoodSerializer
#     throttle_classes = (UserRateThrottle, AnonRateThrottle)
#     # 搜索
#     search_fields = ('name', 'goods_brief', 'goods_desc')
#     # 排序
#     ordering_fields = ('sold_num', 'shop_price')
#
#     # 商品点击数 + 1
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.click_num += 1
#         instance.save()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)