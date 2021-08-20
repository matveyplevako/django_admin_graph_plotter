# Generated by Django 3.2.6 on 2021-08-20 15:11

from django.db import migrations, models
import graphs.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function_text', models.CharField(max_length=255, verbose_name='Функция')),
                ('graph', models.ImageField(blank=True, null=True, storage=graphs.storage.OverwriteStorage(), upload_to='graphs/')),
                ('error', models.CharField(blank=True, max_length=1024, null=True)),
                ('interval_days', models.IntegerField(verbose_name='Интервал t, дней')),
                ('step_hours', models.IntegerField(verbose_name='Шаг t, часы')),
                ('process_time', models.DateTimeField(blank=True, null=True, verbose_name='Дата обработки')),
            ],
        ),
    ]