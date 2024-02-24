config = { # Only include rows that have these values.
    "email_first": False,
    "email_second": False,
    "phone": True,
    "company_phone": True,
    "first_name": True,
    "middle_name": False,
    "last_name": False,
    "url": False,
    "job_title": False,
    "company_name": False,
    "company_domain": False,
    "company_id": False,
    "city": False,
    "linkedin_id": False,
    "created_date": False,
    "list_name": False,
}

phone_filter_include = [] # Only includes numbers which are specified here. For example: ["+33", "(8"]
phone_filter_exclude = ["04"] # Excludes all numbers beginning with string. For example: ["+33", "(8"]

input_folder = "input"
output_folder = "output"