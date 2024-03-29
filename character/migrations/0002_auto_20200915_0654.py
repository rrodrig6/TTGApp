# Generated by Django 3.1.1 on 2020-09-15 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='age',
            field=models.IntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='character',
            name='arcane_tomes',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='character',
            name='artifacts',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='character',
            name='assets',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='character',
            name='birthplace',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='character',
            name='encounters',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='character',
            name='ideology_and_beliefs',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='character',
            name='injuries_and_scars',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='character',
            name='meaningful_locations',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='character',
            name='notes',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='character',
            name='occupation',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='character',
            name='personal_description',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='character',
            name='phobias_and_manias',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='character',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='character.player'),
        ),
        migrations.AlterField(
            model_name='character',
            name='residence',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='character',
            name='significant_people',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='character',
            name='spells',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='character',
            name='spending_level',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='character',
            name='traits',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='character',
            name='treasured_possessions',
            field=models.CharField(blank=True, max_length=512),
        ),
    ]
