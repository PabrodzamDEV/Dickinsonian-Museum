# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

from Museum.models import GalleryPiece, Essay


@receiver(pre_delete, sender=GalleryPiece)
def gallery_piece_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.piece.delete(False)


@receiver(pre_delete, sender=Essay)
def essay_delete(sender, instance, **kwargs):
    instance.file.delete(False)
