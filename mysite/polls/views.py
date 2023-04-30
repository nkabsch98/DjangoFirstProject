from django.http import HttpResponse

from .models import Question

# Create your views here.
# /polls/
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# /polls/id
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

# /polls/id/results/
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# /polls/id/vote/
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)