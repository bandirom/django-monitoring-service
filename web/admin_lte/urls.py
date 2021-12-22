from django.urls import path
from rest_framework.routers import DefaultRouter

from main.views import TemplateAPIView

app_name = 'admin_lte'

router = DefaultRouter()

urlpatterns = [
    path('index/', TemplateAPIView.as_view(template_name='admin_lte/index.html'), name='index'),
    path('index2/', TemplateAPIView.as_view(template_name='admin_lte/index2.html'), name='index2'),
    path('index3/', TemplateAPIView.as_view(template_name='admin_lte/index3.html'), name='index3'),
    path('widgets/', TemplateAPIView.as_view(template_name='admin_lte/pages/widgets.html'), name='widgets'),
    path('calendar/', TemplateAPIView.as_view(template_name='admin_lte/pages/calendar.html'), name='calendar'),
    path('gallery/', TemplateAPIView.as_view(template_name='admin_lte/pages/gallery.html'), name='gallery'),
]

urlpatterns += router.urls

"""Layout Options part"""
urlpatterns += [
    path('layout/top-nav/', TemplateAPIView.as_view(template_name='admin_lte/pages/layout/top-nav.html'),
         name='layout_top-nav'),
    path('layout/top-nav-sidebar/',
         TemplateAPIView.as_view(template_name='admin_lte/pages/layout/top-nav-sidebar.html'),
         name='layout_top-nav-sidebar'),
    path('layout/boxed/',
         TemplateAPIView.as_view(template_name='admin_lte/pages/layout/boxed.html'), name='layout_boxed'),
    path('layout/fixed-sidebar/',
         TemplateAPIView.as_view(template_name='admin_lte/pages/layout/fixed-sidebar.html'),
         name='layout_fixed-sidebar'),
    path('layout/fixed-navbar/',
         TemplateAPIView.as_view(template_name='admin_lte/pages/layout/fixed-topnav.html'), name='layout_fixed-topnav'),
    path('layout/fixed-footer/',
         TemplateAPIView.as_view(template_name='admin_lte/pages/layout/fixed-footer.html'), name='layout_fixed-footer'),
    path('layout/collapsed-sidebar/',
         TemplateAPIView.as_view(template_name='admin_lte/pages/layout/collapsed-sidebar.html'),
         name='layout_collapsed-sidebar')
]

"""Charts part"""
urlpatterns += [
    path('charts/chartjs/', TemplateAPIView.as_view(template_name='admin_lte/pages/charts/chartjs.html'),
         name='chartjs'),
    path('charts/flot/', TemplateAPIView.as_view(template_name='admin_lte/pages/charts/flot.html'), name='flot'),
    path('charts/inline/', TemplateAPIView.as_view(template_name='admin_lte/pages/charts/inline.html'), name='inline'),
]

"""UI elements part"""
urlpatterns += [
    path('ui/general/', TemplateAPIView.as_view(template_name='admin_lte/pages/UI/general.html'), name='general'),
    path('ui/icons/', TemplateAPIView.as_view(template_name='admin_lte/pages/UI/icons.html'), name='icons'),
    path('ui/buttons/', TemplateAPIView.as_view(template_name='admin_lte/pages/UI/buttons.html'), name='buttons'),
    path('ui/sliders/', TemplateAPIView.as_view(template_name='admin_lte/pages/UI/sliders.html'), name='sliders'),
    path('ui/modals/', TemplateAPIView.as_view(template_name='admin_lte/pages/UI/modals.html'), name='modals'),
    path('ui/navbar/', TemplateAPIView.as_view(template_name='admin_lte/pages/UI/navbar.html'), name='navbar'),
    path('ui/timeline/', TemplateAPIView.as_view(template_name='admin_lte/pages/UI/timeline.html'), name='timeline'),
    path('ui/ribbons/', TemplateAPIView.as_view(template_name='admin_lte/pages/UI/ribbons.html'), name='ribbons'),
]

"""Forms part"""
urlpatterns += [
    path('forms/general/', TemplateAPIView.as_view(template_name='admin_lte/pages/forms/general.html'),
         name='general_form'),
    path('forms/advanced/', TemplateAPIView.as_view(template_name='admin_lte/pages/forms/advanced.html'),
         name='advanced_form'),
    path('forms/editors/', TemplateAPIView.as_view(template_name='admin_lte/pages/forms/editors.html'),
         name='editors_form'),
    path('forms/validation/', TemplateAPIView.as_view(template_name='admin_lte/pages/forms/validation.html'),
         name='validation_form'),
]

"""Tables part"""
urlpatterns += [
    path('tables/data/', TemplateAPIView.as_view(template_name='admin_lte/pages/tables/data.html'), name='data_table'),
    path('tables/jsgrid/', TemplateAPIView.as_view(template_name='admin_lte/pages/tables/jsgrid.html'),
         name='jsgrid_table'),
    path('tables/simple/', TemplateAPIView.as_view(template_name='admin_lte/pages/tables/simple.html'),
         name='simple_table'),
]

"""Mailbox part"""
urlpatterns += [
    path('mailbox/compose/', TemplateAPIView.as_view(template_name='admin_lte/pages/mailbox/compose.html'),
         name='compose_mailbox'),
    path('mailbox/mailbox/', TemplateAPIView.as_view(template_name='admin_lte/pages/mailbox/mailbox.html'),
         name='mailbox_mailbox'),
    path('mailbox/read-mail/', TemplateAPIView.as_view(template_name='admin_lte/pages/mailbox/read-mail.html'),
         name='read-mail_mailbox'),
]

"""Pages part"""
urlpatterns += [
    path('pages/invoice/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/invoice.html'),
         name='pages_invoice'),
    path('pages/invoice/print/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/invoice-print.html'),
         name='pages_invoice-print'),
    path('pages/profile/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/profile.html'),
         name='pages_profile'),
    path('pages/e-commerce/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/e-commerce.html'),
         name='pages_e-commerce'),
    path('pages/projects/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/projects.html'),
         name='pages_projects'),
    path('pages/project-add/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/project-add.html'),
         name='pages_project-add'),
    path('pages/project-edit/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/project-edit.html'),
         name='pages_project-edit'),
    path('pages/project-detail/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/project-detail.html'),
         name='pages_project-detail'),
    path('pages/contacts/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/contacts.html'),
         name='pages_contacts'),
]

"""Extra part"""
urlpatterns += [
    path('extra/login/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/login.html'),
         name='extra_login'),
    path('extra/register/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/register.html'),
         name='extra_register'),
    path('extra/forgot/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/forgot-password.html'),
         name='extra_forgot'),
    path('extra/recover/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/recover-password.html'),
         name='extra_recover'),
    path('extra/lockscreen/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/lockscreen.html'),
         name='extra_lockscreen'),
    path('extra/leg-user-menu/',
         TemplateAPIView.as_view(template_name='admin_lte/pages/examples/legacy-user-menu.html'),
         name='extra_leg-user-menu'),
    path('extra/lang-menu/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/language-menu.html'),
         name='extra_lang'),
    path('extra/error404/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/404.html'),
         name='extra_404'),
    path('extra/error500/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/500.html'),
         name='extra_500'),
    path('extra/pace/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/pace.html'),
         name='extra_pace'),
    path('extra/blank/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/blank.html'),
         name='extra_blank'),
    path('extra/starter/', TemplateAPIView.as_view(template_name='admin_lte/pages/examples/starter.html'),
         name='extra_starter'),
]
