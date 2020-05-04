from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def count(request):
    content = request.GET["text"]
    count_text = len(request.GET['text'])
    word_dict = {}
    for word in content:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    return render(request, "count.html", {"total": count_text, "word_count": word_dict.items()})
