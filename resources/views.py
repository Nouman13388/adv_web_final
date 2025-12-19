from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Resource
from .forms import ResourceForm
from .decorators import role_required, can_delete_resource, can_edit_resource, get_user_role


def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('resource_list')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('resource_list')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'resources/login.html', {'form': form})


def logout_view(request):
    """User logout view"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


@login_required
def resource_list(request):
    """List all resources with pagination"""
    resources = Resource.objects.all()
    
    # Pagination
    paginator = Paginator(resources, 10)  # Show 10 resources per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    user_role = get_user_role(request.user)
    
    context = {
        'page_obj': page_obj,
        'user_role': user_role,
    }
    return render(request, 'resources/resource_list.html', context)


@login_required
def resource_detail(request, pk):
    """View a single resource"""
    resource = get_object_or_404(Resource, pk=pk)
    user_role = get_user_role(request.user)
    
    context = {
        'resource': resource,
        'user_role': user_role,
        'can_edit': can_edit_resource(request.user, resource),
        'can_delete': can_delete_resource(request.user, resource),
    }
    return render(request, 'resources/resource_detail.html', context)


@login_required
@role_required(['administrator', 'faculty'])
def resource_create(request):
    """Create a new resource"""
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.created_by = request.user
            resource.save()
            messages.success(request, 'Resource created successfully!')
            return redirect('resource_detail', pk=resource.pk)
    else:
        form = ResourceForm()
    
    return render(request, 'resources/resource_form.html', {'form': form, 'action': 'Create'})


@login_required
@role_required(['administrator', 'faculty'])
def resource_update(request, pk):
    """Update an existing resource"""
    resource = get_object_or_404(Resource, pk=pk)
    
    if not can_edit_resource(request.user, resource):
        messages.error(request, 'You do not have permission to edit this resource.')
        return redirect('resource_detail', pk=pk)
    
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resource updated successfully!')
            return redirect('resource_detail', pk=resource.pk)
    else:
        form = ResourceForm(instance=resource)
    
    return render(request, 'resources/resource_form.html', {'form': form, 'action': 'Update', 'resource': resource})


@login_required
def resource_delete(request, pk):
    """Delete a resource"""
    resource = get_object_or_404(Resource, pk=pk)
    
    if not can_delete_resource(request.user, resource):
        messages.error(request, 'You do not have permission to delete this resource.')
        return redirect('resource_detail', pk=pk)
    
    if request.method == 'POST':
        resource.delete()
        messages.success(request, 'Resource deleted successfully!')
        return redirect('resource_list')
    
    return render(request, 'resources/resource_confirm_delete.html', {'resource': resource})
