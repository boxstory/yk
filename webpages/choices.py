from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.translation import gettext_lazy as _


class Language(models.TextChoices):
    FRENCH = 'F', _('French')
    SPANISH = 'S', _('Spanish')
    ARABIC = 'A', _('Arabic')
    MANDARIN = 'M', _('Mandarin')


# class Science(models.TextChoices):
#     BIOLOGY = 'BIO', _('Biology')
#     CHEMISTRY = 'CHEM', _('Chemistry')
#     PHYSICS = 'PHY', _('Physics')
#     COMPUTERSCIENCE = 'CS', _('Computer Science')
#     DESIGNTECHNOLOGY = 'DT', _('Design Technology')
#     ESS = 'ESS', _('Environmental Systems and Societies')


# class Society(models.TextChoices):
#     MANAGEMENT = 'BM', _('Business Management')
#     ECONOMICS = 'ECON', _('Economics')
#     GEOGRAPHY = 'GEO', _('Geography')
#     GLOBALPOLITICS = 'GP', _('Global Politics')
#     HISTORY = 'HIS', _('History')
#     PSYCHOLOGY = 'PSYCH', _('Psychology')


# class Art(models.TextChoices):
#     VISUALARTS = 'VA', _('Visual Arts')
#     MUSIC = 'MUS', _('Music'),
#     FILM = 'FILM', _('Film')
