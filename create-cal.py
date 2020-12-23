from bs4 import BeautifulSoup
from ics import Calendar, Event

def extract_course_info():
    with open('webregMain.html', 'r') as fi:
        htmltext = fi.read()

    soup = BeautifulSoup(htmltext, 'lxml')

    # Extracts rows of tables from html
    # This gets us rows from two different tables, however we only want the first table
    rows = soup.find_all(class_='ui-widget-content jqgrow ui-row-ltr wr-grid-en')
    missing_row = soup.find(class_='ui-widget-content jqgrow ui-row-ltr wr-grid-en ui-state-hover')
    if missing_row:
        rows.insert(int(missing_row['id']), missing_row)

    # Finds point where second table starts and slices our array
    i = 0
    while int(rows[i]['id']) == i:
        i += 1
    table = rows[:i]

    # Populates array of courses where each course consists of 3 row vectors
    courses_array = []
    curr_course = []
    for row in table:

        # Converts row into an array of cell data
        course_row = []
        for cell in row.findChildren(recursive=False):
            if cell['style'] != 'display:none;' and cell.text.strip() != '':
                course_row.append(cell.text.strip())

        # Adds row to the current course
        curr_course.append(course_row)

        # When reached the last row corresponding to the current course, adds course to list of courses
        if course_row[0] == 'Final Exam':
            courses_array.append(curr_course)
            curr_course = []

    for c in courses_array:
        print(c[0][0])
        for row in c:
            print(row)

    # Converts 3D course array into an array of course dicts with relevant calendar info
    courses = []
    for c in courses_array:
        course = {
            'name': '',
            'lecture': {},
            'discussion': {},
            'final': {},
        }
        for row in c:
            # Row corresponds to discussion info
            if row[1] = 'DI':
                course['dicussion']['day'] = row[2]
                course['dicussion']['time'] = row[3]

            # Row corresponds to final info
            elif row[0] == 'Final Exam':
                course['final']['date'] = row[2]
                course['final']['time'] = row[3]

            # Row corresponds to lecture info
            else:
                course['name'] = row[0]
                course['lecture']['days'] = row[7]
                course['lecture']['time'] = row[8]

        courses.append(course)
    return courses

def create_cal(courses, startdate):
    cal = Calendar()
    for c in courses:
        for day in c['lecture']['days']:
            timedate = 
