# Generated by Django 3.2.9 on 2022-01-04 05:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offices', '0001_initial'),
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('serv_id', models.CharField(default='---', max_length=255, unique=True)),
                ('core_serv_id', models.CharField(max_length=255, unique=True)),
                ('core_items_serial', models.CharField(max_length=255)),
                ('opt_serv_id', models.CharField(blank=True, max_length=255, null=True)),
                ('opt_items_serial', models.CharField(max_length=255)),
                ('ver', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='offices.area', to_field='code')),
                ('serv_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='words.service_name', to_field='phrase')),
            ],
        ),
        migrations.CreateModel(
            name='Used_Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_num', models.IntegerField()),
                ('resident_num', models.CharField(blank=True, max_length=12, null=True)),
                ('used_serv_item_ids', models.CharField(max_length=255)),
                ('send_vals', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('my_num_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='res_my_num_id', to='offices.resident', to_field='my_num_id')),
                ('serv_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='stock_serv_id', to='peace_keeping.service_stock', to_field='serv_id')),
            ],
        ),
    ]
