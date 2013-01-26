from fabric.api import local
from tools import templater
import os

djangobox_dir = os.path.dirname(os.path.abspath(__file__))

def build_benjamin(project_name):
    local('django-admin.py startproject --template=tools/'
      'build_templates/benjamin %s' % project_name)

def build_rimururu(project_name, app_name='core'):
    build_pinax_zero(project_name)
    inner_project_path = os.path.join(project_name, project_name)
    os.chdir(os.path.join(djangobox_dir, inner_project_path))
    local('django-admin.py startapp %s' % app_name)
    os.chdir(djangobox_dir)
    app_path = os.path.join(inner_project_path, app_name)
    viewbox_path = os.path.join(inner_project_path, 'templates',  
      'viewbox.html')
    templater.create_template('tools/build_templates/rimururu/'
      'rimururu_viewbox.html', viewbox_path, {})
    views_path = os.path.join(app_path, "views.py")
    templater.create_template('tools/build_templates/rimururu/'
      'rimururu_views.py', views_path, {'project_name': project_name, 
      'app_name': app_name})
    urls_path = os.path.join(inner_project_path, "urls.py")
    templater.create_template('tools/build_templates/rimururu/'
      'rimururu_urls.py', urls_path, {'project_name': project_name, 
      'app_name': app_name})

def build_pinax_zero(project_name):
    local('django-admin.py startproject --template=https://github.com/'
      'pinax/pinax-project-account/zipball/master %s' % project_name)

def build_single_template(inp, out, project_name, app_name=''):
    templater.create_template(inp, outp, {'project_name': project_name,
      'app_name': app_name}) 
