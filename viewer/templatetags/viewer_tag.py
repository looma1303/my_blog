from django import template
from write.models import Write, Photo
import pickle

register = template.Library()

@register.simple_tag(takes_context=True)
def write(context,write_id):
    write = Write.objects.get(id=write_id)

    target_write = write.things
    target_write = target_write.split('///')

    return target_write






@register.simple_tag(takes_context=True)

def photo(context, write_id):
    photo = Photo.objects.filter(write_id=write_id)


    with open('counter_result.pickle','rb') as fr:
        load_count = pickle.load(fr)
    now_counter = 0


    for x in photo:


        now_counter = now_counter + 1

        if now_counter == load_count:
            result = x
            with open('counter_result.pickle','wb') as fw:
                pickle.dump(now_counter+1, fw)
            if load_count == counter(write_id):
                with open('counter_result.pickle', 'wb') as fw:
                    pickle.dump(1, fw)
        else:
            pass

    return result

@register.simple_tag(takes_context=True)
def title_giver(context,write_id):

    write = Write.objects.get(id=write_id)


    return write.title











def counter(write_id):

    img_count = 0

    write = Write.objects.get(id=write_id)
    target_write = write.things
    target_write = target_write.split('///')


    for x in target_write:
        if x == '@img':
            img_count = img_count + 1
        else:
            pass

    return img_count
