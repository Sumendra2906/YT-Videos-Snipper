from .models import VideosInfo
from .serializers import VideosInfoSerializer

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class StandardResultsSetPagination(PageNumberPagination):
    """
    Declaration Of Default Page Size
    """
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100

class VideosInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ** Search provides case-insensitive partial matches support.
    """
    queryset = VideosInfo.objects.all().order_by('-published_on')
    serializer_class = VideosInfoSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['published_on', 'created_at']
    search_fields = ['title', 'description']
    ordering_fields = ['published_on', 'created_at']

