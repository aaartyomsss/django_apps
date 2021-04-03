from django.http import HttpResponse, Http404
from .models import Question
from django.shortcuts import render, get_object_or_404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list }  # The context is a dictionary mapping template variable names to Python objects.
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # shortcut to avoid try-catch
    return render(request, 'polls/details.html', { 'question': question })

def result(request, question_id):
    response = "You are looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)

