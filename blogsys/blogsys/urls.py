import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()


from django.conf.urls import url

from blog.views import IndexView, CategoryView, TagView, PostView, AuthorView
from config.views import LinkView
from comment.views import CommentView
# from config.views import links


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
    #url(r'^polls/', include('practice.urls')),
]
