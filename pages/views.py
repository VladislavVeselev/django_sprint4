from django.shortcuts import render


def page_not_found(request, exception):
    """Страница 404."""
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    """Страница 403 CSRF."""
    return render(request, 'pages/403csrf.html', status=403)


def server_error(request):
    """Страница 500."""
    return render(request, 'pages/500.html', status=500)


def about(request):
    """Страница 'О проекте'."""
    return render(request, 'pages/about.html')


def rules(request):
    """Страница 'Правила'."""
    return render(request, 'pages/rules.html')