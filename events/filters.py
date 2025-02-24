import django_filters

from .models import Event


class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Event Title')
    location = django_filters.CharFilter(lookup_expr='icontains', label='Location')
    date = django_filters.DateFromToRangeFilter(label='Event Date')

    class Meta:
        model = Event
        fields = ['title', 'location', 'date']
