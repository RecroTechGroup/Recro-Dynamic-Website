"""
Context processors for RecroTech Django application.
These functions make data available globally across all templates.
Now using Django's built-in i18n system with gettext_lazy.
"""

from django.utils.translation import gettext_lazy as _


def solutions_context(request):
    """
    Context processor to make solutions data available to all templates.
    Usage in templates: {{ solutions.agri.hero_title }}

    All strings are marked for translation with _() and will be
    automatically translated based on the active language.
    """
    solutions_data = {
        'agri': {
            'hero_title': _('AI in Agriculture'),
            'page_title': _('AI in Agriculture'),
            'intro_title': _('AI in Agriculture'),
            'intro_text': _(
                "We leverage AI to support farmers and agriculture enthusiasts by providing up-to-date "
                "information on regulations and tailored solutions for the specific challenges they may face. "
                "Our intelligent systems help optimize decision-making across every aspect of farming, from "
                "crop management to resource allocation, ensuring better yields, compliance, and sustainability."
            ),
            'section_title': _('Spot-on Solutions in Agriculture'),
            'section_text': _(
                "With AI-driven insights, farmers can anticipate problems before they occur, stay informed "
                "about evolving regulations, and make smarter, data-backed decisions for their land and crops."
            ),
            'image_main': 'img/gif/tarım.gif',
            'image_side': 'img/service/tarım.png',
            'pills': [
                {
                    'key': 'pilot',
                    'title': _('Spot-on Solutions'),
                    'description': _(
                        "Create domain-specific agents capable of autonomous reasoning, planning, and interaction. "
                        "Tailored AI solutions that understand your specific agricultural challenges and provide "
                        "actionable recommendations."
                    )
                },
                {
                    'key': 'agent',
                    'title': _('Up-To-Date'),
                    'description': _(
                        "Stay current with the latest regulations, best practices, and market conditions affecting "
                        "your agricultural operations."
                    )
                },
                {
                    'key': 'modernize',
                    'title': _('Low-Cost Maintenance'),
                    'description': _(
                        "Integrate AI through lightweight APIs for instant scalability. "
                        "Efficient, cost-effective solutions that reduce overhead while maximizing sustainability."
                    )
                }
            ]
        },

        'fashion': {
            'hero_title': _('Fashion Models'),
            'page_title': _('AI Fashion Models - RecroTech'),
            'intro_title': _('AI Fashion Models'),
            'intro_text': _(
                "AI solutions are designed specifically for the fashion retail industry, helping your company "
                "boost sales and streamline operations. By leveraging advanced machine learning and computer "
                "vision, our models are fine-tuned to your company's unique needs, enabling smarter "
                "decision-making across every aspect of your business."
            ),
            'section_title': _('Adaptive Intelligence That Works for You'),
            'section_text': _(
                "Different types of GANs, image recognition, and diffusion models are integrated to provide "
                "your company with the best fashion solutions, from trend prediction to realistic "
                "visualizations and personalized styling. With retail-specific AI, your company can predict "
                "what customers want before they do, reduce waste, improve efficiency, and ultimately maximize "
                "revenue and customer satisfaction."
            ),
            'image_main': 'img/gif/fashion.gif',
            'image_side': 'img/service/fashion.png',
            'pills': [
                {
                    'key': 'pilot',
                    'title': _('Higher Sales'),
                    'description': _(
                        "Boost revenue with AI-powered trend forecasting, personalized recommendations, and "
                        "dynamic pricing. Predict customer preferences and optimize inventory to maximize "
                        "conversion rates and average order value."
                    )
                },
                {
                    'key': 'agent',
                    'title': _('Reduced Ops Cost'),
                    'description': _(
                        "Streamline end-to-end business processes with adaptive automation and minimal supervision. "
                        "Reduce waste, optimize supply chains, and automate routine tasks to cut operational "
                        "expenses significantly."
                    )
                },
                {
                    'key': 'modernize',
                    'title': _('Company Specific'),
                    'description': _(
                        "Integrate agents through lightweight APIs and open frameworks for instant scalability. "
                        "Our models are fine-tuned to your brand's unique aesthetic, customer base, and business "
                        "objectives for maximum impact."
                    )
                }
            ]
        },

        'space': {
            'hero_title': _('AI in Space'),
            'page_title': _('AI in Space - RecroTech'),
            'intro_title': _('AI in Space'),
            'intro_text': _(
                "Build and deploy autonomous AI agents that tackle real-world business challenges through "
                "open-source automation and seamless deployment. From intelligent task routing to adaptive "
                "workflows and predictive orchestration, our systems integrate directly with your stack, "
                "accelerating outcomes and reducing manual overhead."
            ),
            'section_title': _('Adaptive Intelligence That Works for You'),
            'section_text': _(
                "Our AI agents continuously learn from interactions and data, improving performance over time. "
                "They automate repetitive operations, detect anomalies, and respond to complex signals — "
                "allowing teams to focus on strategic decisions while the system handles precision execution."
            ),
            'image_main': 'img/gif/uzay.gif',
            'image_side': 'img/service/uzay.png',
            'pills': [
                {
                    'key': 'pilot',
                    'title': _('Design an AI Agent'),
                    'description': _(
                        "Create domain-specific agents capable of autonomous reasoning, planning, and interaction. "
                        "Tailor AI systems to your unique requirements with advanced customization and training capabilities."
                    )
                },
                {
                    'key': 'agent',
                    'title': _('Automate Workflows'),
                    'description': _(
                        "Streamline end-to-end business processes with adaptive automation and minimal supervision. "
                        "Reduce manual tasks, improve efficiency, and enable teams to focus on high-value activities."
                    )
                },
                {
                    'key': 'modernize',
                    'title': _('Deploy Effortlessly'),
                    'description': _(
                        "Integrate agents through lightweight APIs and open frameworks for instant scalability. "
                        "Deploy to production quickly with robust monitoring, version control, and rollback capabilities."
                    )
                }
            ]
        }
    }

    return {'solutions': solutions_data}


