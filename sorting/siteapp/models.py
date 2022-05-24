from django.db import models


class Sort(models.Model):
    algorithm_type = models.CharField(max_length=30, choices=(('Bubble', 'Bubble'), ('Insertion', 'Insertion'),
                                                              ('Merge', 'Merge')), default='Bubble')
    input_array = models.FileField(upload_to='unsorted/')
    sorted_array = models.FileField(upload_to='sorted/', blank=True)
    execution_time = models.CharField(max_length=30)

    def __str__(self):
        return self.algorithm_type
