it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#===================LEVEL 1===================
companies_len = len(it_companies)
print(companies_len)
it_companies.add("Twitter")
print("Twitter" in it_companies)
it_companies.update({"Sucker Punch", "Rassberry"})
print("Sucker Punch" in it_companies)
it_companies.remove("IBM")
print("IBM" in it_companies)

#===================LEVEL 2===================
C = A.union(B)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B), "  ", B.union(A))
print(A.symmetric_difference(B))
del A
del B

#===================LEVEL 3===================
age_set = set(age)
print(len(age))
print(len(age_set))

sentence = "I am a teacher and I love to inspire and teach people."
sentence_words = sentence.split(" ")
sentence_unique_words = set(sentence_words)
print(len(sentence_words))
print(len(sentence_unique_words))

