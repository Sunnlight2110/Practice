from django.shortcuts import render

def recipe(request):
   template_name = 'template'
   context = {}
   if request.method == 'GET' :
       
       pass
   if request.method == 'POST' :
       pass
   return render(request,template_name = 'recipe.html',context={})

