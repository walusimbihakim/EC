# Generated by Django 4.1.3 on 2022-11-21 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_vote', '0004_alter_candidate_gender_alter_voter_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='positionid',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='e_vote.position'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='votes',
            name='candidated_voted',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='e_vote.candidate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='votes',
            name='position_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='e_vote.position'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='votes',
            name='voter_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='e_vote.voter'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='address',
            field=models.CharField(blank=True, default='N/A', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='contact',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='position',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
