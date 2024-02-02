# example/views.py
from datetime import datetime

from django.http import HttpResponse
from pyamaze import maze,agent

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    
    m=maze(20,20)
    m.CreateMaze(loopPercent=50)
    a=agent(m,filled=True,footprints=True)
    m.tracePath({a:m.path})
    m.run()
    return HttpResponse("Your Maze game Ends, Thank You")