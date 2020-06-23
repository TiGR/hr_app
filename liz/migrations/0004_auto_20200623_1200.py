# Generated by Django 3.0.7 on 2020-06-23 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liz', '0003_auto_20200623_1044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': '1) Сотрудник', 'verbose_name_plural': '1) Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='employeeanswer',
            options={'verbose_name': '5) Ответы сотрудника', 'verbose_name_plural': '5) Ответы сотрудников'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '2) Вопрос', 'verbose_name_plural': '2) Вопросы'},
        ),
        migrations.AlterModelOptions(
            name='questionnaire',
            options={'verbose_name': '3) Опросник', 'verbose_name_plural': '3) Опросники'},
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='users',
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='questions',
            field=models.ManyToManyField(to='liz.Question', verbose_name='Вопросы в текущем опроснике'),
        ),
        migrations.CreateModel(
            name='ApointmentTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.ManyToManyField(blank=True, to='liz.Questionnaire', verbose_name='Опросники открытые для отрудников')),
            ],
            options={
                'verbose_name': '4) Опросники открытые',
                'verbose_name_plural': '4) Опросники открытые',
            },
        ),
    ]
