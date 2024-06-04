file_path = 'dropdown.txt'

with open(file_path, 'r') as file:
    content = file.read()


from bs4 import BeautifulSoup, NavigableString

# Assuming 'content' is your HTML string
soup = BeautifulSoup(content, 'html.parser')

# Find all 'a' tags with class 'dropdown-item'
dropdown_items = soup.find_all('a', class_='dropdown-item')

# Extract the text from the 'a' tag and the 'small' tag within it
result = []
cleared = []
for item in dropdown_items:
    a_text = next(item.children).strip() if isinstance(next(item.children), NavigableString) else ''
    small_text = item.small.get_text(strip=True) if item.small else ''
    result.append(f"{a_text} {small_text}")
    cleared.append(a_text)

print(result)

with open('domains.txt', 'w') as file:
    for item in result:
        file.write(item + '\n')

with open('domains-only.txt', 'w') as file:
    for item in cleared:
        file.write(item + '\n')