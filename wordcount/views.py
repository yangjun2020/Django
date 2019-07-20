from django.http import HttpResponse 
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()    

    dict_cnt = {}
    max_cnt = 0
    max_word = ''

    for w in wordlist:
        if w not in dict_cnt:
            dict_cnt[w] = 1
        else: #found the word in dict_cnt
            dict_cnt[w]+=1            
        if dict_cnt[w] >= max_cnt:
            max_cnt = dict_cnt[w]
            max_word = w

    return render(request, 'count.html', {'fulltext':fulltext, 'len':len(wordlist), 'max_word':max_word, 'dict_cnt': dict_cnt.items()})