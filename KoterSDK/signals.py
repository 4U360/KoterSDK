import django.dispatch

pre_receive_hook = django.dispatch.Signal()
post_receive_hook = django.dispatch.Signal()
