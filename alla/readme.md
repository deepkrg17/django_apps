# Aladdin Episode Details 
This is an Django app for viewing Alladin episode details.
## Setup
Clone this sub-directory in project main folder. You can use [subdirGit.sh](https://gist.github.com/deepkrg17/a8deb79ba22674d884e81c6de65234d7).
1. Add `'alla'` in {{project}}.settings.INSTALLED_APPS
2. In {{project}}.urls add `from django.urls import path, include`
3. In {{project}}.urls.urlpatterns append `path('alla/', include('alla.urls')),`

4. > Run this code in main project folder,

```bash
  sh alla/setup/setup.sh
```