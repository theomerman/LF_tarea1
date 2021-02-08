def is_leap(year):
    if 1900 <= year <= 1000000:
        
        leap = False
        if year % 4 == 0:
            
            if year % 100 == 0:
                
                if year % 400 == 0:
                    
                    leap = True
                    return leap

                leap = False
                return leap
            leap = True
            return leap
        
        else:
            return leap