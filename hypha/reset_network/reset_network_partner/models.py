import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from hypha.reset_network.reset_network_utils.models import ResetNetworkBasePage


class ResetNetworkPartnersPage(ResetNetworkBasePage):
    class Meta:
        verbose_name = "Reset Network Partners Page"

    parent_page_types = ['reset_network_home.ResetNetworkHomePage']
    subpage_types = ['reset_network_partner.ResetNetworkPartnerPage']

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        partners = ResetNetworkPartnerPage.objects.live().public()
        context = super().get_context(request, *args, **kwargs)
        context['partners'] = partners
        return context


class ResetNetworkPartnerPage(ResetNetworkBasePage):
    STATUS = [
        ('current_partner', 'Current Partner'),
        ('alumni_partner', 'Alumni Partner')
    ]

    TYPE = [
        ('profit', 'For Profit'),
        ('non_profit', 'Non Profit')
    ]

    class Meta:
        verbose_name = "Reset Network Partner Page"

    parent_page_types = ['reset_network_partner.ResetNetworkPartnersPage']
    subpage_types = []

    name = models.CharField(max_length=100)
    status = models.CharField(
        choices=STATUS, default='current_partner', max_length=20
    )
    type = models.CharField(
        choices=TYPE, default='non_profit', max_length=20
    )
    description = RichTextField(blank=True)
    web_url = models.URLField(blank=True)
    logo_url = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('status'),
        FieldPanel('type'),
        FieldPanel('description'),
        FieldPanel('web_url'),
        FieldPanel('logo_url'),
    ]

    def __str__(self):
        return self.name

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)    


class ResetNetworkInvestment(models.Model):

    PRIMARY_IMPACT_AREA = [
        ('civic_empowerment', 'Civic Empowerment'),
        ('data_and_digital_rights', 'Data & Digital Rights'),
        ('financial_transparency', 'Financial Transparency'),
        ('independent_media', 'Independent Media'),
        ('reset', 'Reset'),
        ('other', 'Other'),
    ]

    GEOGRAPHIC_FOCUS = [
        ('africa', 'Africa'),
        ('central_and_eastern_europe', 'Central And Eastern Europe'),
        ('global', 'Global'),
        ('latin_america', 'Latin America'),
        ('multi_country', 'Multi-Country'),
        ('southeast_asia', 'Southeast Asia'),
        ('united_states', 'United States'),
        ('western_europe', 'Western Europe'),
        ('other', 'Other'),
    ]

    partner = models.ForeignKey(
        ResetNetworkPartnerPage,
        on_delete=models.CASCADE,
        related_name='investments'
    )
    name = models.CharField(max_length=50)
    primary_impact_area = models.CharField(
        default='',
        max_length=50,
        choices=PRIMARY_IMPACT_AREA
    )
    geographic_focus = models.CharField(
        default='',
        max_length=50,
        choices=GEOGRAPHIC_FOCUS
    )
    year = models.IntegerField(
        default=current_year,
        validators=[MinValueValidator(1984), max_value_current_year],
        help_text='Use format: <YYYY>'
    )
    amount_committed = models.DecimalField(
        decimal_places=2,
        default=0,
        max_digits=11,
        verbose_name='Ammount Commited US$'
    )
    type = models.CharField(
        max_length=200, blank=True,
    )
    purpose = models.CharField(
        max_length=200, blank=True
    )
    description = models.TextField()
