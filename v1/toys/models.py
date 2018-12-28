from django.db import models

# Create your models here.
class Toy(models.Model):

    # Django automatically adds an auto-increment integer primary key column named id when it 
    # creates the database table related to the model. It is very important to notice that the 
    # model maps the underlying id column in an attribute named pk for the model.

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, default='')
    description = models.CharField(max_length=250, blank=True, default='')
    toy_category = models.CharField(max_length=200, blank=False, default='')
    release_date = models.DateTimeField()
    was_included_in_home = models.BooleanField(default=False)

    class Meta:
        # By default, we want the results ordered by the name attribute in ascending order.
        ordering = ('name',)