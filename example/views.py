# example/views.py
from datetime import datetime

from django.http import HttpResponse
from pyamaze import maze,agent

def index(request):
    now = datetime.now()
    
    m=maze(20,20)
    m.CreateMaze(loopPercent=50)
    a=agent(m,filled=True,footprints=True)
    m.tracePath({a:m.path})
    m.run()
    return HttpResponse("Your Maze game Ends, Thank You")
