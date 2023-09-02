from django.shortcuts import render, redirect
from .models import Animation

def add_animation(request):
    if request.method == 'POST':
        mode = request.POST.get('mode')
        character = request.POST.get('character')
        dir_head = request.POST.get('dir_head')
        emotion = request.POST.get('emotion')
        dir_eye = request.POST.get('dir_eye')
        word = request.POST.get('word')
        body = request.POST.get('body')
        background = request.POST.get('background')
        foreground = request.POST.get('foreground')
        
        Animation.objects.create(
            mode=mode,
            character=character,
            dir_head=dir_head,
            emotion=emotion,
            dir_eye=dir_eye,
            word=word,
            body=body,
            background=background,
            foreground=foreground
        )
        # Redirect to a success page or render a response
        return redirect('add_animation')
    
    return render(request, 'animation_form.html')
