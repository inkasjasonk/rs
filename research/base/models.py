
from django.db import models


def getattr_related(obj, field):
    qs = getattr(obj, field.name).all()   
    return ', '.join([u'%s' % (val.name) for val in qs])

class RawData(object):

    def get_fields(self):
        fields = [(field.name, getattr(self,field.name)) for field in self._meta.fields]
        meta_fields = [(field.name, getattr_related(self, field)) for field in self._meta.many_to_many]
        return fields + meta_fields

    def meta(self):
        return self._meta

    def class_name(value):
        return value.__class__.__name__.lower() 

class Manufacturer(models.Model, RawData):
    name = models.CharField("Name",max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    employees = models.IntegerField(blank=True, null=True)
    sales = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

    def __unicode__(self):
        return u'%s' % (self.name)

class Store(models.Model, RawData):
    name = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Stores"

    def __unicode__(self):
        return u'%s' % (self.name)

class LockRating(models.Model, RawData):
    rating = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Lock Rating"
        verbose_name_plural = "Lock Ratings"

    def __unicode__(self):
        return u'%s' % (self.rating)

class SafeRating(models.Model, RawData):
    rating = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Safe Rating"
        verbose_name_plural = "Safe Ratings"

    def __unicode__(self):
        return u'%s' % (self.rating)

class SafeComponentCategory(models.Model, RawData):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Safe Component Category"
        verbose_name_plural = "Safe Component Categories"

    def __unicode__(self):
        return u'%s' % (self.name)

class SafeCategory(models.Model, RawData):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Safe Category"
        verbose_name_plural = "Safe Categories"

    def __unicode__(self):
        return u'%s' % (self.name)

class SafeFeature(models.Model, RawData):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Safe Feature"
        verbose_name_plural = "Safe Features"

    def __unicode__(self):
        return u'%s' % (self.name)

class SafeProfile(models.Model, RawData):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    manufacturer = models.ForeignKey('Manufacturer')
    store = models.ForeignKey('Store')
    category = models.ForeignKey('SafeCategory')
    volume = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    lock_rating = models.ForeignKey('LockRating', blank=True, null=True)
    safe_ratings = models.ManyToManyField('SafeRating', blank=True, null=True)
    bolt_diameter = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    wall_thickness = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    door_thickness = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    features = models.ManyToManyField('SafeFeature', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Safe Profile"
        verbose_name_plural = "Safe Profiles"

    def __unicode__(self):
        return u'%s' % (self.name)

class SafeComponentProfile(models.Model, RawData):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    manufacturer = models.ForeignKey('Manufacturer')
    store = models.ForeignKey('Store')
    category = models.ForeignKey('SafeComponentCategory')
    description = models.TextField(blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Safe Component Profile"
        verbose_name_plural = "Safe Component Profiles"

    def __unicode__(self):
        return u'%s' % (self.name)





    


