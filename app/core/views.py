from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.db import models


def stats_view(request):
    user_with_courses_count = User.objects.filter(courses_created__isnull=False).distinct().count()
    user_without_courses_count = User.objects.filter(courses_created__isnull=True).count()
    avg_courses_joined = User.objects.annotate(jumlah=models.Count('courses_joined')).aggregate(models.Avg('jumlah'))['jumlah__avg']
    most_active_user = User.objects.annotate(jumlah=models.Count('courses_joined')).order_by('-jumlah').first()
    inactive_users = User.objects.filter(courses_joined__isnull=True)

    context = {
        'user_with_courses_count': user_with_courses_count,
        'user_without_courses_count': user_without_courses_count,
        'avg_courses_joined': avg_courses_joined,
        'most_active_user': most_active_user,
        'inactive_users': inactive_users,
    }
    return render(request, 'stats.html', context)

def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            User.objects.create(name=name)
            return redirect('stats')
    return render(request, 'add_user.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.save()
        return redirect('user_list')
    return render(request, 'edit_user.html', {'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('user_list')
