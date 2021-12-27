import os, sys, django
settings = f'{sys.argv[1]}.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
django.setup()

from  django.apps import apps
if not apps.is_installed('alla'):
    print(f'Add "alla" in {settings}.INSTALLED_APPS')
    os.remove(sys.argv[0])
    exit()

from alla.models import EpData
allepds = open('alla/setup/epds.txt', 'r')
epds = allepds.read().split('\n\n')

for i in range(len(epds)):
    epd = epds[i].split('\n')
    ep = EpData(epnum=i+1, name=epd[0], details=epd[1], date=epd[2])
    ep.save()

print(f' In {sys.argv[1]}.urls add "from django.urls import path, include" and in urlpatterns append "path(\'alla/\', include(\'alla.urls\')),"')
os.remove(sys.argv[0])