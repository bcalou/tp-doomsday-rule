def is_leap_year(year : int) :
    return ((year%4 == 0 and year%100!=0) or (year%100==0 and year%400==0))