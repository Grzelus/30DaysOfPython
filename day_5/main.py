def main():
    #LEVEL 1 ===============
    # array = list()
    # array = []
    # array = [1,2,3,4,5]
    array_with_range = list(range(1,11))
    
    print(array_with_range, len(array_with_range))

    print(array_with_range[0], array_with_range[len(array_with_range)//2], array_with_range[-1])

    mixed_data_types = ['Kacper', 21, 1.74, True, {'city': 'Jarocin', 'street': 'Os. Stefana Batorego'}]
    it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
    print(it_companies, len(it_companies))
    print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])
    it_companies[0] = 'Meta'
    print(it_companies)
    it_companies.append('Nvidia')
    it_companies.insert(1, 'Samsung')
    it_companies[0] = it_companies[0].upper()
    joined_it_companies = '#; '.join(it_companies)
    print(joined_it_companies)
    print('META' in it_companies)
    it_companies.sort()
    it_companies.reverse()
    print(it_companies[:3])
    print(it_companies[-3:])
    print(it_companies[len(it_companies)//2:len(it_companies)//2+1])
    del it_companies[0]
    del it_companies[len(it_companies)//2]
    del it_companies[-1]
    it_companies.clear()
    del it_companies

    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node', 'Express', 'MongoDB']
    web_development = front_end + back_end
    print(web_development)
    full_stack = web_development.copy()
    index = full_stack.index('Redux') + 1
    full_stack[index:index] = ['Python', 'SQL']
    print(full_stack)

    #LEVEL 2 ===============

    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    ages.sort()
    min_age, max_age = ages[0], ages[len(ages)-1]
    print(min_age, max_age)
    ages.insert(0, min_age)
    ages.append(max_age)
    print(ages)

    def find_median(numbers: list[int]):
        while(len(numbers)>2):
            numbers = numbers[1:-1]
        if len(numbers) == 1:
            return numbers[0]
        if len(numbers) == 2:
            return sum(numbers)/2
        
    print(find_median(ages))
    avg_age = sum(ages)/len(ages)
    print(avg_age)
    print(max_age-min_age)
    print(abs(min_age -avg_age) == abs(max_age - avg_age))

    countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
    
    if len(countries) % 2 == 0:
        print(countries[len(countries)//2-1:len(countries)//2+1])
    else:
        print(countries[len(countries)//2])
    
    if len(countries) % 2 == 0:
        first_half = countries[:len(countries)//2]
        second_half = countries[len(countries)//2:]
    else:
        first_half = countries[:len(countries)//2+1]
        second_half = countries[len(countries)//2+1:]
    print(len(first_half), len(second_half))
        
    china, russia, usa, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
    print(china, russia, usa, scandic)

if __name__ == '__main__':
    main()