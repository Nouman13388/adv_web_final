from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def role_required(allowed_roles):
    """Decorator to check if user has required role"""
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            
            user_role = get_user_role(request.user)
            
            if user_role not in allowed_roles:
                messages.error(request, 'You do not have permission to access this page.')
                return redirect('resource_list')
            
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def get_user_role(user):
    """Get user role based on groups or superuser status"""
    if user.is_superuser:
        return 'administrator'
    elif user.groups.filter(name='Faculty').exists():
        return 'faculty'
    elif user.groups.filter(name='Student').exists():
        return 'student'
    else:
        return 'student'  # Default role


def can_delete_resource(user, resource):
    """Check if user can delete a resource"""
    user_role = get_user_role(user)
    
    if user_role == 'administrator':
        return True
    elif user_role == 'faculty':
        # Faculty can only delete their own resources
        return resource.created_by == user
    else:
        return False


def can_edit_resource(user, resource):
    """Check if user can edit a resource"""
    user_role = get_user_role(user)
    
    if user_role in ['administrator', 'faculty']:
        return True
    else:
        return False
