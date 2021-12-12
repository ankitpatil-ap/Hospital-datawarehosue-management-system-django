
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201121_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='symptoms',
        ),
    ]
