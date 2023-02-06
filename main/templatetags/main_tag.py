from django import template

from write.models import Write, Photo

import pickle

register = template.Library()

@register.simple_tag

def preview_write():
    write = Write.objects.all()
    result = write
    return result

@register.simple_tag(takes_context=True)


def preview_photo(context, write_id):
    photo = Photo.objects.filter(write_id=write_id)

    for x in photo:
        photo = x
        break

    photo_count = Photo.objects.filter(write_id=write_id).count()
    if photo_count == 0:
        photo = 'NO_IMG'
    else:
        pass


    return photo








'''

html파일에서 {%%}에 쓰면되지만 {{에 쓰면 작동하지 않음.}}
@register.simple_tag

def preview_things():

    write = Write.objects.all()
    for x in write:
        result = x.things
    return result




    for x in write:
        for y in photo:
            if x.id == y.id:
                #images = []
                image = ''
                for z in photo.image:
                    image = image +' '+ z
                #result.append([x.title,x.things,images])
                result = result + x.title + ' ' + ' ' + x.things + ' ' + image + '!@!' + ' '
'''
    #return result
