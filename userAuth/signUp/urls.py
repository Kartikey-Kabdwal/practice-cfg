from django.urls import include, path
from django.contrib import admin
from .views import classroom, students, teachers
from .views.classroom import home

handler404 = 'signUp.views.classroom.handler404'

urlpatterns = [
    path('', home,name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('discussion/', classroom.DiscussionView, name='discussion'),
    path('chat/room/<str:room>/', classroom.room, name='room'),
    path('chat/checkview', classroom.checkview, name='checkview'),
    path('chat/send/', classroom.send, name='send'),
    path('getMessages/<str:room>/', classroom.getMessages, name='getMessages'),

    path('students/', include(([
        path('', students.QuizListView.as_view(), name='quiz_list'),
        path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),

        path('<int:pk>/', students.quiz_view, name='quiz-view'),
        path('<int:pk>/save/', students.save_quiz_view, name='save_view,'),
        path('<int:pk>/data/', students.quiz_data_view, name='quiz_data_view,'),

    ], 'signUp'), namespace='students')),

    path('teachers/', include(([
        path('', teachers.QuizListView.as_view(), name='quiz_change_list'),
        path('quiz/add/', teachers.QuizCreateView.as_view(), name='quiz_add'),

        path('quiz/glist/', teachers.Global_list, name='glist'),
        path('quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='quiz_delete'),

        path('quiz/<int:pk>/results/', teachers.QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/stats/', teachers.QuizStatsView.as_view(), name='quiz_stats'),

        # path('quiz/<int:pk>/about/', teachers.about_percentile, name='quiz_about'),

        path('quiz/<int:pk>/question/add/', teachers.question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', teachers.question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', teachers.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'signUp'), namespace='teachers')),
]
