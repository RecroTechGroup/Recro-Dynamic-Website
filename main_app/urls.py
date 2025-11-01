"""
URL Configuration for RecroTech Pages App
All URLs use dynamic routing with single templates.
"""

from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    # ==================== ANA SAYFALAR (MAIN PAGES) ====================
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('docs/', views.docs_view, name='docs'),
    path('faq/', views.faq_view, name='faq'),
    path('isp/', views.isp_view, name='isp'),

    # ==================== ÇÖZÜMLER (SOLUTIONS) ====================
    path('solutions/', views.solutions_view, name='solutions'),
    # Dinamik solution details - Tek template kullanır (solution_details.html)
    # Örnek: /solutions/agri/, /solutions/fashion/, /solutions/space/
    path('solutions/<str:solution_type>/', views.solution_details_view, name='solution_details'),

    # ==================== HİZMETLER (SERVICES) ====================
    path('services/', views.services_view, name='services'),
    # Dinamik service details - Tek template kullanır (service_details.html)
    # Örnek: /services/aiagent/, /services/awide/, /services/train/
    path('services/<str:service_type>/', views.service_details_view, name='service_details'),

    # ==================== EĞİTİMLER (TRAININGS) ====================
    path('trainings/', views.trainings_view, name='trainings'),

    # ==================== HABERLER (NEWS) ====================
    path('news/', views.news_view, name='news'),
    path('news/<int:news_id>/', views.news_details_view, name='news_details'),

    # ==================== ÜRÜNLER (PRODUCTS) ====================
    path('products/', views.products_view, name='products'),

    # ==================== PROJELER (PROJECTS) ====================
    path('projects/', views.projects_view, name='projects'),
    path('projects/<int:project_id>/', views.project_details_view, name='project_details'),

    # ==================== TAKIM (TEAM) ====================
    path('team/', views.team_view, name='team'),
    path('team/<int:member_id>/', views.team_details_view, name='team_details'),

    # ==================== FOOTER PAGES ====================
    path('information-security-policy/', views.isp_view, name='information_security_policy'),
    path('documents/', views.docs_view, name='documents'),
]

# ==================== NOT: ESKİ URL YAPISI ====================
# Eski yapıda her service için ayrı template ve URL vardı:
#   - /services/service-details-awide/  ❌
#   - /services/service-details-train/  ❌
# 
# Yeni yapıda tek bir dinamik URL kullanıyoruz:
#   - /services/awide/  ✅
#   - /services/train/  ✅
#
# Eğer eski URL'lere geri dönük uyumluluk gerekirse, 
# aşağıdaki yönlendirmeleri ekleyebilirsiniz:
#
# from django.views.generic import RedirectView
# path('services/service-details-<str:service_type>/', 
#      RedirectView.as_view(pattern_name='pages:service_details', permanent=True)),