from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'Quiz', views.QuizViewSet)
router.register(r'Quiz/(?P<Quiz_id>[0-9]+)/question', views.QuestionViewSet)
router.register(r'Quiz/(?P<Quiz_id>[0-9]+)/question/(?P<question_id>[0-9]+)/choice', views.ChoicesViewSet)
router.register(r'Quiz/(?P<Quiz_id>[0-9]+)/question/(?P<question_id>[0-9]+)/answer', views.AnswerViewSet)

app_name = "Quizs"

urlpatterns = [
    path('api/', include(router.urls)),
    re_path(r'api/user/(?P<user_id>[0-9]+)', views.UserView.as_view()),
    re_path(r'api/user', views.UserListView.as_view()),
]