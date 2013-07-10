from fabric.api import local
from tools import templater
import os

djangobox_dir = os.path.dirname(os.path.abspath(__file__))

def safe_create_box_dir():
    try:
        local('mkdir box')
    except:
        pass


def build_benjamin(project_name):
    local('django-admin.py startproject --template=tools/'
      'build_templates/benjamin %s' % project_name)
    safe_create_box_dir()
    local('mv %s box/%s' % (project_name, project_name))


def build_batsunan(project_name):
    local('django-admin.py startproject --template=tools/'
      'build_templates/batsunan %s' % project_name)
    build_single_file(os.path.join(project_name, 'Procfile'),
      os.path.join(project_name, 'Procfile'), project_name)
    safe_create_box_dir()
    local('mv %s box/%s' % (project_name, project_name))


def build_jiro(project_name):
    local('django-admin.py startproject --template=tools/'
      'build_templates/jiro %s' % project_name)
    build_single_file(os.path.join(project_name, 'Procfile'),
      os.path.join(project_name, 'Procfile'), project_name)
    safe_create_box_dir()
    local('mv %s box/%s' % (project_name, project_name))


def build_single_file(inp, out, project_name, app_name=''):
    templater.create_template(inp, out, {'project_name': project_name,
      'app_name': app_name})
