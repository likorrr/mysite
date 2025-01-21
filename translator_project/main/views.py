from django.shortcuts import render
from googletrans import Translator
import asyncio

async def translate_text(txt, dest):
    async with Translator() as translator:
        result = await translator.translate(txt, dest=dest)
        return result

def index(request):
    if request.method == 'POST':
        lang = request.POST.get('lang', None)
        txt = request.POST.get('txt', None)

        translator = Translator()
        result = asyncio.run(translate_text(txt, lang))

        return render(request, 'main/index.html', {'result': result.text, 'lang':lang})
    return render(request, 'main/index.html')
        
        
