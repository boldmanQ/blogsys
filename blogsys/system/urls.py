#import debug_toolbar
#import silk
#from xadmin.plugins import xversion
from django.contrib import admin
from rest_framework import routers, documentation

from django.conf import settings
#from django.conf.urls import url, include
from django.views.decorators.cache import cache_page
from django.urls import path, include
from django.conf.urls.static import static
from django.views.static import serve

from blog.views import IndexView, CategoryView, TagView, PostView, AuthorView
from extra.views import LinkView
from comment.views import CommentView
from blog.api import PostViewSet, CategoryViewSet, TagViewSet, UserViewSet
# from config.views import links


#xversion.register_models()
#xadmin.autodiscover()

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'cats', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'users', UserViewSet)


#def static(prefix, view=serve, **kwargs):
#    return [path(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), view, kwargs=kwargs)]


urlpatterns = [
    path('', cache_page(60)(IndexView.as_view()), name="index"),
    path('category/<str:category_name>/', CategoryView.as_view(), name='category'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='tag'),
    path('post/<slug:slug>/', PostView.as_view(), name='detail'),
    path('author/<str:author_username>/', AuthorView.as_view(), name='author'),
    path('links/', LinkView.as_view(), name='links'),
    path('admin/', admin.site.urls),
    path('comment/', CommentView.as_view(), name="Comment"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/', include(router.urls)),
    path('api/docs/', documentation.include_docs_urls(title='blogsys apis')),
] + static(settings.MEDIA_URL, serve, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, serve, document_root=settings.STATIC_ROOT)


#if settings.DEBUG:
#    #import debug_toolbar
#    urlpatterns += [
#        url(r'^__debug__/', include(debug_toolbar.urls)),
##        url(r'^silk/', include('silk.urls', namespace='silk')),
#    ]
