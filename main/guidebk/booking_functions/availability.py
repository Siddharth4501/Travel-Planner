import datetime
from guidebk.models import Guide,Gd_booking

def check_availability(guide, bk_start_date, bk_end_date):
    avail_list=[]
    booking_list=Gd_booking.objects.filter(guide=guide)
    
    if booking_list is not None:
        for booking in booking_list:
            
            if booking.bk_start_date > bk_end_date or booking.bk_end_date < bk_start_date:
                # if booking.guide_book_active_status:
                #     pass
                # else:
                avail_list.append(True)
            else:
                avail_list.append(False)
        
    else:
        avail_list.append(False)
    
    return all(avail_list)
    