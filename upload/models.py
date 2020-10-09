from django.db import models
import datetime
import os


HOTEL_CODE = 'DOHRZ'

def rename_file():
    pass

class Future(models.Model):
    hotel_code = models.CharField(max_length=20)
    file_name = models.FileField(upload_to=f'{HOTEL_CODE}/future/', max_length=100)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name


    def delete(self, *args, **kwargs):
        self.file_name.delete()
        super().delete(*args, **kwargs)



class DataReport(models.Model):
    date = models.DateField()
    market_code = models.CharField(max_length=100, null=True)
    room_night = models.IntegerField()
    room_revenue = models.IntegerField()
    room_capacity =models.PositiveIntegerField()
    Uploaded_on = models.DateTimeField(auto_now_add=True)
    # file_name = models.ForeignKey(Future, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.Uploaded_on)

    # def remove_on_file_update(self):
    #     try:
    #         # is the object in the database yet?
    #         obj = self.objects.get(id=self.id)
    #     except self.DoesNotExist:
    #         # object is not in db, nothing to worry about
    #         return
    #     # is the save due to an update of the actual image file?
    #     if obj.file_name and self.file_name and obj.file_name != self.file_name:
    #         # delete the old image file from the storage in favor of the new file
    #         obj.file_name.delete()

    # def delete(self, *args, **kwargs):
    #     # object is being removed from db, remove the file from storage first
    #     self.file_name.delete()
    #     return super(MyImageModel, self).delete(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     # object is possibly being updated, if so, clean up.
    #     self.remove_on_file_update()
    #     return super(MyImageModel, self).save(*args, **kwargs)

# from uuid import uuid4
# def get_file_path(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = "%s.%s" % (uuid4(), ext)
#     return os.path.join(instance, filename)


class ImportFiles(models.Model):
    files = models.FileField(upload_to=f'{HOTEL_CODE}/%Y-%m-%d/', blank=True, null=True)
    file_name = models.CharField(max_length = 100, blank=True, null=True)
    file_path = models.URLField()
    is_active = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Files {}'.format(self.file_name)
    
    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)
    
    # def save(self, *args, **kwargs):
    #     pass

    # @property
    # def filename(self):
    #     name = self.file.name.split("/")[1].replace('_',' ').replace('-',' ')
    #     return name
    # def get_absolute_url(self):
    #     return reverse('myapp:document-detail', kwargs={'pk': self.pk})



