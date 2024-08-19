from .models import HouseImage

def save_image(offer, image):
    HouseImage.objects.create(offer=offer, image=image)