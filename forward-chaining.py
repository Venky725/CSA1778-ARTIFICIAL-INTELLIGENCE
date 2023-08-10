global facts
global is_changed

is_changed = True
facts = [["plant","mango"],["eating","mango"],["seed","sprouts"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "seed":
            assert_fact(["plant",A1[1]])
        if A1[0] == "plant":
            assert_fact(["fruit",A1[1]])
        if A1[0] == "plant" and ["eating",A1[1]] in facts:
            assert_fact(["human",A1[1]])

print(facts)