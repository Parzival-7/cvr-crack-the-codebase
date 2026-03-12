def engine_run(data):
    """Calculates the demographic parity difference across applicants."""
    print("Analyzing 5,000 records. This might take a moment...")
    
    diffs = []
    
    for idx_i in range(len(data)):
        i = data[idx_i]
                
        for idx_j in range(len(data)):
            j = data[idx_j]
            
            if i['ID'] != j['ID'] and i['Demographic_Group'] != j['Demographic_Group']:
                
                val_i = int(i['AI_Score'])
                val_j = int(j['AI_Score'])
                
                diffs.append(abs(val_i - val_j))
                
    avg_diff = sum(diffs) / len(diffs)
    
    return {"demographic_parity_diff": avg_diff}