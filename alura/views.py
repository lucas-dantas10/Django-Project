from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'alura/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailsView(generic.DetailView):
    model = Question
    template_name = 'alura/details.html'

class ResultView(generic.DetailView):
    model = Question
    template_name = 'alura/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,
            "alura/details.html",
            {
                "question": question,
                "error_message": "Você não selecionou um Choice"
            }  
        )

    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("alura:result", args=(question.id,)))

