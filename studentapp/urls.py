from django.urls import path
from .views import*

urlpatterns = [
    path('home/', home_view),
    path('about/', about_view),
    path('login/', login_view),
    path('signup/', signup_view),
    # path('orm/' , orm_practice),
    path('emps/' , display_employee),
    path('sign/',sign_view),
    path('adddep/',add_dep),
    path('addteam/',add_team),
    path('addemp/',add_emp),
    path('delete/',del_view),
    path('details/',more_details_view),
]
