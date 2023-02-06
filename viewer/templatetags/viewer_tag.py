from django import template
from write.models import Write, Photo
import pickle

register = template.Library()

@register.simple_tag(takes_context=True)
def write(context,write_id):
    #write_id = a
    #print(write_id, context)
    write = Write.objects.get(id=write_id)

    target_write = write.things
    target_write = target_write.split('///')
    #print(type(target_write))
    return target_write

    #print(write.pub_date)





@register.simple_tag(takes_context=True)

def photo(context, write_id):
    photo = Photo.objects.filter(write_id=write_id)
    #print(photo)
    #print(photo.title)

    with open('counter_result.pickle','rb') as fr: #지금 이 호출이 몇번째 호출인지 알아보기
        load_count = pickle.load(fr)
    now_counter = 0
    #print(load_count, now_counter)

    for x in photo:

        #print()
        now_counter = now_counter + 1
        #print(now_counter, load_count)
        if now_counter == load_count:
            result = x
            with open('counter_result.pickle','wb') as fw: #다음 찾을 사진이 몇번째일지 저장해놓기
                pickle.dump(now_counter+1, fw)
            if load_count == counter(write_id): #만약 지금이 마지막 사진이라면
                with open('counter_result.pickle', 'wb') as fw:
                    pickle.dump(1, fw)
        else:
            pass

    return result

@register.simple_tag(takes_context=True)
def title_giver(context,write_id):
    #write_id = a
    #print(write_id, context)
    write = Write.objects.get(id=write_id)

    #target_write = write.things
    #target_write = target_write.split('///')
    #print(type(target_write))
    return write.title

    #print(write.pub_date)








#TODO:카운터를 태그 말고 그냥 함수로 만들어서 photo에서 호출하면 img_count리턴해주도록 바꾸기
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
