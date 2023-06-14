from django.urls import path
from students.views import (
    StudentListCreateView,
    StudentRetrieveView,
    MarkCreateView,
    MarkListView,
    StudentResultsView,
)

urlpatterns = [
    path('api/students/', StudentListCreateView.as_view(), name='student-list'),
    path('api/student/add/', StudentListCreateView.as_view(), name='student-create'),
    path('api/student/<int:pk>/', StudentRetrieveView.as_view(), name='student-detail'),
    path('api/student/<int:pk>/add-mark/', MarkCreateView.as_view(), name='mark-create'),
    path('api/student/<int:pk>/mark/', MarkListView.as_view(), name='mark-list'),
    path('api/student/results/', StudentResultsView.as_view(), name='student-results'),
]
