from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,Login,SignupPage
from django.contrib.auth.views import LogoutView
urlpatterns=[
    #path("",views.tasklist,name='tasks'),
    path("signup/",SignupPage.as_view(),name="Signup"),
    path("",TaskList.as_view(),name="tasks"),
    path("login/",Login.as_view(),name="login"),
    path("logout/",LogoutView.as_view(next_page='login'),name="logout"),
    path("task/<int:pk>/",TaskDetail.as_view(),name="detail"),
    path("createtask/",TaskCreate.as_view(),name="createtasks"),
    path("updatetask/<int:pk>/",TaskUpdate.as_view(),name="taskupdate"),
    path("deletetask/<int:pk>/",TaskDelete.as_view(),name="taskdelete"),
]