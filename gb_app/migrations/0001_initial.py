# Generated by Django 3.2.9 on 2021-12-03 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GreatBuilding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(choices=[('No Age', 'No Age'), ('Stone Age', 'Stone Age'), ('Bronze Age', 'Bronze Age'), ('Iron Age', 'Iron Age'), ('Early Middle Age', 'Early Middle Age'), ('High Middle Age', 'High Middle Age'), ('Late Middle Age', 'Late Middle Age'), ('Colonial Age', 'Colonial Age'), ('Industrial Age', 'Industrial Age'), ('Progressive Era', 'Progressive Era'), ('Modern Era', 'Modern Era'), ('Postmodern Era', 'Postmodern Era'), ('Contemporary Era', 'Contemporary Era'), ('Tomorrow Era', 'Tomorrow Era'), ('Future Era', 'Future Era'), ('Arctic Future', 'Arctic Future'), ('Oceanic Future', 'Oceanic Future'), ('Virtual Future', 'Virtual Future'), ('Space Age Mars', 'Space Age Mars'), ('Space Age Asteroid Belt', 'Space Age Asteroid Belt'), ('Space Age Venus', 'Space Age Venus')], max_length=30)),
                ('level', models.IntegerField(default=0)),
                ('p1', models.IntegerField(default=0)),
                ('p2', models.IntegerField(default=0)),
                ('p3', models.IntegerField(default=0)),
                ('p4', models.IntegerField(default=0)),
                ('p5', models.IntegerField(default=0)),
            ],
        ),
    ]
