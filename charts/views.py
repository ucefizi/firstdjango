from django.shortcuts import render

def simple(request):
    import django

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from firstapp.models import Room

    rooms = Room.objects.all()
    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    z=[]
    for room in rooms:
        x.append(room.id)
        y.append(room.temp)
        z.append(room.press)
    ax.plot(x, y, 'ro-')
    ax.plot(x, z, 'bo')
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
   