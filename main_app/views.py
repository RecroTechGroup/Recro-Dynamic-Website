"""
Views for RecroTech Django application.
Handles all page rendering and routing logic.
Uses context processors for dynamic data (solutions, services, site info).
"""

from django.shortcuts import render
from django.http import Http404


# ==================== ANA SAYFALAR ====================

def home_view(request):
    """Ana sayfa - Home page"""
    return render(request, 'pages/index.html')


def about_view(request):
    """Hakkımızda sayfası - About page"""
    return render(request, 'pages/about.html')


def contact_view(request):
    """İletişim sayfası - Contact page"""
    return render(request, 'pages/contact.html')


def docs_view(request):
    """Dökümantasyon sayfası - Documents page"""
    return render(request, 'pages/docs.html')


def faq_view(request):
    """Sık Sorulan Sorular - FAQ page"""
    return render(request, 'pages/faq.html')


def isp_view(request):
    """Bilgi Güvenliği Politikası - Information Security Policy page"""
    return render(request, 'pages/isp.html')


# ==================== ÇÖZÜMLER (SOLUTIONS) ====================

def solutions_view(request):
    """
    Çözümler ana sayfası - Solutions listing page
    Uses solutions_context from context processor
    """
    return render(request, 'pages/solutions.html')


def solution_details_view(request, solution_type):
    """
    Dinamik çözüm detay sayfası - Dynamic solution details page

    Args:
        solution_type: Çözüm tipi slug (agri, fashion, space)

    Template: pages/solution_details.html (single template for all solutions)
    Context: solution, solution_type, prev_solution, next_solution
    """
    # Import context processor to get solutions data
    from main_app.contexts import solutions_context
    solutions_data = solutions_context(request)['solutions']

    # Validate solution exists
    if solution_type not in solutions_data:
        raise Http404("Solution not found")

    # Get current solution data
    solution = solutions_data[solution_type]

    # Navigation: Previous and Next solutions
    solutions_order = list(solutions_data.keys())  # ['agri', 'fashion', 'space']
    current_index = solutions_order.index(solution_type)

    prev_solution = solutions_order[current_index - 1] if current_index > 0 else None
    next_solution = solutions_order[current_index + 1] if current_index < len(solutions_order) - 1 else None

    context = {
        'solution': solution,
        'solution_type': solution_type,
        'prev_solution': prev_solution,
        'next_solution': next_solution,
    }

    return render(request, 'pages/solution_details.html', context)


# ==================== HİZMETLER (SERVICES) ====================

def services_view(request):
    """
    Hizmetler ana sayfası - Services listing page
    Uses services_context from context processor
    """
    return render(request, 'pages/service.html')


def service_details_view(request, service_type):
    """
    Dinamik hizmet detay sayfası - Dynamic service details page

    Args:
        service_type: Hizmet tipi slug (aiagent, awide, cloud, crm, tech, train)

    Template: pages/service_details.html (single template for all services)
    Context: service, service_type, prev_service, next_service
    """
    # Import context processor to get services data
    from main_app.contexts import services_context
    services_data = services_context(request)['services']  # ✅ services_data olarak aldık

    # Validate service exists
    if service_type not in services_data:
        raise Http404("Service not found")

    # Get current service data
    service = services_data[service_type]  # ✅ services_data kullanıyoruz

    # Navigation: Previous and Next services
    services_order = list(services_data.keys())  # ✅ services_data.keys()
    current_index = services_order.index(service_type)

    prev_service = services_order[current_index - 1] if current_index > 0 else None
    next_service = services_order[current_index + 1] if current_index < len(services_order) - 1 else None

    context = {
        'service': service,
        'service_type': service_type,
        'prev_service': prev_service,
        'next_service': next_service,
    }

    return render(request, 'pages/service_details.html', context)


# ==================== EĞİTİMLER (TRAININGS) ====================

def trainings_view(request):
    """Eğitimler ana sayfası - Trainings page"""
    return render(request, 'pages/trainings.html')


# ==================== HABERLER (NEWS) ====================

def news_view(request):
    """Haberler listesi - News listing page"""
    return render(request, 'pages/news.html')


def news_details_view(request, news_id):
    """
    Dinamik haber detay sayfası - Dynamic news details page

    Args:
        news_id: Haber ID'si

    Note: Gerçek projede database'den çekilecek
    """
    context = {
        'news_id': news_id,
        # Future: 'news': get_object_or_404(News, id=news_id)
    }
    return render(request, 'pages/news-details.html', context)


# ==================== ÜRÜNLER (PRODUCTS) ====================

def products_view(request):
    """Ürünler listesi - Products listing page"""
    return render(request, 'pages/products.html')


# ==================== PROJELER (PROJECTS) ====================

def projects_view(request):
    """Projeler listesi - Projects listing page"""
    return render(request, 'pages/project.html')


def project_details_view(request, project_id):
    """
    Dinamik proje detay sayfası - Dynamic project details page

    Args:
        project_id: Proje ID'si

    Note: Gerçek projede database'den çekilecek
    """
    context = {
        'project_id': project_id,
        # Future: 'project': get_object_or_404(Project, id=project_id)
    }
    return render(request, 'pages/project-details.html', context)


# ==================== TAKIM (TEAM) ====================

def team_view(request):
    """Takım sayfası - Team page"""
    return render(request, 'pages/team.html')


def team_details_view(request, member_id):
    """
    Dinamik takım üyesi detay sayfası - Dynamic team member details page

    Args:
        member_id: Takım üyesi ID'si

    Note: Gerçek projede database'den çekilecek
    """
    context = {
        'member_id': member_id,
        # Future: 'member': get_object_or_404(TeamMember, id=member_id)
    }
    return render(request, 'pages/team-details.html', context)


# ==================== ESKİ YAPIDA KULLANILAN VIEWS (DEPRECATED) ====================
# Bu fonksiyonlar eski template sistemi için kullanılıyordu.
# Yeni yapıda solution_details_view() ve service_details_view() kullanılıyor.

def solutions_agri_view(request):
    """
    DEPRECATED: Eski tarım çözümleri sayfası
    Yeni yapıda: solution_details_view(request, 'agri')
    """
    return render(request, 'pages/solutions-agri.html')


def solutions_fashion_view(request):
    """
    DEPRECATED: Eski moda çözümleri sayfası
    Yeni yapıda: solution_details_view(request, 'fashion')
    """
    return render(request, 'pages/solutions-fashion.html')


def solutions_space_view(request):
    """
    DEPRECATED: Eski uzay çözümleri sayfası
    Yeni yapıda: solution_details_view(request, 'space')
    """
    return render(request, 'pages/solutions-space.html')