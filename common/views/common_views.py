from django.shortcuts import render, redirect

def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, 'common/404.html', {})