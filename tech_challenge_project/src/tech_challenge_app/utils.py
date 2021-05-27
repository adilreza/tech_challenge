
import json
import requests

# imported model 
from .models import Notice, Record
from .models import Match

# algo function 

def strong_match_fun(first_name, last_name, date_of_birth):
    return_result = 0

    return_result = Notice.objects.filter(first_name=first_name).filter(last_name=last_name).filter(dat_of_birth=date_of_birth).count()
    if return_result==0:
        return_result = Notice.objects.filter(alt_first_name=first_name).filter(alt_last_name=last_name).filter( dat_of_birth=date_of_birth).count()

    return return_result;

def possible_match_fun(first_name, last_name, province):
    return_result = 0
    return_result = Notice.objects.filter(first_name=first_name, last_name=last_name, province=province).count()
    if return_result==0:
        return_result = Notice.objects.filter(alt_first_name=first_name).filter(alt_last_name=last_name).filter(province=province).count()
    return return_result

def weak_match_fun(first_name, last_name):
    return_result = 0
    return_result = Notice.objects.filter(first_name=first_name).filter(last_name=last_name).count()
    if return_result==0:
        return_result = Notice.objects.filter(alt_first_name=first_name).filter(alt_last_name=last_name).count()
    return return_result;


def decision_maker(first_name, last_name, province, date_of_birth):
    flag = 0
    if date_of_birth!="0000-00-00":
        print("start strong ------------")
        result = strong_match_fun(first_name, last_name, date_of_birth)
        # for strong 1
        flag=1
    elif province!="NOT":
        print("start possible ------------")
        result = possible_match_fun(first_name, last_name, province)
        # for possible 2
        flag = 2
        
    elif date_of_birth=="0000-00-00" and province=="NOT":
        print("start weak ------------")
        result = weak_match_fun(first_name, last_name)
        # for weak
        flag = 3
    
    return flag
        

def update_match_now(decision, first_name, last_name, province, date_of_birth):

    if decision==1:
        notice_cnt1 = Notice.objects.filter(first_name=first_name, last_name=last_name, dat_of_birth=date_of_birth).count()
        if notice_cnt1!=0:
            notice1 = Notice.objects.get(first_name=first_name, last_name=last_name, dat_of_birth=date_of_birth)
        else:
            notice1 = Notice.objects.get(alt_first_name=first_name, alt_last_name=last_name, dat_of_birth=date_of_birth)

        if province=="NOT":
            record1 = Record.objects.create(first_name=first_name, last_name=last_name, dat_of_birth=date_of_birth)
            final1 = Match.objects.create(notice=notice1, record=record1, type=1)
        else:
            record1 = Record.objects.create(first_name=first_name, last_name=last_name, province=province, dat_of_birth=date_of_birth)
            final1 = Match.objects.create(notice=notice1, record=record1, type=1)
    
    elif decision==2:
        print("start possible insert-------------")
        notice_cnt2 = Notice.objects.filter(first_name=first_name, last_name=last_name, province=province).count()
        if notice_cnt2!=0:
            notice2 = Notice.objects.get(first_name=first_name, last_name=last_name, province=province)
        else:
            notice2 = Notice.objects.get(alt_first_name=first_name, alt_last_name=last_name, province=province)

        if date_of_birth=="0000-00-00":
            record2 = Record.objects.create(first_name=first_name, last_name=last_name, province=province)
            final2 = Match.objects.create(notice=notice2, record=record2, type=2)
        else:
            record2 = Record.objects.create(first_name=first_name, last_name=last_name, province=province, dat_of_birth=date_of_birth)
    
    elif decision==3:
        notice_cnt = Notice.objects.filter(first_name=first_name, last_name=last_name).count()
        if notice_cnt!=0:
            notice3 = Notice.objects.get(first_name=first_name, last_name=last_name)
        else:
            notice3 = Notice.objects.get(alt_first_name=first_name, alt_last_name=last_name)


        if date_of_birth=="0000-00-00" and province=="NOT":
            record3 = Record.objects.create(first_name=first_name, last_name=last_name)
            final3 = Match.objects.create(notice=notice3, record=record3, type=3)
        else:
            record3 = Record.objects.create(first_name=first_name, last_name=last_name, province=province, dat_of_birth=date_of_birth)
            final3 = Match.objects.create(notice=notice3, record=record3, type=3)

    return "ok"


