from django.contrib import admin
from .models import Question, Choice

class ChoiceAdmin(admin.TabularInline):
    model = Choice
    #exclude = ('votes',)
    readonly_fields = ['votes']
    min_num = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently') # To view also date on list of questions
    list_filter = ['pub_date'] # Create a filter box on list
    search_fields = ['question_text']

    #readonly_fields = ["pub_date"]
    fields = ["pub_date", "question_text"] # To order the fields inside, use this
    inlines = [ChoiceAdmin]

admin.site.register(Question, QuestionAdmin)

