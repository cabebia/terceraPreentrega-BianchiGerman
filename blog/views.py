from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import BlogPost
# Create your views here.

def v_index(request):
    last_4_post = BlogPost.objects.all().order_by('-id')[:4]

    return render(request, 'blog/index.html', {"posts": last_4_post})

def add_3_users(request):
    last_4_post = BlogPost.objects.all().order_by('-id')[:4]
    for post in last_4_post:
        blog_post_1 = BlogPost(
        userId=post.userId,  # Asume que hay al menos un usuario en la base de datos
        title="El lanzamiento del nuevo iPhone 14 revoluciona el mercado",
        subtitle="Apple sorprende con innovaciones tecnológicas",
        postdate="2023-10-20",
        postContent="Apple ha lanzado su último iPhone, el iPhone 14, que ha dejado a todos asombrados con sus características revolucionarias. Este nuevo dispositivo presenta una pantalla plegable, una batería de larga duración y una cámara mejorada que redefine la fotografía en los teléfonos inteligentes. Además, se espera que el iPhone 14 sea compatible con la tecnología 5G en todo el mundo, lo que permitirá velocidades de conexión más rápidas y una mejor experiencia de usuario."
        )

        # Segundo objeto
        blog_post_2 = BlogPost(
            userId=post.userId,
            title="Las criptomonedas alcanzan un nuevo récord de valor",
            subtitle="Bitcoin y Ethereum lideran la tendencia alcista",
            postdate="2023-10-15",
            postContent="El mercado de criptomonedas ha sido testigo de un aumento impresionante en el valor de Bitcoin y Ethereum. El Bitcoin ha alcanzado un nuevo máximo histórico, superando los $100,000 por moneda, mientras que Ethereum ha superado los $5,000. Este repunte se debe en parte a la creciente adopción de las criptomonedas en la economía global y a la creciente demanda de inversores institucionales."
        )

        # Tercer objeto
        blog_post_3 = BlogPost(
            userId=post.userId,
            title="La inteligencia artificial revoluciona la atención médica",
            subtitle="Diagnósticos más precisos y tratamiento personalizado",
            postdate="2023-10-10",
            postContent="La inteligencia artificial está cambiando la forma en que se brinda atención médica. Los algoritmos de IA pueden analizar grandes cantidades de datos médicos para realizar diagnósticos más precisos y predecir enfermedades antes de que se desarrollen. Además, la IA permite la personalización de tratamientos, lo que mejora la eficacia de los cuidados médicos. Hospitales y clínicas de todo el mundo están adoptando esta tecnología para mejorar la salud de los pacientes."
        )

        # Cuarto objeto
        blog_post_4 = BlogPost(
            userId=post.userId,
            title="El auge de la industria de los vehículos eléctricos",
            subtitle="Tesla, Rivian y otras compañías lideran el mercado",
            postdate="2023-10-05",
            postContent="La industria de los vehículos eléctricos está experimentando un crecimiento espectacular. Empresas como Tesla, Rivian y otras están liderando el mercado con sus innovadores automóviles eléctricos que ofrecen un rendimiento excepcional y cero emisiones. A medida que aumenta la conciencia sobre el cambio climático, la demanda de vehículos eléctricos sigue creciendo, y se espera que esta tendencia continúe en el futuro."
        )
        blog_post_1.save()
        blog_post_2.save()
        blog_post_3.save()
        blog_post_4.save()
    return redirect('blog/index.html', {})

def v_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            # Guardar el objeto BlogPost en la base de datos
            form.instance.userId = request.user
            form.save()
            # Redirigir a la página de detalles del blog post o a donde desees
            return redirect('index')
    else:
        form = BlogPostForm()
    return render(request, 'blog/post.html', {'form': form})    

def v_about(request):

    return render(request, 'blog/about.html', {})

def v_contact(request):

    return render(request, 'blog/contact.html', {})

def v_samplepost(request, blogpostId):
    try:
        post = BlogPost.objects.get(id=blogpostId)
    except BlogPost.DoesNotExist:
        # Maneja la excepción si el objeto no se encuentra
        post = None

    return render(request, 'blog/samplepost.html', {"data": post})
