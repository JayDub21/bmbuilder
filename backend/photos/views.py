from django.shortcuts import render, redirect
from .models import Category, Photo

def gallery(request):
    search_field = ''
    category = request.GET.get('category')
    # search_field = request.GET.get('search')

    if category == None:
       photos = Photo.objects.all().order_by('-id')
    # elif 'search' in request.GET: 
    #     search_field = request.GET['search']
    #     photos = Photo.objects.all().filter(description = search_field)
    else: 
        photos = Photo.objects.filter(category__name__contains = category).order_by('-id')

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos, 'search_field': search_field}
    return render(request, 'photos/gallery.html', context)



def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})



def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none': 
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category: None
        
        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image, 
        )
    
        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)