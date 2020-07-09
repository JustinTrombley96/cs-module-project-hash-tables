
records = [
    ("Tim", "Texas", "Like coffee"),
    ("Adam", "Florida", "Likes tea"),
    ("Austin", "Florida"),
    ("Kai", "South Carolina"),
    ('Jud', 'Phoebos'),
    ("Eric", "Utah"),
    ("Mandi", "Virginia"),
    ("Emma", "Florida"),
    ("Anna", "Texas"),
    ("Andrew", "Utah"),
    ("Leo", "New York"),
    ('James', "New York"),
]
# Understand
# given a list of records, build an index
# so we can quickly find everyone in a given state

# Plan
## Iterate through the tuples in our list
## Build a dictionary as we go
## use states as key, and names as values

### if state isn't in the dictionary, add it as key
### value: [name1, name2, name3]

### possible value data structures: list, set, nest hashtable
#### {state: {name: lastname}}

## if we have good pseudocode, then we're done planning


'''
for name, state in records:
    value = index.setdefault(state, [])
    value.append(name)
'''

def build_index(records):
    index = {}

    # iterate through list
    for name, state in records:
    ## for each pair, check if the state is in the dictionary
        if state in index:
    ### if so, append the name to the list
            index[state].append(name)
    ### if not, add the key and list (with name in it)
        else:
            index[state] = []
            index[state].append(name)

    return index

idx = build_index(records)

print(idx["South Carolina"])
print(idx["New York"])