# Generated by Django 2.0.2 on 2018-02-12 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(null=True, upload_to='static/images')),
                ('image2', models.ImageField(null=True, upload_to='static/images')),
                ('image3', models.ImageField(null=True, upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='WorkModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('material_type', models.CharField(choices=[('marble', 'Μάρμαρο'), ('granite', 'Γρανίτης')], max_length=10)),
                ('place_type', models.CharField(choices=[('bath', 'Μπάνιο'), ('out', 'Εξωτερικούς χώρους'), ('cousine', 'Κουζίνες'), ('floor', 'Πάτωμα'), ('fireplace', 'Τζάκια')], max_length=28)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.WorkModel'),
        ),
    ]
