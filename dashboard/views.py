from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    # Example data: you could query your models for stats
    context = {
        'welcome_message': f"Welcome, {request.user.username}!",
        'stats': {
            'total_users': 150,  # Example: fetch from your User model
            'active_sessions': 35,
        }
    }
    return render(request, 'dashboard/dashboard.html', context)