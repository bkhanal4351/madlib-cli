import re


def read_template(file_path):
    with open(file_path, 'r') as file:
        try:
            return file.read().strip()
            print(file.read().strip())
        except FileNotFoundError:
            print("File does not exist")


def parse_template(parsed_file):
    inner_regex = r'{\w*}'
    outer_regex = r'\w{2,}'
    parts = str(re.findall(inner_regex, parsed_file))  # findall creates a list of matches that match regex
    return_parts = tuple(re.findall(outer_regex, parts))  # create tuple and only grab strings within curly
    stripped_string = re.sub(inner_regex, '{}', parsed_file)  # substitute whatever inner_regex grabs with empty curly
    print(return_parts)
    print(stripped_string)

    return stripped_string, return_parts


parse_template('It was a {Adjective} and {Adjective} {Noun}.')  # checking output


def merge(string, user_input):
    merge_output = string.format(*user_input)
    print(merge_output)
    return merge_output


merge("It was a {} and {} {}.", ("dark", "stormy", "night"))  # to test if the output is as expected








