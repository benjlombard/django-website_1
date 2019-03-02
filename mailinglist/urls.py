from django.urls import path, re_path

from mailinglist import views

app_name = 'mailinglist'

urlpatterns = [
  re_path('', views.MailingListListView.as_view(), name='mailinglist_list'),
    re_path('new',views.CreateMailingListView.as_view(),name='create_mailinglist'),
re_path('<uuid:pk>/delete',views.DeleteMailingListView.as_view(),name='delete_mailinglist'),
re_path('<uuid:pk>/manage',views.MailingListDetailView.as_view(),name='manage_mailinglist'),
              ]
