from django.urls import path
from utility import views


urlpatterns = [
    # Utility
    path('utility/starter-page/',views.StarterPageView.as_view(),name='pages-starter'),# Starter Pages
    path('utility/maintenance',views.MaintenanceView.as_view(),name='pages-maintenance'),# Maintenance
    path('utility/coming-soon',views.ComingSoonView.as_view(),name='pages-comingsoon'),# Maintenance
    path('utility/timeline',views.TimelineView.as_view(),name='pages-timeline'),# Timeline
    path('utility/faqs',views.FaqsView.as_view(),name='pages-faqs'),# Faqs
    path('utility/pricing',views.PricingView.as_view(),name='pages-pricing'),# Pricing
    path('utility/error-404',views.Error404View.as_view(),name='pages-404'),# Error 404 
    path('utility/error-500',views.Error500View.as_view(),name='pages-500'),# Error 404

    path('utility/starter-page-test',views.TestView.as_view(),name='pages-starter-test'),
    path('utility/starter-page-test/jump',views.jump_bars,name='jump'),

    # visual_data
    path('utility/simulation', views.SimulationView.as_view(),name='simulation'),
    path('utility/results',views.result_page,name='results'),
    path('utility/results/finish_time',views.jump_bars,name='finish_time'),
    path('utility/results/compare_results',views.compare_bars,name='compare_results'),
    path('utility/results/waiting_time',views.wait_bars,name='waiting_time'),
    path('utility/results/analysis_time',views.analysis_bars_time,name='analysis_time'),
    path('utility/results/analysis_wait',views.analysis_bars_wait,name='analysis_wait'),
    # path('utility/results/collision',views.line_collision,name='collision'),
    path('utility/results/pie_wait', views.pie_wait,name='pie_wait'),
    path('utility/pie/', views.ChartView.as_view(), name='pie'),
    path('utility/bar/', views.ChartView_2.as_view(), name='bar'),
    path('utility/text/', views.TextView.as_view(), name='text'),
    path('utility/task/', views.TaskView.as_view(), name='task'),
    path('utility/loc/', views.LocView.as_view(), name='loc'),
    path('utility/waitnum/', views.WaitNumView.as_view(), name='wait-num'),
    path('utility/move/', views.MoveView.as_view(), name='move'),
    path('utility/map/', views.MapView.as_view(), name='map'),
    path('utility/process/', views.ProcessView.as_view(), name='process'),
    path('utility/starter-page/wait', views.bar_wait_simultaneous,name='wait'),
    path('utility/starter-page/pie_wait',views.pie_wait_2,name='pie_wait_2'),
    ]
