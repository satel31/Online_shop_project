from django.urls import path
from apps.catalog.views import ProductListView, ProductCreateView, ProductByPageListView, PostListView, PostUpdateView, \
    PostDetailView, PostDeleteView, toggle_activity, PostCreateView

# products,add_products, all_products

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('add_products/', ProductCreateView.as_view(), name='add_products'),
    path('all_products/', ProductByPageListView.as_view(), name='all_products'),

    path('add_post/', PostCreateView.as_view(), name='add_post'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('post/toggle/<int:pk>', toggle_activity, name='toggle_activity'),
]
