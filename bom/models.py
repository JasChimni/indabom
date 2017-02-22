from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator

class PartClass(models.Model):
    code = models.IntegerField(default=0, unique=True, validators=[MaxValueValidator(999)])
    name = models.CharField(max_length=255, default='')
    comment = models.CharField(max_length=255, default='', blank=True)

# Numbering scheme is hard coded for now, may want to change this to a setting depending on a part numbering scheme
class Part(models.Model):
    number_class = models.ForeignKey(PartClass, default=None, blank=False, related_name='number_class')
    number_item = models.IntegerField(default=None, blank=True, validators=[MaxValueValidator(9999)])
    number_variation = models.IntegerField(default=None, blank=True, validators=[MaxValueValidator(99)])
    description = models.CharField(max_length=255, default='')
    revision = models.CharField(max_length=2, default='1')
    manufacturer_part_number = models.CharField(max_length=128, default='', blank=True)
    manufacturer = models.CharField(max_length=128, default='', blank=True)
    subparts = models.ManyToManyField('self', blank=True, symmetrical=False, through='Subpart', through_fields=('assembly_part', 'assembly_subpart'))
    minimum_order_quantity = models.IntegerField(null=True, blank=True)
    minimum_pack_quantity = models.IntegerField(null=True, blank=True)
    unit_cost = models.DecimalField(null=True, max_digits=8, decimal_places=4, blank=True)

    class Meta():
        unique_together = (('number_class', 'number_item', 'number_variation')),

    def atlas_part_number(self):
        return "{0:0=3d}-{1:0=4d}-{2:0=2d}".format(self.number_class.code,self.number_item,self.number_variation)

    def save(self):
        if self.number_item is None or self.number_item == 0:
            last_number_item = Part.objects.all().order_by('number_item').last()
            if not last_number_item:
                self.number_item = 1
            else:
                self.number_item = last_number_item.number_item + 1
        if self.number_variation is None or self.number_variation == 0:
            last_number_variation = Part.objects.all().filter(number_item=self.number_item).order_by('number_variation').last()
            if not last_number_variation:
                self.number_variation = 1
            else:
                self.number_variation = last_number_variation.number_variation + 1
        if self.manufacturer_part_number == '' and self.manufacturer == '':
            self.manufacturer_part_number = self.atlas_part_number()
            self.manufacturer = 'Atlas Wearables'
        super(Part, self).save()

class Subpart(models.Model):
    assembly_part = models.ForeignKey(Part, related_name='assembly_part', null=True)
    assembly_subpart = models.ForeignKey(Part, related_name='assembly_subpart', null=True)
    count = models.IntegerField(default=1)