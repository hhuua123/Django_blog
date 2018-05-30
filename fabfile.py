from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "git@github.com:hhuua123/Django_blog.git"

env.user = 'root'
env.password = 'huangye@6450'

# 填写你自己的主机对应的域名
env.hosts = ['www.hhuua.com']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '22'


def deploy():
    source_folder = '/srv/sites/www.hhuua.com/Django_blog'

    run('cd %s && git pull' % source_folder)
    run('source ./env/bin/activate')
    run("""
        pip install -r requirements.txt &&
        python manage.py collectstatic --noinput &&
        python manage.py migrate
        """.format(source_folder))
    run('gunicorn --bind unix:/tmp/www.hhuua.com.socket blogproject.wsgi:application')
    sudo('./etc/init.d/nginx')