from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Quiz, Question, Choice, Answer, Man


# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 30})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 60})}
    }


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 30})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 60})}
    }


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 70})}
    }


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'question_type')
    inlines = [
        ChoiceInline
    ]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5})}
    }

class AnswerAdmin(admin.ModelAdmin):
     list_display = ('question_id', 'txt_answer', 'user_id')

class ManAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline
    ]
    list_display = ('user_id', 'nick_name')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Man, ManAdmin)

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
      list_display = ('pk', 'quiz_title', 'quiz_specification')
      save_on_top = True
      fieldsets = [
        (None, {'fields': ['quiz_title', 'quiz_specification']}),
        ('Dates', {'fields': [('start_date', 'expiration_date'), ]}),
    ]
      inlines = [
              QuestionInline
       ]

