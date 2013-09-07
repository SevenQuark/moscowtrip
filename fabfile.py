from fabric.operations import local
from fabric.decorators import task
from yo_fabric.tasks import *
import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

# For vagrant
# env.user = 'vagrant'
# env.hosts = ['10.10.10.2']
# env.project_root = '/vagrant'
# env.virtualenv_root = '/home/vagrant/project-name-env'
# env.method = run
# env.key_filename = '/path/to/key'

env.project_root = PROJECT_ROOT
env.virtualenv_root = os.path.join(PROJECT_ROOT, '.env')
env.method = local


@task
def run():
    django_cmd('runserver')


@task
def shiva():
    django_sync()
    south_migrate()
    django_loaddata('main.json')
