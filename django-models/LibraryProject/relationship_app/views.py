from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and user.profile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin.html', {'message': 'Welcome, Admin!'})

def is_librarian(user):
    return user.is_authenticated and user.profile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian.html', {'message': 'Welcome, Librarian!'})

def is_member(user):
    return user.is_authenticated and user.profile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member.html', {'message': 'Welcome, Member!'})