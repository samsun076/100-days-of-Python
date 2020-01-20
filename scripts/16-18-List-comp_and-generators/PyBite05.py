NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

PY_CONTENT_CREATORS = ['brian okken', 'michael kennedy', 'trey hunner',
                       'matt harrison', 'julian sequeira', 'dan bader',
                       'michael kennedy', 'brian okken', 'dan bader']

girls = ["ann", "leslie", "ann", "betsy", "stacey", "Ellie", "becky", "ann"]
def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    #PyBites Solution
    return list({name.title() for name in names})
    #return  [name.title() for name in list(dict.fromkeys(names))]


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    #for name in names:
    #    print(name.split()[0], name)
    #PyBites Solution
    return sorted(names, key=lambda x: x.split()[-1],reverse=True)
    #return sorted(names, key=lambda x: x.split(" ")[-1], reverse=True)



def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    #n = [name.split(' ')[0] for name in names]
    #return sorted(n, key=len)[0]

    #PyBites Solution
    names = [name.split()[0] for name in names]
    return min(names, key=len)


print(dedup_and_title_case_names(NAMES))
print(dedup_and_title_case_names(PY_CONTENT_CREATORS))
print()
print(sort_by_surname_desc(NAMES))
print(sort_by_surname_desc(PY_CONTENT_CREATORS))
print()
print(shortest_first_name(NAMES))
print(shortest_first_name(PY_CONTENT_CREATORS))
