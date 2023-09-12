from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse,HttpRequest
import openai

openai_api_key = 'your CHATGPY API KEY'
openai.api_key = openai_api_key

"""def ask_openai(message):
    response=openai.Completion.create(
        model = "gpt-3.5-turbo",
        prompt = message,
        max_tokens = 150,
        n=1,
        stop=None,
        temperature=0.7,
    
    )
    #print(response)
    answer=response.choices[0].text.strip()
    #answer = response.choices[0].message.content.strip()
    return answer"""
    
def ask_openai(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = message + "multiple choice question with Json format with options line by line " + message  ,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    print(response)  
    answer = response.choices[0].text.strip()
    return answer
# Create your views here.




def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message':message, 'response':response})
    return render(request,'chatbot.html')
