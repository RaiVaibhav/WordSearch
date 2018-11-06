from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.db.models.functions import Length
from .models import Word
from .serializers import WordSerializer
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response

class WordListAPIView(ListAPIView):
    serializer_class = WordSerializer
    renderer_classes = (JSONRenderer,)

    def get_queryset(self):
        queryset = Word.objects.all()
        word = self.request.query_params.get('word',None)
        if word is not None:
            queryset = Word.objects.get(name = word)
        return queryset

    def get(self, request, format=None):
        word = self.get_queryset()
        content = {'name': word.name, 'frequency': word.frequency}
        return Response(content)

# def word_detail(request, pk):
#     word = Word.objects.get(pk=pk)
#     data = {
#         'name': word.name,
#         'frequency': word.frequency
#     }
#     return JsonResponse(data)

def search_words(request):
    if request.method=='POST':
        search_text = request.POST['search_text']
    else:
        search_text=''
    words = Word.objects.filter(name__contains=search_text, name__startswith=search_text).order_by('-frequency')
    words = words.order_by(Length('name').asc())
    # words = words.objects.order_by('frequency')
    return render(request, 'ajax_search.html', {'words': words})

def home_view(request):
    message = 'Hello everyone'
    return render(request, 'base.html', {'msg': message})