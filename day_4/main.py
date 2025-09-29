def main():
    import math

    strings_1 = ['Thirty', 'Days', 'Of', 'Python']
    print(" ".join(strings_1))

    strings_2 = ['Coding', 'For', 'All']
    print(" ".join(strings_2))

    company = 'Coding For All'
    upper_company = company.upper()
    lower_company = company.lower()
    capitalize_company = company.capitalize()
    title_company = company.title()
    swapcase_company = company.swapcase()

    print(company, upper_company, lower_company, capitalize_company, title_company, swapcase_company, sep="\n")

    company_words = company.split(" ")
    print(company_words[0])
    print(company.find('Coding'))

    replace_company = company.replace('Coding', 'Python')
    print(replace_company)
    print("Python for Everyone".replace('Everyone', 'All'))

    companies = "Facebook, Google, Microsoft, IBM, Oracle, Amazon".split(', ')
    print(companies)

    print(company[0])
    print(len(company)-1)
    print(company[10])

    string = 'Python For Everyone'
    strings_3 = string.split(" ")
    for str in strings_3:
        print(str[0], end='')
    print('')
    
    for word in company_words:
        print(word[0],end='')
    print('')

    print(company.index('C'))
    print(company.index('F'))
    print(company.rfind('l'))

    long_sentence = 'You cannot end a sentance with because because because is a conjunction'
    print(long_sentence.find('because'))
    print(long_sentence.rindex('because'))
    sliced_long_sentence = long_sentence[long_sentence.find('because'):long_sentence.find('because')+3*len('because')+2]
    print(sliced_long_sentence)

    do_start_with_coding = company.startswith('Coding')
    do_end_with_coding = company.endswith('coding')

    if do_start_with_coding:
        print("Yes, string starts with \'Coding\'")
    if not do_end_with_coding:
        print("Yes, string ends with \'coding\'")

    print('   Coding For All   '.strip())

    print('30DaysOfPython'.isidentifier())
    print('thirty_days_of_python'.isidentifier())

    library_string = " #".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'])
    print(library_string)
    print('I am anjoying this callenge.\nI just wonder what is next.')
    print('''Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\t Helsinki''')

    radius = 10
    area = math.pi * radius ** 2
    print("The area of circle with radius {} is {} meters square".format(radius, area))

    a = 8 
    b = 6

    total = a + b
    diff = a - b
    product = a * b
    division = a / b
    modulo = a % b
    floor_division = a // b
    exp = a ** b
    print(f'''
{a} + {b} = {total}
{a} - {b} = {diff}
{a} * {b} = {product}
{a} / {b} = {division:.2f}
{a} % {b} = {modulo}
{a} // {b} = {floor_division}
{a} ** {b} = {exp}
''')

if __name__ == '__main__':
    main()