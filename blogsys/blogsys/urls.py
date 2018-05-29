import xadmin
from xadmin.plugins import xversion
from rest_framework import routers, documentation

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from blog.views import IndexView, CategoryView, TagView, PostView, AuthorView
from config.views import LinkView
from comment.views import CommentView
from blog.api import PostViewSet, CategoryViewSet, TagViewSet, UserViewSet
# from config.views import links


xversion.register_models()
xadmin.autodiscover()

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'cats', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^category/(?P<category_id>\d+)', CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>\d+)/', TagView.as_view(), name='tag'),
    url(r'^post/(?P<pk>\d+)/', PostView.as_view(), name='detail'),
    url(r'^author/(?P<author_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^links/$', LinkView.as_view(), name='links'),
    url(r'^admin/', xadmin.site.urls),
    # url(r'^cus_admin/', custom_site.urls),
    url(r'^comment/$', CommentView.as_view(), name="Comment"),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api/docs/', documentation.include_docs_urls(title='blogsys apis')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
