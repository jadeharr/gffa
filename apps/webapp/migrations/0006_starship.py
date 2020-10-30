# Generated by Django 3.1.2 on 2020-10-07 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20200806_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Starship',
            fields=[
                ('starship_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('starship_class', models.CharField(blank=True, max_length=40, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=40, null=True)),
                ('cost_in_credits', models.CharField(blank=True, max_length=40, null=True)),
                ('length', models.CharField(blank=True, max_length=40, null=True)),
                ('crew', models.CharField(blank=True, max_length=40, null=True)),
                ('passengers', models.CharField(blank=True, max_length=40, null=True)),
                ('max_atmosphering_speed', models.CharField(blank=True, max_length=40, null=True)),
                ('hyperdrive_rating', models.CharField(blank=True, max_length=40, null=True)),
                ('MGLT', models.CharField(blank=True, max_length=40, null=True)),
                ('cargo_capacity', models.CharField(blank=True, max_length=40, null=True)),
                ('consumables', models.CharField(blank=True, max_length=40, null=True)),
                ('pilots', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='starship_person', to='webapp.person')),
            ],
            options={
                'verbose_name': 'Starship',
                'verbose_name_plural': 'Starships',
                'db_table': 'starships',
                'ordering': ['name'],
                'managed': True,
            },
        ),
    ]