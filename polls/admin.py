"""
Registering Question modification to admin
"""
from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    """
        3 sets of choices by default
    """
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """
        Coustmising the look of fields
    """
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
