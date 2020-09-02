from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import ResetNetworkInvestment


class ResetNetworkInvestmentAdmin(ModelAdmin):
    model = ResetNetworkInvestment
    menu_label = 'Reset Network Investment'
    menu_icon = 'placeholder'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('partner', 'name', 'primary_impact_area', 'geographic_focus', 'amount_committed', 'year')
    list_filter = ('partner__name', 'primary_impact_area', 'geographic_focus')
    search_fields = ('name', 'primary_impact_area', 'geographic_focus', 'year')

modeladmin_register(ResetNetworkInvestmentAdmin) 
