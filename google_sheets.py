import gspread

sa = gspread.service_account()

def process_mentee_csv():
    mentee_csv = sa.open("Mentee Intake (Responses)")
    registered_mentees = set()

    # This is the name of a given worksheet. This normally defaults to Form 1 or similar syntax.
    form_worksheet = mentee_csv.worksheet('Form Responses 1')
    mentee_data = form_worksheet.get_all_records()
    for mentee_datum in mentee_data:
        registered_mentees.add(mentee_datum['Email?'])

    return registered_mentees

def process_mentor_csv():
    mentor_csv = sa.open("Mentor Intake (Responses)")
    registered_mentors = set()

    # This is the name of a given worksheet. This normally defaults to Form 1 or similar syntax.
    form_worksheet = mentor_csv.worksheet('Form Responses 1')
    mentor_data = form_worksheet.get_all_records()
    for mentor_datum in mentor_data:
        registered_mentors.add(mentor_datum['Email'])

    return registered_mentors



"""
wks.row_count -> Int

-- READ --
wks.acell(string).value -> String
wks.cell(Int, Int).value -> String

wks.get(Range*) -> [[String]]

wks.get_all_records() -> [{Header:Value}]
wks.get_all_values() -> [[Values]]

*Range is a selection of Spreadsheet values, for example A7 - E9 will return 12 individual cells
for example wks.get('A7:E9')

-- WRITE -- 

wks.update(cell, value)
ex. update('A3', 'Anthony')

wks.update(Range)

 -- META -- 

 pass the param `raw = False` to create spreadsheet functions
 wks.update('F2', '=UPPER(E2)', raw=False)

""" 