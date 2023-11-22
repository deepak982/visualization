from django.shortcuts import render
from .serializers import dataSerializers
from .models import data
from rest_framework import viewsets
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.http import JsonResponse

def home (request):
    Data = data.objects.all().values('topic', 'intensity' , 'likelihood' , 'title' , 'relevance' , 'country' , 'end_year')

    topic = [item['topic'] for item in Data]
    title = [item['title'] for item in Data]
    intensity = [item['intensity'] for item in Data]
    likelihood = [item['likelihood'] for item in Data]
    relevance = [item['relevance'] for item in Data]
    country = [item['country'] for item in Data]
    end_year = [item['end_year'] for item in Data]


    context = {
        'topic': topic,
        'intensity': intensity,
        'title': title,
        'likelihood': likelihood,
        'country': country,
        'relevance':relevance,
        'end_year':end_year,
    }

    return render(request, 'index.html', context)


class DataViewset(viewsets.ModelViewSet):
    queryset = data.objects.all()
    serializer_class = dataSerializers
