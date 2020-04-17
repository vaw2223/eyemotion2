# Generated by Django 2.1.2 on 2020-04-12 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200412_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='unit_price',
            field=models.IntegerField(blank=True, choices=[(1, '40円'), (2, '36円'), (3, '32円')], default=1, verbose_name='単価(権利取得日)'),
        ),
        migrations.AlterField(
            model_name='item',
            name='operation_period',
            field=models.IntegerField(blank=True, choices=[(1, '01年'), (2, '02年'), (3, '03年'), (4, '04年'), (5, '05年'), (6, '06年'), (7, '07年'), (8, '08年'), (9, '09年'), (10, '10年'), (11, '11年'), (12, '12年'), (13, '13年'), (14, '14年'), (15, '15年'), (16, '16年'), (17, '17年'), (18, '18年'), (19, '19年'), (20, '20年'), (21, '21年'), (22, '22年'), (23, '23年'), (24, '24年'), (25, '25年'), (26, '26年'), (27, '27年'), (28, '28年'), (29, '29年'), (30, '30年')], default=1, verbose_name='稼働年数'),
        ),
        migrations.AlterField(
            model_name='item',
            name='site_area',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='敷地面積/㎡'),
        ),
    ]
