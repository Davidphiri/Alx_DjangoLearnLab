
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import CustomUser

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

@permission_required('bookshelf.can_create', raise_exception=True)
def user_create(request):
    if request.method == 'POST':
        # Handle user creation
        pass
    return render(request, 'user_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def user_edit(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
        # Handle user edit
        pass
    return render(request, 'user_form.html', {'user': user})

@permission_required('bookshelf.can_delete', raise_exception=True)
def user_delete(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})
