from fabric.api import local

def manage_dev(command="runserver"):
    local("python manage.py %s" % command)
