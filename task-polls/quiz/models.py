from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Quiz(models.Model):
# models for Quiz
    quiz_title = models.CharField(max_length=200)
    quiz_specification = models.TextField(blank=True)
    start_date = models.DateField()
    expiration_date = models.DateField()

    def __str__(self):
        return self.quiz_title

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    def clean(self):
        # Test dates
        super().clean()
        if self.start_date > self.expiration_date:
            raise ValidationError(
                    'End date cant be early the end date'
                )

ANSWER_TYPES = [('TEXT', 'Free text'), ('SINGLE', 'Single choice'), ('MULTI', 'Multiple choices')]


class Question(models.Model):
# models for Question
    question_text = models.TextField('question text', max_length=8192)
    question_type = models.CharField(max_length=6, choices=ANSWER_TYPES)
    quiz_id = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question_text


class Choice(models.Model):
# models for Choice
    question_id = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=1000)
    lock_other = models.BooleanField(default=True)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"

class Answer(models.Model):
# models for Answer
    user_id = models.ForeignKey('Man', related_name='answers', on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    choices_id = models.ManyToManyField(Choice, blank=True, related_name='answers')
    txt_answer = models.TextField(blank=True)


class Man(models.Model):
# models for Man
    user_id = models.IntegerField(primary_key=True, unique=True)
    nick_name = models.CharField(max_length=30, null=True)