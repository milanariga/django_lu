from django.shortcuts import render
from django.http import HttpResponse

from .forms import (
    VisitForm,
    VisitorNameForm,
    UploadCsvForm,
)

from .csv_handler import (
    read_and_decode_csv,
    visits_csv_rows_to_db,
)

from .models import Visit


def filter_visits_by_visitor(request):

    form = VisitorNameForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            visitor_name = form.cleaned_data['visitor_name']
            visits = Visit.objects.filter(visitor=visitor_name)

            context = {
                'visits': visits,
            }

            return render(
                request,
                template_name='visits.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='visit_form.html',
        context=context,
    )


def get_all_visits(request):

    visits = Visit.objects.all()

    context = {
        'visits': visits,
    }

    return render(
        request,
        template_name='visits.html',
        context=context,
    )


def get_visit(request, visit_id):

    visit = Visit.objects.get(id=visit_id)

    context = {
        'visit': visit,
    }

    return render(
        request,
        template_name='visit.html',
        context=context,
    )


def add_visit(request):

    form = VisitForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            visit = form.save()

            context = {
                'visit': visit,
            }

            return render(
                request,
                template_name='visit.html',
                context=context,
            )

    return render(
        request,
        template_name='visit_form.html',
        context={'form': form}
    )


def upload_csv_to_db(request):

    form = UploadCsvForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':

        if form.is_valid():

            decoded_file = read_and_decode_csv(request.FILES['csv_file'])
            visits_csv_rows_to_db(decoded_file)

            return HttpResponse('CSV records added to the database!')

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='visit_form.html',
        context=context,
    )
