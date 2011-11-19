from fabric.api import local

def test():
    local("./manage.py test")

def commit():
    local("git add . && git commit")

def push():
    local("git push")

def push_epio():
    local("epio upload")

def deploy():
    test()
    commit()
    push()
    push_epio()
