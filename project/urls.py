from django.urls import path
from . import views

urlpatterns=[
    # path("",views.post_it,name="post_it"),
    path("patient/<int:pk>/",views.patient,name="patient"),
    path("special/<int:id>/",views. Apispecialiser.as_view(),name="specialisation"),
    path("doctor/",views.doctor,name="doctor"),
    path("disease/",views.ApiDisserialiser.as_view()),
    path("chat/",views.ApiChatserialiser.as_view()),
    path("docspecial/",views.ApiDoc_specserialiser.as_view()),

    path("qualification/",views.ApiQualserialiser.as_view()),
    path("affiliation/",views.ApiHos_afflserialiser.as_view()),


    path("available/",views.ApiOff_availabserialiser.as_view()),
    path("appointment/",views.ApiAppserialiser.as_view()),
    path("appstatus/",views.ApiApp_statusserialiser.as_view()),

    path("transaction/",views.ApiTranserialiser.as_view()),
    path("symptom/",views.ApiSympserialiser.as_view()),


    # path("javas/<str:pk>/",views.one,name="one"),
    # path("javas/<str:pk>/deletenote",views.delete,name="delete")
    
]