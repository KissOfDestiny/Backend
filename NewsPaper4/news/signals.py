from django.db.models.signals import post_save
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import mail_admins, send_mail
from .models import Post, Category
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и в отправители надо передать также модель
@receiver(post_save, sender=Post)
def notify_subs_post(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.title} {instance.dateCreation.strftime("%d %m %Y")}'
    else:
        subject = f'Post {instance.title},{instance.dateCreation.strftime("%d %m %Y")},was changed.'

    subscribers = instance.postCategory.subscribers.all()
    address = []
    for each in subscribers:
        address.append(each.email)
    html_content = render_to_string(
        'created.html',
        {
            'post': instance.text,
        }
    )
    body = f'Здравствуй! Новая статья в твоем любимом разделе {instance.postCategory}! {instance.text[:50]}...'
    msg = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email='wholespam@yandex.ru',
        to=[*address],
    )
    msg.attach_alternative(html_content, "text/html")  # добавляем html
    msg.send()
    #send_mail(
        #subject=subject,
        #message=f'{instance.text[:30]}...',
        #from_email='wholespam@yandex.ru',
        #recipient_list=address
    #)
