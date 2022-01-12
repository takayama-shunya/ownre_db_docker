# Generated by Django 3.2.9 on 2022-01-04 05:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raw_Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_in_paper', models.CharField(max_length=32)),
                ('serv_id', models.CharField(max_length=255, unique=True)),
                ('serv_name', models.CharField(max_length=32)),
                ('items_in_paper_serial', models.CharField(max_length=255)),
                ('items_order_by_serv_item_serial', models.CharField(max_length=255)),
                ('items_order_by_serv_item_id_serial', models.CharField(max_length=255)),
                ('core_serv_id', models.CharField(max_length=255, unique=True)),
                ('core_items_serial', models.CharField(max_length=255)),
                ('core_items_not_in_paper_serial', models.CharField(blank=True, max_length=255, null=True)),
                ('opt_serv_id', models.CharField(blank=True, max_length=255, null=True)),
                ('opt_items_serial', models.CharField(blank=True, max_length=255, null=True)),
                ('original_file_path', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('area', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='offices.area', to_field='code')),
            ],
        ),
        migrations.CreateModel(
            name='Archived_Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('serv_name', models.CharField(max_length=255)),
                ('core_serv_id', models.CharField(max_length=255)),
                ('core_items_serial', models.CharField(max_length=255)),
                ('opt_serv_id', models.CharField(blank=True, max_length=255, null=True)),
                ('opt_items_serial', models.CharField(blank=True, max_length=255, null=True)),
                ('inputs_in_paper_serial', models.CharField(max_length=255)),
                ('original_file_path', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('area_id', models.ForeignKey(default=901000, on_delete=django.db.models.deletion.CASCADE, to='offices.area', to_field='code')),
                ('serv_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_serv_id', to='restore_order.raw_item', to_field='serv_id')),
            ],
        ),
        migrations.AddConstraint(
            model_name='raw_item',
            constraint=models.UniqueConstraint(fields=('area', 'serv_id'), name='unique_serv_id_in_small_area'),
        ),
    ]