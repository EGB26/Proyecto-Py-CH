from django.urls import path
from AppCoder import views
#from AppCoder.views import login_request
from django.contrib.auth.views import LogoutView
#from AppCoder import curso
#views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    #path('cursoFormulario', views.cursoFormulario, name="cursoFormulario"),
    path('busquedaCamada', views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
    path('leerProfesores', views.leerProfesores, name="LeerProfesores"),
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),
    
    path('curso/list', views.CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
]

"""
Es una expresión regular, que se compara con la URL real.
Aquí r'' especifica que la cadena es una cadena sin procesar. 
'^' significa el comienzo y $ marca el final.
Ahora 'pk' (cuando está dentro de <>) representa una clave principal. 
Una clave principal puede ser cualquier cosa, por ejemplo. puede ser una 
cadena, un número, etc. Una clave principal se usa para diferenciar 
diferentes columnas de una tabla.
"""