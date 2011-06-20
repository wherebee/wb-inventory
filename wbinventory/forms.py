from django.forms.models import ModelForm
from uni_form.helpers import FormHelper, Submit, HTML, Row
from wbinventory.models import Item


save_helper = FormHelper()
submit = Submit('save', 'Save')
save_helper.add_input(submit)

# TODO: Cancel link
## cancel = HTML('<a href="javascript:history.go(-1)">Cancel</a>')


class ItemForm(ModelForm):

    class Meta:
        model = Item
        fields = (
            'number',
            'name',
            'description',
            'default_uom',
            'default_location',
            'reorder_quantity',
            'target_quantity',
        )

    helper = save_helper
