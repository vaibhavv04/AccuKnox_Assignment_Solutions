import django
from django.conf import settings
from django.db import models, transaction, connection
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

# Configure Django settings for standalone script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", __name__)
settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',  # In-memory SQLite database for simplicity
        }
    }
)
django.setup()

# Define a simple model
class User(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'myapp'

# Define another model to be modified by the signal receiver
class Log(models.Model):
    message = models.CharField(max_length=200)

    class Meta:
        app_label = 'myapp'

# Signal receiver that creates a Log entry when a User is saved
@receiver(post_save, sender=User)
def log_user_creation(sender, instance, **kwargs):
    print("Receiver: Creating Log entry")
    Log.objects.create(message=f"User {instance.name} created")
    print("Receiver: Log entry created")

# Function to test transaction behavior
def test_signal_transaction():
    # Create database tables
    with connection.schema_editor() as schema_editor:
        schema_editor.create_model(User)
        schema_editor.create_model(Log)

    print("Starting transaction")
    try:
        with transaction.atomic():  # Start a transaction
            print("Creating User")
            user = User.objects.create(name="Alice")  # Triggers post_save signal
            print("User created, checking Log count")
            log_count = Log.objects.count()
            print(f"Log count: {log_count}")
            print("Raising exception to rollback transaction")
            raise Exception("Force rollback")  # Force transaction rollback
    except Exception as e:
        print(f"Exception caught: {e}")

    print("After rollback, checking User and Log counts")
    user_count = User.objects.count()
    log_count = Log.objects.count()
    print(f"User count: {user_count}, Log count: {log_count}")

# Run the test
if __name__ == "__main__":
    test_signal_transaction()
