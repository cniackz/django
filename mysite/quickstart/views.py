from django.shortcuts import render
from .models import Question
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]