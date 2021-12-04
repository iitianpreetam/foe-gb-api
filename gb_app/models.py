from django.db import models

class GreatBuilding(models.Model):
    AGE_CHOICES = (
        ('No Age', 'No Age'),
        ('Stone Age', 'Stone Age'),
        ('Bronze Age', 'Bronze Age'),
        ('Iron Age', 'Iron Age'),
        ('Early Middle Age', 'Early Middle Age'),
        ('High Middle Age', 'High Middle Age'),
        ('Late Middle Age', 'Late Middle Age'),
        ('Colonial Age', 'Colonial Age'),
        ('Industrial Age', 'Industrial Age'),
        ('Progressive Era', 'Progressive Era'),
        ('Modern Era', 'Modern Era'),
        ('Postmodern Era', 'Postmodern Era'),
        ('Contemporary Era', 'Contemporary Era'),
        ('Tomorrow Era', 'Tomorrow Era'),
        ('Future Era', 'Future Era'),
        ('Arctic Future', 'Arctic Future'),
        ('Oceanic Future', 'Oceanic Future'),
        ('Virtual Future', 'Virtual Future'),
        ('Space Age Mars', 'Space Age Mars'),
        ('Space Age Asteroid Belt', 'Space Age Asteroid Belt'),
        ('Space Age Venus', 'Space Age Venus'),
    )
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=30, choices=AGE_CHOICES)

    def __str__(self):
        return self.name

class GBLevel(models.Model):
    gb = models.ForeignKey(GreatBuilding, related_name='gb_level', on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    p1 = models.IntegerField(default=0)
    p2 = models.IntegerField(default=0)
    p3 = models.IntegerField(default=0)
    p4 = models.IntegerField(default=0)
    p5 = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.gb.name} - #{self.level}'