from django.db import models


class Course(models.Model):
    PLATFORM = (
        ('Udemy', 'Udemy'),
        ('YouTube', 'YouTube'),
    )

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    instructor = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=PLATFORM)
    link = models.URLField()
    image = models.URLField()
    show = models.BooleanField(default=True)
    show_to_home = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=False)
    completed = models.IntegerField()
    hours = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    code = models.URLField(blank=True)

    def __str__(self):
        return self.title
