from django.shortcuts import render
from siteapp.models import Sort
from siteapp.algorithms import BubbleSort, InsertionSort, MergeSort
from siteapp.forms import SortForm
from datetime import datetime


def sort_file(algorithm_type, sorter, new_record):
    line = new_record.input_array.read().decode("utf-8")
    array = [int(digit) for digit in line.split(' ')]
    sorted_array, execution_time = sorter.sort(array)
    sorted_filename = f'sorted/sorted_{algorithm_type}_' \
                      f'{datetime.now().isoformat(" ", "seconds")}_{new_record.input_array}'
    with open(f'media/{sorted_filename}', 'w') as writer:
        writer.write(' '.join([str(el) for el in sorted_array]))
    new_record.sorted_array = sorted_filename
    new_record.execution_time = execution_time
    return new_record


def main_view(request):
    if request.method == 'GET':
        context = {'form': SortForm()}
        return render(request, 'base.html', context)
    elif request.method == 'POST':
        try:
            form = SortForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                algorithm_type = data.get('algorithm_type')
                input_array = request.FILES['input_array']
                new_record = Sort()
                new_record.algorithm_type = algorithm_type
                new_record.input_array = input_array
                sort_type = None
                if algorithm_type == 'Bubble':
                    sort_type = BubbleSort()
                elif algorithm_type == 'Insertion':
                    sort_type = InsertionSort()
                elif algorithm_type == 'Merge':
                    sort_type = MergeSort()
                new_record = sort_file(algorithm_type, sort_type, new_record)
                context = {
                    'execution_time': new_record.execution_time,
                    'url': f'media/{new_record.sorted_array}'
                }
                new_record.save()
                return render(request, 'result.html', context)
        except ValueError:
            return render(request, 'file_error.html')
