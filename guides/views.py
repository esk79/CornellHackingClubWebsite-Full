from django.shortcuts import render
from .models import Guides
from django.db.models import Q

# Just using function based views for now because they're easy
def guides_home(request):
    queryset = Guides.objects.all()
    search = request.GET.get("query")
    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) | Q(description__icontains=search))
    context = {
        "guides": queryset,
    }

    return render(request, "guides.html", context)