from django.shortcuts import render
import openai
from openai import OpenAI
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json 
# Create your views here.

openai.api_key=''

conversation_history=[]

@csrf_exempt
def chat(request):
    if request.method=="POST":
        data=json.loads(request.body)
        user_message=data.get("message")

        client=OpenAI()

        conversation_history.append({'role':'user','content':user_message})

        res=client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history
        )

        bot_message= res.choices[0].message.content

        conversation_history.append({"role":"assistant","content":bot_message})

        return JsonResponse({"message":bot_message})
    return JsonResponse({"error":"Invalid request method"},status=400)

def home(request):
    return render(request,'chat.html')