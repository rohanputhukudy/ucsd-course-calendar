from bs4 import BeautifulSoup 

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
courses = []
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
        courses.append(curr_course)
        curr_course = []

for c in courses:
    print(c[0][0])
    for row in c:
        print(row)

# Converts 3D course array into an array of course dicts with relevant calendar info
