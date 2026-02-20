from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ForumBlock', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-created_at']},
        ),
    ]
