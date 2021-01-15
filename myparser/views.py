from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from stl import mesh
from math import sqrt
from src import read_stl
from src import stl_extraction
from src import stl_calculation


def upload_file(request):
    """
    This is the main function which will use all the helper function to
    extract the data from stl file.
    """
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location='files/')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        uploaded_file_url = mesh.Mesh.from_file("files/" + myfile.name)
        plot = read_stl.ReadStl(uploaded_file_url)
        plot = plot.plot_stl()
        minx, maxx, miny, maxy, minz, maxz = stl_extraction.calc_dimension(uploaded_file_url)
        w1, l1, h1 = maxx - minx, maxy - miny, maxz - minz
        volume = stl_calculation.CalculateVolume(uploaded_file_url)
        volume = volume.calc_volume()
        radius = stl_extraction.circle_radius(w1, l1, h1)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url,
            "X": maxx - minx,
            "Y": maxy - miny,
            "Z": maxz - minz,
            "Length": l1,
            "Width": w1,
            "Height": h1,
            "volume": volume,
            "Radius": radius,
            "plot": plot,
        
        })
    return render(request, 'upload.html')
