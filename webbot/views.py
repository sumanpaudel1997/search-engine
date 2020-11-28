from django.shortcuts import render
from html.parser import HTMLParser

import wolframalpha
import wikipedia




def index(request):
    return render(request, 'webbot/index.htm')


def bot_search(request):
    query = request.GET.get('query')

    
    try:
        client = wolframalpha.Client("<--Your API key-->")
        res = client.query(query)
        ans = next(res.results).text
        return render(request, 'webbot/index.htm', {'ans': ans, 'query': query})




    except Exception:
        try:
            ans = wikipedia.summary(query, sentences=10)
            return render(request, 'webbot/index.htm', {'ans': ans, 'query': query})


        except Exception:

            ans ="We couln't find what you have searched.Try search again ?"
            return render(request, 'webbot/index.htm', {'ans': ans, 'query': query})


