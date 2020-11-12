from .models import Question
from django.template import loader
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework import permissions
from quickstart.serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

# This is the web page located at http://127.0.0.1:8000/quickstart/
def index(request):
    # To use a html template where CSS or JS will be loaded
    template = loader.get_template('quickstart/index.html')
    context = {}
    return HttpResponse(template.render(context, request)) # <--- this is rendering the template with some context in case is needed by the template
    #return HttpResponse("Hello, world. You're at the polls index.") <--- This returns plain text only