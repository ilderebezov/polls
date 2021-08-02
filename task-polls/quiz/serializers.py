from rest_framework import serializers
from .models import Quiz, Question, Answer, Choice, Man


class ChoiceSerializer(serializers.ModelSerializer):
# Choise model serializer
    class Meta:
        model = Choice
        fields = ['id', 'choice_text']


class QuestionSerializer(serializers.ModelSerializer):
# Question model serializer
    class Meta:
        model = Question
        fields = '__all__'


class QuestionDetailSerializer(serializers.ModelSerializer):
    # Question Detail model serializer
    choices = ChoiceSerializer(read_only=True, many=True)
    class Meta:
        model = Question
        fields = ['text', 'type', 'choices']


class QuizSerializer(serializers.ModelSerializer):
    # Quiz model serializer
    class Meta:
        model = Quiz
        fields = '__all__'


class QuizDetailSerializer(serializers.ModelSerializer):
    # QuizDetail serializer
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ['title', 'start_date', 'expiration_date', 'quiz_specification', 'questions']


class AnswerSerializer(serializers.ModelSerializer):
    # Answer model serializer
    class Meta:
        model = Answer
        fields = ['user_id', 'question_id', 'choices_id', 'txt_answer']

class ManSerializer(serializers.ModelSerializer):
    # Man model serializer
    answers = AnswerSerializer(many=True, read_only=True, allow_null=True)

    class Meta:
        model = Man
        fields = ['user_id', 'nick_name']
