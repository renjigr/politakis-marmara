from django.db import models
from django.utils.text import slugify
from easy_thumbnails.fields import ThumbnailerImageField
from django.template.defaultfilters import slugify
from slugify import slugify_el
# Create your models here.


class WorkModel(models.Model):
    my_choices =(('marble','Μάρμαρο'),('granite','Γρανίτης'),
                 ('quartz','Χαλαζιακά'))
    place_choices = (('bath','Μπάνια'),('out','Εξωτερικοί χώροι'),
                     ('cousines','Κουζίνες'),('floor','Πάτωμα'),
                     ('fireplace','Τζάκια'),('stairs','Σκάλες'),
                     ('art','Καλλιτεχνίματα')
                     )

    name = models.CharField (max_length= 255, unique=True)
    slug = models.SlugField(unique=True, max_length=255,blank=True)
    material_type = models.CharField(max_length = 10,choices = my_choices)
    place_type = models.CharField(max_length = 28, choices = place_choices)
    image1 = models.ImageField(upload_to='images/%Y/%m/%d')
    image2 = models.ImageField(upload_to='images/%Y/%m/%d',blank=True,null=True)
    image3 = models.ImageField(upload_to='images/%Y/%m/%d',blank=True,null=True)
    description = models.CharField(max_length= 255,blank=True,null=True)


    def _get_unique_slug(self):
        slug = slugify_el(self.name)
        unique_slug = slug
        num = 1
        while WorkModel.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()


    @models.permalink
    def get_absolute_url(self):
        return ('work_details', [self.slug,])


    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)



class IndexModel(models.Model):
    name = models.CharField (max_length= 255, unique=True)
    bathi = models.ImageField(upload_to='images/%Y/%m/%d')
    outi = models.ImageField(upload_to='images/%Y/%m/%d')
    cousinei = models.ImageField(upload_to='images/%Y/%m/%d')
    floori = models.ImageField(upload_to='images/%Y/%m/%d')
    fireplacei = models.ImageField(upload_to='images/%Y/%m/%d')
    stairsi = models.ImageField(upload_to='images/%Y/%m/%d')
    arti = models.ImageField(upload_to='images/%Y/%m/%d')

    def __str__(self):
        return self.name
