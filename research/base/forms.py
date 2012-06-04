from django import forms
from models import *


class ChoiceField(forms.ChoiceField):
    def __init__(self, choices=(), empty_label=None, required=True, widget=None, label=None,
                 initial=None, help_text=None, *args, **kwargs):

        # prepend an empty label if it exists (and field is not required!)
        if empty_label is not None:
            choices = tuple([(u'', empty_label)] + list(choices))

        super(ChoiceField, self).__init__(choices=choices, required=required, widget=widget, label=label,
                                        initial=initial, help_text=help_text, *args, **kwargs)

class GraphSafesForm(forms.Form):

    manufacturers = ChoiceField( choices=((opt['name'], opt['name']) for opt in
                    Manufacturer.objects.filter(safeprofile__isnull=False, name__isnull=False).values('name').distinct()), required=True, empty_label="Select a manufacturer" )

    stores = ChoiceField( choices=((opt['name'], opt['name']) for opt in
                    Store.objects.filter(safeprofile__isnull=False, name__isnull=False).values('name').distinct()), required=True, empty_label="Select a store" )

    categories = ChoiceField( choices=((opt['name'], opt['name']) for opt in
                    SafeCategory.objects.filter(name__isnull=False).values('name').distinct()), required=True, empty_label="Select a category" )

    volumes = ChoiceField( choices=((opt['volume'], opt['volume']) for opt in
                    SafeProfile.objects.filter(volume__isnull=False).values('volume').distinct()), required=True, empty_label="Select a volume" )

    weights = ChoiceField( choices=((opt['weight'], opt['weight']) for opt in
                   SafeProfile.objects.filter(weight__isnull=False).values('weight').distinct()), required=True, empty_label="Select a weight" )

    lock_ratings = ChoiceField( choices=((opt['rating'], opt['rating']) for opt in
                    LockRating.objects.filter(rating__isnull=False).values('rating').distinct()), required=True, empty_label="Select a lock rating" )

    bolt_diameters = ChoiceField( choices=((opt['bolt_diameter'], opt['bolt_diameter']) for opt in
                    SafeProfile.objects.filter(bolt_diameter__isnull=False).values('bolt_diameter').distinct()), required=True, empty_label="Select a bolt diameter" )

    door_thicknesses = ChoiceField( choices=((opt['door_thickness'], opt['door_thickness']) for opt in
                    SafeProfile.objects.filter(door_thickness__isnull=False).values('door_thickness').distinct()), required=True, empty_label="Select a door thickness" )

    safe_ratings = forms.MultipleChoiceField( choices=((opt['rating'], opt['rating']) for opt in
                    SafeRating.objects.filter(rating__isnull=False).filter(safeprofile__isnull=False).values('rating').distinct()))

    features = forms.MultipleChoiceField( choices=((opt['name'], opt['name']) for opt in
                    SafeFeature.objects.filter(name__isnull=False).values('name').distinct()), required=True)



class GraphSafeComponentForm(forms.Form):

    manufacturers = ChoiceField( choices=((opt['name'], opt['name']) for opt in
                    Manufacturer.objects.filter(safecomponentprofile__isnull=False, name__isnull=False).values('name').distinct()), required=True, empty_label="Select a manufacturer" )

    stores = ChoiceField( choices=((opt['name'], opt['name']) for opt in
                    Store.objects.filter(safecomponentprofile__isnull=False, name__isnull=False).values('name').distinct()), required=True, empty_label="Select a store" )

    categories = ChoiceField( choices=((opt['name'], opt['name']) for opt in
                    SafeCategory.objects.filter(name__isnull=False).values('name').distinct()), required=True, empty_label="Select a category" )






