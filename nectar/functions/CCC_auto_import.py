import pandas as pd

def read_ccc_data(start_date, end_date, sid):
    """
    Aims to automate input of Colorado Climate Centre CSVs
    
    Arguments:
        - start_date: MMDDYYYY Target start date. 
        - end_date: MMDDYYYY Target end date
        - sid: Station ID, can be found on CCC website 
    """
    
    # Ensure dates are right length before trying to format 
    if (len(start_date) == 8) and (len(end_date) == 8):
        pass
    else: 
        raise ValueError("Please enter correct date format (MMDDYYYY)")

    # Format input dates in the way needed for URL
    month_s = start_date[0:2]
    if month_s[0] == "0":
        month_s = month_s[1] #URLS do not include the 0 in months like 03 / march
    day_s = start_date[2:4]
    if day_s[0] == "0":
        day_s = day_s[1] #URLS do not include the 0 in days like 03
    year_s = start_date[4::]
    sdate = year_s + "-" + month_s + "-" + day_s

    month_e = end_date[0:2]
    if month_e[0] == "0":
        month_e = month_e[1] #URLS do not include the 0 in months like 03 / march
    day_e = end_date[2:4]
    if day_e[0] == "0":
        day_e = day_e[1] #URLS do not include the 0 in days like 03
    year_e = end_date[4::]
    edate = year_e + "-" + month_e + "-" + day_e

    # Input link using start and end dates
    url = "https://data.rcc-acis.org/StnData?sid="+sid+"&sdate="+sdate+"&edate="+edate+"&elems=1,2,4,10&output=csv"
    print(f"Trying to import from: {url}")
    df_c = pd.read_csv(url)

    return df_c


# Verification: 
if __name__ == "__main__":

    df_c = read_ccc_data("03032024", "11292025", "050848")
    print(f"{df_c}")