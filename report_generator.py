
def write_output(metrics_dict):
    """Writes the final analytics dictionary to a text file for HR."""
    out_file = open("hr_report.txt", "w")
    out_file.write(metrics_dict)
    print("Report saved to hr_report.txt successfully!")