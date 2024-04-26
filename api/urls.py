from django.urls import path
from e_commerce.api.views import *

urlpatterns = [
    path('comic-list/', comic_list_api_view),
    path('comic-retrieve/', comic_retrieve_api_view),
    path('comic-create/', comic_create_api_view),
    path('comic-filtered/', comic_list_filtered_api_view),
    path('comic-stock-filtered/', comic_list_stock_ordered_api_view),
    path('comic-ordered-by/', comic_list_ordered_by_api_view)
]
