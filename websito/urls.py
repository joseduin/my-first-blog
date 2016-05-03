"""websito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    # Esto significa que para cada URL que empieza con admin/ Django encontrar�
    # su correspondiente view. En este caso estamos incluyendo en una sola l�nea
    # muchas URLs de admin, as� no est� todo comprimido en este peque�o archivo
    # es m�s limpio y legible.
    
        # ^ denota el principio del texto
        # $ denota el final del texto
        # \d representa un d�gito
        # + indica que el �tem anterior deber�a ser repetido por lo menos una vez
        # () para encerrar una parte del patr�n

            # EJEMPLO: http://www.mysite.com/post/12345/
                
            #   ^post/(\d+)/$
                            
            # ^post/ le est� diciendo a Django que tome cualquier cosa que tenga post/ al principio
            # del URL (justo antes de ^)
            # (\d+) significa que habr� un n�mero (de uno o m�s d�gitos) y que queremos que ese n�mero
            # sea capturado y extra�do
            # / le dice a Django que otro caracter / deber�a venir a continuaci�n
            # $ indica el final del URL, lo que significa que s�lo cadenas finalizando con / coincidir�n
            # con este patr�n

]

