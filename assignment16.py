#Q1
years_list = [1998,1999,2000,2001,2002]

#Q2....third birthday was
third_birthday = years_list[3]

#Q3
oldest = years_list[-1]

#Q4
things = ["mozzarella", "cinderella", "salmonella"]

#Q5
things[1] = things[1].capitalize()  #yes it dose change the elements 
print(things)

#Q6 and Q7
surprise = ["Groucho", "Chico", "Harpo"]
surprise[-1] = surprise[-1].lower()[::-1] #its now lower and reverse
surprise[-1] = surprise[-1].capitalize() # now the last element is Oprah

#Q8 and Q9
e2f = {'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}
print(e2f['walrus'])

#Q10
f2e = {}
for x, y in e2f.items():
    f2e[y] = x
print(f2e)

#Q11 and Q12
print(f2e['chien'])
eng_words = set(e2f.keys())
print(eng_words)

#Q13
life = {'animals' : {'cats' : ['Henri', 'Grumpy','Lucy'], 'octopi' : {}, 'emus' : {}},'plants' :{},'other': {}}
print(life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])