# Generated by Django 3.2.9 on 2021-11-11 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('create_vote', '0025_alter_sendformtable_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sendformtable',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='sendformtable',
            name='group',
        ),
        migrations.RemoveField(
            model_name='sendformtable',
            name='question',
        ),
        migrations.CreateModel(
            name='SendAnswerTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='create_vote.groupstable')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='create_vote.questiontable')),
            ],
        ),
        migrations.AddField(
            model_name='sendformtable',
            name='answers',
            field=models.ManyToManyField(to='create_vote.SendAnswerTable'),
        ),
    ]
