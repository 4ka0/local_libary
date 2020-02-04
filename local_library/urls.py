"""local_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from django.urls import include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView


'''
The second item below includes a path() that forwards requests with 
the pattern catalog/ to the module catalog.urls (the file with the 
relative URL catalog/urls.py).

The third item redirects the root url of the site '127.0.0.1:8000'
to the URL '127.0.0.1:8000/catalog/' since the catalog app is the only
app in this project.

The final '+ static ...' line enables the serving of static files during 
development such as CSS, JavaScript, and images (this is ordinarily disabled 
by default).
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
