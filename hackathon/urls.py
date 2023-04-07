from django.urls import path
from .views import Hackathons,register,Enrolled,submission,Home,RegisterView,getSubmission
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("",Home.as_view()),
    #authentication
    path("register",RegisterView.as_view()),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    #endpoints
    path("hackathons", Hackathons.as_view()),
    path("enroll/<int:pk>",register.as_view()),
    path("enrolled",Enrolled.as_view()),
    path("getsubmission",getSubmission.as_view()) ,
    path("submission/<int:pk>",submission.as_view()) ,
    
    
]