from django.shortcuts import render
from django.http import JsonResponse
import openai


api_key = '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'
openai.api_key = api_key

def ask_openAI(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokecs = 150,
        n =1,
        stop=None,
        temperature=0.7,
    )
    openAI_response = response.choices[0].text.strip()
    return openAI_response

# Create your views here.

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        # me trying shitty things
        if (message.lower()) == "shubham":
            response = "Shubham ka naam izzjat se lio gand faad dunga sale"
        elif ((" chut " or " gand" or " lund" or " bsdk" or " bhosda" or " saale" or " kutte" or " kamine") in message):
            response = "mc gaali kisko de raha hai bsdk. ghar mein maa behen nahi hai kya"
        elif "tu" in message:
            response = "tu nahi aap karke baat kar bsdk"
        elif (("shubham" and "chutiya") in (message.lower())):
            response = "saale Shubham bhai ka naam izzjat se lio gand maar dunga ni toh"
        # end
        else :
            response = ask_openAI(message)
        return JsonResponse({'message':message, 'response':response})
    return render(request, 'chatbot.html')