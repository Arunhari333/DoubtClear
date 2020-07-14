from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.StuddentQuestionViewSet.as_view(), name='student_question'),
    path('teacher/', views.TeacherQuestionViewSet.as_view(), name='teacher_question'),
]
