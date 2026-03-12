import csv
import re
from datetime import datetime

def loader_func(pth):
    # This function works fine, it just uses bad variable names (pth, tmp_lst, f_obj)
    tmp_lst = []
    with open(pth, 'r') as f_obj:
        rdr = csv.DictReader(f_obj)
        for r in rdr:
            tmp_lst.append(r)
    return tmp_lst

def func_alpha_9(v_list):
    """Scrubs the applicant data for the metrics engine."""
    res_arr = []
    
    # BUG 1: The Crash Loop
    # range(len(v_list) + 1) will cause an IndexError at the very end of the list.
    for idx in range(len(v_list) + 1):
        cur_r = v_list[idx]
        
        # --- Email Validation ---
        eml = cur_r['Email']
        
        # BUG 2: The Regex Trap
        # This regex does not allow periods in the prefix. 
        # It will incorrectly drop all valid emails like 'applicant.num_1@email.com'.
        eml_regex = r"^[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
        if not re.match(eml_regex, eml):
            continue 
            
        # --- Date Formatting ---
        dt_str = cur_r['Date_of_Birth']
        
        # BUG 3: The Date Trap
        # Only attempts to parse YYYY-MM-DD. 
        # When it hits an MM-DD-YYYY date from our generator, it will throw a ValueError.
        # Fix: Teams must wrap this in a try-except block to handle both formats.
        dt_obj = datetime.strptime(dt_str, "%Y-%m-%d")
        cur_r['Date_of_Birth'] = dt_obj.strftime("%Y-%m-%d")
        
        # --- Score Cleanup ---
        scr = cur_r['AI_Score']
        
        # BUG 4: The Null Trap
        # Checks for an empty string, but forgets to check for the literal string "null".
        # This allows "null" to pass through, which will crash the math logic later.
        if scr == "":
            continue
            
        res_arr.append(cur_r)
        
    return res_arr