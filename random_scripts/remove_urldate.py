import re

def remove_urldate_except_misc(input_file):
    """
    Removes the 'urldate' field from all entries except those of type '@misc' in a .bib file.

    Args:
        input_file (str): Path to the .bib file to modify.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    output_lines = []
    inside_misc_entry = False

    for line in lines:
        # Check if the line starts a new entry
        entry_match = re.match(r'@([a-zA-Z]+)\{', line)
        if entry_match:
            print(f"Found entry type: {entry_match.group(1)}")
            entry_type = entry_match.group(1).lower()
            inside_misc_entry = (entry_type == 'misc')

        # Remove 'urldate' if not inside a @misc entry
        if not inside_misc_entry and re.match(r'\s*urldate\s*=\s*\{.*\},?', line):
            print(f"Removing urldate line: {line.strip()}")
            continue

        output_lines.append(line)

    # Overwrite the input file with the modified lines
    with open(input_file, 'w', encoding='utf-8') as file:
        file.writelines(output_lines)

input_bib_file = r"C:\Users\jupf0\Desktop\MasterThesis\MasterThesis\literature.bib"
remove_urldate_except_misc(input_bib_file)
