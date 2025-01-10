from django.shortcuts import render

def homepage(request):
  return render(request, 'templates/registration/base.html')  # Render the template
