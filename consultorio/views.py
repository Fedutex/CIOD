from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.contrib.auth.decorators import login_required


def consultorio(request):
    return render(request, 'consultorio/home.html', {})


def blog(request):
    from .models import Blog  # Importar el modelo Blog
    blogs = Blog.objects.all()

    return render(request, 'consultorio/blog.html', {'blogs': blogs})


@login_required
def create_blog(request):
    import re
    from .forms import BlogForm
    from urllib.parse import urljoin

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            
            title_slug = re.sub(r'[^a-zA-Z0-9]+', '_', blog.title.lower())  # Reemplazar todo lo que no sea alfanumérico por guiones bajos
            
            blog.url = urljoin(request.build_absolute_uri('/'), f"blog/{title_slug}/")
            blog.save()
            
            return redirect('blog')  
    else:
        form = BlogForm()

    return render(request, 'consultorio/create_blog.html', {'form': form})

def blog_detail(request, title_slug):
    # El slug se genera reemplazando caracteres especiales, por lo que debemos buscar de forma flexible
    blog = get_object_or_404(Blog, url__icontains=title_slug)  # Buscar el blog donde la URL contenga el slug
    return render(request, 'consultorio/blog_detail.html', {'blog': blog})

@login_required
def edit_blog(request, blog_id):
    from .forms import BlogForm
    blog = get_object_or_404(Blog, id=blog_id)  # Obtener el blog por su id

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)  # Pasar la instancia del blog al formulario
        if form.is_valid():
            blog = form.save(commit=False)

            # Volver a generar el title_slug para la URL si el título fue editado
            from urllib.parse import urljoin
            import re
            title_slug = re.sub(r'[^a-zA-Z0-9]+', '_', blog.title.lower())  # Eliminar caracteres especiales
            blog.url = urljoin(request.build_absolute_uri('/'), f"blog/{title_slug}/")
            
            blog.save()  # Guardar los cambios
            return redirect('blog')  # Redirigir al listado de blogs o a una página de éxito
    else:
        form = BlogForm(instance=blog)  # Cargar el formulario con los datos actuales del blog

    return render(request, 'consultorio/edit_blog.html', {'form': form, 'blog': blog})