from .views import *
from .models import *

def count(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct=cartlist.objects.filter(cart_id=c_id(request))
            cti=items.objects.all().filter(cart=ct[:1])
            for i in cti:
                item_count += i.quan
        except cartlist.DoesNotExist:
            item_count=0
        return dict(itc=item_count)