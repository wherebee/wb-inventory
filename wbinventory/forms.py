import django.forms
from django.forms.models import ModelForm
from uni_form.helpers import FormHelper, Submit, HTML, Row
from wbinventory.models import Item, ItemTransaction


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


class ItemAddForm(ModelForm):

    class Meta:
        model = ItemTransaction
        fields = (
            'item',
            'to_location',
            'to_quantity',
            'to_uom',
        )
        widgets = {
            'item': django.forms.HiddenInput(),
        }

    helper = save_helper


class ItemRemoveForm(ModelForm):

    class Meta:
        model = ItemTransaction
        fields = (
            'item',
            'from_location',
            'from_quantity',
            'from_uom',
        )
        widgets = {
            'item': django.forms.HiddenInput(),
        }

    helper = save_helper


class ItemMoveForm(ModelForm):

    class Meta:
        model = ItemTransaction
        fields = (
            'item',
            'from_location',
            'from_quantity',
            'from_uom',
            'to_location',
        )
        widgets = {
            'item': django.forms.HiddenInput(),
        }

    helper = save_helper


class ItemConvertForm(ModelForm):

    class Meta:
        model = ItemTransaction
        fields = (
            'item',
            'from_location',
            'from_quantity',
            'from_uom',
            'to_quantity',
            'to_uom',
        )
        widgets = {
            'item': django.forms.HiddenInput(),
        }

    helper = save_helper
