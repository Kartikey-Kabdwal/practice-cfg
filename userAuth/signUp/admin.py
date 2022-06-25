from django.contrib import admin
from .models import User,Subject,Question,Quiz,Answer,Student,TakenQuiz,StudentAnswer
from .models import Room,Message

class RoomAdmin(admin.ModelAdmin):
    list_display=['id','name']

class MessageAdmin(admin.ModelAdmin):
    list_display=['id','value','date','user','room']

admin.site.register(Room,RoomAdmin)
admin.site.register(Message,MessageAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display=['name','color']

class AnswerInline(admin.TabularInline):
    model=Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines=[AnswerInline]

admin.site.register(Subject,SubjectAdmin)
admin.site.register(User)

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Quiz)


admin.site.register(Student)
admin.site.register(TakenQuiz)
admin.site.register(StudentAnswer)
