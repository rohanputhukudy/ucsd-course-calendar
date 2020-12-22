from bs4 import BeautifulSoup 

with open('webregMain.html', 'r') as fi:
    htmltext = fi.read()

soup = BeautifulSoup(htmltext, 'lxml')
n = 0
rows = soup.find_all(class_='ui-widget-content jqgrow ui-row-ltr wr-grid-en')
missing_row = soup.find(class_='ui-widget-content jqgrow ui-row-ltr wr-grid-en ui-state-hover')
rows.insert(int(missing_row['id']), missing_row)

for r in rows:
    print(r['id'])

for row in rows:
    # This happens when the current row is part of the finals table on the calendar tab of the website
    if int(row['id']) != n:
        print(f'n={n}, id={row["id"]}')
        break

    # Every class has 3 rows corresponding to it
    # This is actually not true, MATH 95 has no discussion so there is only 2 rows
    if n%3 == 0:
        print(f'\nClass {int(n/3)}:', end='')

    # Prints out all the text in each row
    for cell in row.findChildren(recursive=False):
        if cell['style'] != 'display:none;' and cell.text.strip() != '':
            print(cell.text.strip(), end=' ')

    print()
    n += 1
