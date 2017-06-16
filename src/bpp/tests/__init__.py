from autoslug.fields import AutoSlugField
from bpp import autocomplete_light_registry
autocomplete_light_registry # Leave this alone, PyCharm!

from django_bpp import urls
urls


from model_mommy import mommy

mommy.generators.add('django.contrib.postgres.fields.array.ArrayField',
                     lambda x: [])

mommy.generators.add('django.contrib.postgres.search.SearchVectorField',
                     lambda x=None: None)


from bpp.tests.util import *
#
#from test_abstract import *
#from test_admin import *
#from test_autocomplete import *
#from test_cache import *
#from test_commands import *
#from test_imports import *
#from test_jezyk_polski import *
#from test_management import *
#from test_models import *
#from test_multiseek import *
#from test_tasks import *
#from test_templatetags import *
#from test_util import *
#
#from test_views import *
#from test_reports import *
#
#import os
#if os.getenv("NO_SELENIUM", "0") != "1":
#    from test_selenium import *
#from test_selenium.test_admin import *
