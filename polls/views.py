from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404,  HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("question_text")[:5]
    return render(request, "index.html", {'latest_question_list':latest_question_list})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        return render(request, "404.html")
        #raise Http404("404.html")
    return render(request, "detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        context =  {"question": question,"error_message": "You didn't select a choice."}
        return render(request,"detail.html",context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

