from django.shortcuts import render
from django.http import HttpResponse

from .models import Question,Answer

def index(request):
    query_list=Question.objects.all()
    if(request.method=='POST'):
        print(request.POST.get('choices'))

    context={
        'query_list':query_list
    }

    return render(request,'polls/index.html',context)

def details(request,question_id):
    queobj=Question.objects.get(pk=question_id)
    answer_list = Answer.objects.all().filter(question=queobj)
    context={
        'answer_list':answer_list,
        'queobj':queobj,
    }

    return render(request,'polls/details.html',context)

def votes(request,question_id):
    question1=Question.objects.get(pk=question_id)
    answer_list=Answer.objects.all().filter(question=question1)
    
    print(request.POST.get('choices'))
    for i in answer_list:
        if i.choice==request.POST.get('choices'):
            i.votes+=1
            i.save()
            
    context={ 'question1':question1 , 'answer_list':answer_list }
    return render(request,'polls/votes.html',context)
