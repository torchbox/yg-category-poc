# Generated by Django 3.2.4 on 2021-06-17 14:45

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_categorypromotedvirtualtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('tracker_id', models.CharField(max_length=255)),
                ('is_promoted', models.BooleanField(blank=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='trackers', to='categories.categorypage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]