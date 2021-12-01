from django.forms import (
    Form,
    ModelForm,
    CharField,
    FileField,
)

from .models import Visit


class VisitForm(ModelForm):

    class Meta:

        model = Visit
        fields = '__all__'


class VisitorNameForm(Form):

    visitor_name = CharField()


class UploadCsvForm(Form):

    csv_file = FileField()
