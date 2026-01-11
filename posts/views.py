from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from .models import Tag


@login_required
@require_POST
def create_tag(request):
    name = request.POST.get('name', '').strip()
    if name:
        Tag.objects.create(name=name)
        return redirect('tag_list')

    tags = Tag.objects.all()
    return render(request, 'tags/tag_list.html', {'tags': tags, 'error': 'Назва не може бути пуста'})


@login_required
@require_GET
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags/tag_list.html', {'tags': tags})