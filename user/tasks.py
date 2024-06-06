from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from user.models import PhoneCode


@shared_task
def delete_phone_code_verification(pk, code):

    instance1 = PeriodicTask.objects.filter(
        name__startswith=f"Delete_UserPhoneCode_{code}"
    )
    for task in instance1:
        task.delete()

    instance2 = PhoneCode.objects.filter(code=code)
    for task in instance2:
        task.delete()
