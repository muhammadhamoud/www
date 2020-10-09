from .models import ImportFiles
from .forms import ImportFilesForm
from django.shortcuts import render, redirect
from upload.forms import FutureForm
from upload.models import Future, DataReport
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.conf.urls.static import static
from upload.handle_files import handle_uploaded_file, is_file_valid
import os
import datetime as dt

# Create your views here.

def upload_show_list(request):
    context = {}
    if request.method == 'POST':
        form = FutureForm(request.POST, request.FILES)
        uploaded_file = request.FILES['file_name']
        if uploaded_file.name.endswith(('.txt', '.csv')):
            if form.is_valid():
                form.save()
                handle_uploaded_file(request.FILES['file_name'])
                return redirect('file_list')
        else:
            context['error'] = f'{uploaded_file} type should be either text or csv file.'
            context['form'] = FutureForm()
    else:
        context['form'] = FutureForm()
    files = Future.objects.order_by('-upload_time')
    context['files'] = files
    return render(request, 'upload/file_list.html', context)



def delete_file(request, pk):
    if request.method == 'POST':
        file_ = Future.objects.get(pk=pk)
        file_.delete()
    return redirect('file_list')




FILE_TYPES = ['txt']

def import_files_view(request):
    if request.method == 'POST':
        form = ImportFilesForm(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        if form.is_valid():
            objs, file_list = [], []
            for f in files:
                # is_valid, file_name = is_file_valid(file_name=f)
                # file_name = f'{file_name}_{dt.datetime.now()}'
                file_instance = ImportFiles(files=f)
                # handle_uploaded_file(f)
                file_instance.is_active = True
                file_instance.file_path = 'placeholder' #f.files.url
                file_type = file_instance.files.url.split('.')[-1]
                file_type = file_type.lower()
                if file_type not in FILE_TYPES:
                    print('Not valid file type')
                
                handle_uploaded_file(file_instance.files)

                return redirect('sample_report')
                error = f'{f} File is not valid'

            return render(request, 'upload/import_files.html', {'form': form, 'obj': file_instance, 'objs': objs})
    else:
        form = ImportFilesForm()
        error = 'File is not valid'
    
    return render(request, 'upload/import_files.html', {'form': form, 'error': error})


from django.db.models import Sum, F
from django.db.models.functions import TruncMonth

def sample_report(request):
    # result = (
    #     DataReport.objects
    #     .all()
    #     .values_list('date__year', 'date__month')
    #     .annotate(Sum('room_night'))
    #     .order_by('date__year', 'date__month')
    #     )

    # result = (DataReport.objects
    #           .annotate(month=TruncMonth('date'))
    #           .values('month')
    #           .annotate(total=Sum('room_night'))
    #           .order_by())
    
    result = (DataReport.objects
            .annotate(month=TruncMonth('date'))
            .values('month')
            .annotate(
                room_night=Sum('room_night'), 
                room_revenue=Sum('room_revenue'),
                average_rate = F('room_revenue') / F('room_night')
                )
            .order_by()).filter(month__lt='2020-03-01')

    return render(
        request,
        'upload/sample_report.html',
        {
            'data': result,
        }
    )


# def file_list(request):
#     files = Future.objects.order_by('-upload_time')
#     return render(request, 'upload/file_list.html', {
#         'files': files
#         })


# def future(request):
#     context = {}
#     if request.method == 'POST':
#         form = FutureForm(request.POST, request.FILES)
#         uploaded_file = request.FILES['file_name']
#         if uploaded_file.name.endswith(('.txt', '.csv')):
#             if form.is_valid():
#                 form.save()

#                 print(request.FILES['file_name'])
#                 # dir(request.FILES['file_name'])
#                 # handle_uploaded_file(str(request.FILES['file_name']))
#                 return redirect('file_list')

#         else:
#             context['error'] = f'{uploaded_file} type should be either text or csv file.'
#             context['form'] = FutureForm()

#     else:
#         context['form'] = FutureForm()
    
#     return render(request, 'upload/upload_future.html', context)


# # Use to upload only one file
# def upload(request):
#     context = {}
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         if uploaded_file.name.endswith(('.txt', '.csv')):
#             fs = FileSystemStorage()
#             name = fs.save(uploaded_file.name, uploaded_file)
#             context['url'] = fs.url(name)
#         else:
#             context['error'] = 'file type should be either text or csv file.'
#     return render(request, 'upload/upload.html', context)
