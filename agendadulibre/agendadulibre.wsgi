import sys
sys.path.insert(0, '/opt/agendadulibreshow/agendadulibre')

#sys.path.insert(0, os.curdir)

activate_this = '/home/numahell/.virtualenvs/flask/local/bin/activate_this.py'
activate_this = '/opt/agendadulibreshow/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))


from app import app as application