def services_context(request):
    """
    Context processor to make services data available to all templates.
    Usage in templates: {{ services.aiagent.hero_title }}

    All strings are marked for translation with _() and will be
    automatically translated based on the active language.
    """
    services_data = {
        'aiagent': {
            'hero_title': _('AI Agents and Automations'),
            'page_title': _('AI Agents and Automations'),
            'intro_title': _('AI Agents and Automations'),
            'intro_text': _(
                "Build and deploy autonomous AI agents that tackle real-world business challenges through "
                "open-source automation and seamless deployment. From intelligent task routing to adaptive "
                "workflows and predictive orchestration, our systems integrate directly with your stack, "
                "accelerating outcomes and reducing manual overhead."
            ),
            'section_title': _('Adaptive Intelligence That Works for You'),
            'section_text': _(
                "Our AI agents continuously learn from interactions and data, improving performance over time. "
                "They automate repetitive operations, detect anomalies, and respond to complex signals — allowing "
                "teams to focus on strategic decisions while the system handles precision execution."
            ),
            'image_main': 'img/gif/agentt.gif',
            'image_side': 'img/service/agentt.png',
            'pills': [
                {
                    'key': 'pilot',
                    'title': _('Design an AI Agent'),
                    'description': _("Create domain-specific agents capable of autonomous reasoning, planning, and interaction.")
                },
                {
                    'key': 'agent',
                    'title': _('Automate Workflows'),
                    'description': _("Streamline end-to-end business processes with adaptive automation and minimal supervision.")
                },
                {
                    'key': 'modernize',
                    'title': _('Deploy Effortlessly'),
                    'description': _("Integrate agents through lightweight APIs and open frameworks for instant scalability.")
                }
            ]
        },

        'awide': {
            'hero_title': _('A Wide Variety of AI Solutions'),
            'page_title': _('A Wide Variety of AI Solutions'),
            'intro_title': _('Industry-Ready AI Across Finance, Public Sector, Law & More'),
            'intro_text': _(
                "We build and deploy industry-ready AI across finance, public sector, law, energy, manufacturing, "
                "and retail. Our solutions turn complex data into decisions by automating reviews, flagging risks, "
                "forecasting demand, and personalizing experiences. From LLMs to forecasting, anomaly detection, "
                "and optimization—we ship secure APIs and agents that integrate with your stack, monitor themselves, "
                "and prove value with live KPIs from day one."
            ),
            'section_title': _('Cutting-Edge Technologies That Deliver Results'),
            'section_text': _(
                "Technology evolves daily—we convert it into measurable results. Faster launches, lower risk, "
                "and proven ROI across software, hardware, communications, and automation. Our cross-industry "
                "expertise ensures you stay ahead with solutions built for scale and performance."
            ),
            'image_main': 'img/gif/awidegif.gif',
            'image_side': 'img/service/awidegorsel.png',
            'pills': [
                {
                    'key': 'pilot',
                    'title': _('Start a Pilot'),
                    'description': _(
                        "Launch a controlled pilot to validate AI impact in your specific workflow. We deploy a "
                        "scoped solution, measure real KPIs, and iterate based on your feedback—proving value "
                        "before full-scale rollout."
                    )
                },
                {
                    'key': 'agent',
                    'title': _('Add an AI Agent'),
                    'description': _(
                        "Deploy autonomous AI agents that handle repetitive tasks, respond to queries, and make "
                        "decisions within defined parameters. Integrate seamlessly with your existing systems for "
                        "24/7 intelligent automation."
                    )
                },
                {
                    'key': 'modernize',
                    'title': _('Modernize the Stack'),
                    'description': _(
                        "Upgrade legacy systems with cloud-native architecture, microservices, and modern DevOps "
                        "practices. Reduce technical debt while maintaining business continuity and improving "
                        "deployment velocity by 10x."
                    )
                },
                {
                    'key': 'kpis',
                    'title': _('See Live KPIs'),
                    'description': _(
                        "Access real-time dashboards displaying business-critical metrics: model accuracy, "
                        "processing speed, cost per transaction, user satisfaction, and ROI. Make data-driven "
                        "decisions with live visibility into AI performance."
                    )
                }
            ]
        },

        'cloud': {
            'hero_title': _('Cloud Services'),
            'page_title': _('Cloud Services'),
            'intro_title': _('Cloud Services'),
            'intro_text': _(
                "We design and deploy cloud-native systems that transform ideas into scalable, high-performance "
                "applications. Our expertise in distributed computing, data orchestration, and infrastructure "
                "automation ensures reliability, speed, and seamless integration across any environment."
            ),
            'section_title': _('Infrastructure That Scales with You'),
            'section_text': _(
                "Our cloud architectures grow with your business — from prototypes to global-scale platforms. "
                "Through automated scaling, containerized deployment, and continuous monitoring, we build "
                "resilient systems that adapt to demand in real time."
            ),
            'image_main': 'img/gif/cloud.gif',
            'image_side': 'img/service/clouds.png',
            'pills': [
                {
                    'key': 'pilot',
                    'title': _('Build on the Cloud'),
                    'description': _(
                        "Develop and deploy applications on secure, global-grade cloud infrastructure with "
                        "high availability and performance optimization."
                    )
                },
                {
                    'key': 'agent',
                    'title': _('Automate Infrastructure'),
                    'description': _(
                        "Use Infrastructure as Code (IaC) and DevOps pipelines to manage cloud environments "
                        "efficiently with version control and automation."
                    )
                },
                {
                    'key': 'modernize',
                    'title': _('Scale Seamlessly'),
                    'description': _(
                        "Enable dynamic scaling and resource optimization based on real-time workloads, "
                        "ensuring cost-efficiency and peak performance."
                    )
                }
            ]
        },

        'crm': {
            'hero_title': _('CRM Solutions'),
            'page_title': _('CRM Solutions'),
            'intro_title': _('CRM Solutions'),
            'intro_text': _(
                "We build intelligent CRM systems that unify data, automate engagement, and surface actionable "
                "insights across sales, support, and marketing. By combining AI-driven analytics with custom "
                "workflows, our CRM solutions help teams anticipate customer needs and strengthen long-term "
                "relationships."
            ),
            'section_title': _('Turning Data into Customer Intelligence'),
            'section_text': _(
                "From lead scoring to retention analytics, our CRM platforms turn customer behavior into "
                "measurable intelligence. Each interaction becomes a feedback loop that sharpens predictions, "
                "improves personalization, and drives sustainable growth."
            ),
            'image_main': 'img/gif/crm.gif',
            'image_side': 'img/service/crmm.png',
            'pills': [
                {
                    'key': 'pilot',
                    'title': _('Centralize Data'),
                    'description': _(
                        "Unify customer data from multiple touchpoints into a single source of truth. Eliminate "
                        "data silos and gain a 360-degree view of every customer interaction."
                    )
                },
                {
                    'key': 'agent',
                    'title': _('Automate Engagement'),
                    'description': _(
                        "Deploy intelligent workflows that trigger personalized communications, follow-ups, and "
                        "nurture sequences based on customer behavior and lifecycle stage."
                    )
                },
                {
                    'key': 'modernize',
                    'title': _('Analyze Behavior'),
                    'description': _(
                        "Leverage AI-powered analytics to identify patterns, predict churn, score leads, and "
                        "uncover opportunities for cross-sell and upsell across your customer base."
                    )
                }
            ]
        },

        'tech': {
            'hero_title': _('Tech Enthusiasts'),
            'page_title': _('Tech Enthusiasts'),
            'intro_title': _('Tech Enthusiasts'),
            'intro_text': _(
                "We run hands-on labs, meetups, and open-source sprints where builders prototype fast, share "
                "knowledge, and ship. From weekend workshops to deep-dive clinics, we turn curiosity into "
                "working artifacts and community momentum."
            ),
            'section_title': _('Learn. Build. Share. Repeat.'),
            'section_text': _(
                "Sessions focus on real tools, real data, and repeatable patterns. You leave with code, docs, "
                "and a path to production—plus a network that keeps the pace."
            ),
            'image_main': 'img/gif/tech.gif',
            'image_side': 'img/service/techh.png',
            'pills': [
                {
                    'key': 'pilot',
                    'title': _('Hands-On Labs'),
                    'description': _(
                        "Guided builds with step-by-step briefs, from idea to working demo in hours. Learn by "
                        "doing with real-world scenarios and production-ready code."
                    )
                },
                {
                    'key': 'agent',
                    'title': _('Open-Source Sprints'),
                    'description': _(
                        "Ship PRs together—issues, reviews, and merges with maintainers. Contribute to meaningful "
                        "open-source projects and build your portfolio."
                    )
                },
                {
                    'key': 'modernize',
                    'title': _('Prototyping Clinics'),
                    'description': _(
                        "Rapid design-to-code cycles, usability checks, and tech spikes. Validate ideas quickly "
                        "and iterate based on real user feedback."
                    )
                }
            ]
        },

        'train': {
            'hero_title': _('Trainings'),
            'page_title': _('AI & Cloud Trainings'),
            'intro_title': _('Trainings'),
            'intro_text': _(
                "We deliver hands-on, outcome-driven trainings that turn teams into effective AI and cloud "
                "practitioners. Programs combine fundamentals, real datasets, and production patterns—so "
                "learners can build, deploy, and operate reliable systems."
            ),
            'section_title': _('From Fundamentals to Production'),
            'section_text': _(
                "Courses progress from core concepts to deployment, monitoring, and cost control. Each module "
                "ends with a working artifact—model, pipeline, or service—ready to integrate."
            ),
            'image_main': 'img/gif/trainnew.gif',
            'image_side': 'img/service/trainnew.png',
            'pills': [
                {
                    'key': 'pilot',
                    'title': _('AI Foundations'),
                    'description': _(
                        "Math, data prep, model selection, evaluation; practical notebooks with real datasets. "
                        "Build a strong foundation in machine learning fundamentals."
                    )
                },
                {
                    'key': 'agent',
                    'title': _('LLMs & Agents'),
                    'description': _(
                        "Prompting, retrieval, tool-use, agent orchestration; safety, evals, and guardrails. "
                        "Master modern LLM applications and autonomous agents."
                    )
                },
                {
                    'key': 'modernize',
                    'title': _('MLOps & Pipelines'),
                    'description': _(
                        "Versioning, CI/CD for ML, feature stores, monitoring, drift and rollback patterns. "
                        "Deploy and maintain production ML systems reliably."
                    )
                }
            ]
        }
    }

    return {'services': services_data}


def site_info_context(request):
    """
    Context processor for global site information.
    Usage in templates: {{ site.company_name }}

    Only the tagline and address are translatable.
    Company name, contact details, and URLs remain the same across languages.
    """
    site_data = {
        'company_name': 'RecroTech',
        'tagline': _('We revive technology for the good of humanity'),
        'email': 'info@recrotechgroup.com',
        'phone': '+90 312 803 78 37',
        'phone2': '+90 537 323 00 81',
        'address': _('Mustafa Kemal Mahallesi, Barış Sitesi, 2092 Sokak, No:22, Çankaya/ANKARA'),
        'social': {
            'youtube': 'https://www.youtube.com/channel/UCu-9E68CfoKosVQMxCtK3wA',
            'twitter': 'https://x.com/RecroTech',
            'linkedin': 'https://www.linkedin.com/company/recrotech',
            'instagram': 'https://www.instagram.com/recrotech/',
            'spotify': 'https://open.spotify.com/show/03cjFsiKrU2UCv8gMbIuoZ'
        }
    }

    return {'site': site_data}