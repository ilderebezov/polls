import datetime
from django.utils.timezone import get_default_timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status, viewsets, generics
from .models import Quiz, Question, Choice, Answer, Man
from . import serializers


# Access
class AdminOrNo(permissions.BasePermission):
    # Access for admin to edit
    def get_access(self, message, view):
        if message.method in permissions.SAFE_METHODS:
            return True
        return message.user.is_superuser


class AdminOrPost(permissions.BasePermission):
    # Access for admin to edit
    def get_access(self, message, view):
        if message.method == 'POST':
            return True
        return message.user.is_superuser


class QuizViewSet(viewsets.ModelViewSet):
    # model view for Quiz

    queryset = Quiz.objects.all()
    quiz_serializer_class = serializers.QuizSerializer
    quiz_detail_serializer_class = serializers.QuizDetailSerializer
    permission_classes = [AdminOrNo]

    def quiz_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'quiz_detail_serializer_class'):
                return self.quiz_detail_serializer_class
        return super().quiz_serializer_class()

    def get_quiz_queryset(self):
        queryset = Quiz.objects.all()
        now = datetime.datetime.now(tz=None).replace(tzinfo=get_default_timezone())
        return queryset.filter(start_date__lte=now, expiration_date__gt=now)

class QuestionViewSet(viewsets.ModelViewSet):
    # model view for Question

    queryset = Question.objects.all()
    queistion_serializer_class = serializers.QuestionSerializer
    question_detail_serializer_class = serializers.QuestionDetailSerializer
    permission_classes = [AdminOrNo]

    def get_question_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'question_detail_serializer_class'):
                return self.question_detail_serializer_class
        return super().get_question_serializer_class()

    def get_question_queryset(self):
        return Question.objects.filter(Quiz=self.kwargs['Quiz_id'])

class ChoicesViewSet(viewsets.ModelViewSet):
    # model view for Choices
    queryset = Choice.objects.all()
    choice_serializer_class = serializers.ChoiceSerializer
    permission_classes = [AdminOrNo]

    def get_choise_queryset(self):
        return Choice.objects.filter(question=self.kwargs['question_id'])


class AnswerViewSet(viewsets.ModelViewSet):
# model view for Answer
    queryset = Answer.objects.all()
    answer_serializer_class = serializers.AnswerSerializer
    permission_classes = [AdminOrPost]

    def perform_answer_create(self, answer_serializer):
        answer_serializer.is_valid()
        answer_serializer.save()

    def get_answer_queryset(self):
         return Answer.objects.filter(question=self.kwargs['question_id'])

class UserListView(APIView):
    # model view for all man in all Quizzes

    def get_UserListView(self, request):
        queryset = Man.objects.all()
        UserListView_serializer = serializers.ManSerializer(queryset, many=True)
        return Response(UserListView_serializer.data, status=status.HTTP_200_OK)


class UserView(APIView):
    # model view for all answer for the man

    def get_UserView(self, request_UserView, user_id):
        queryset = Man.objects.filter(user_id=user_id)
        if queryset.count() < 1:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer_UserView = serializers.ManSerializer(queryset.last())
        return Response(serializer_UserView.data)