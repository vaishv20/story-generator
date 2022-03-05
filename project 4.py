import random
when=["yesterday", "last year", "last weekend", "last week", "today"]
who=["a dog", "a cat", "my friend", "a man", "a tortoise"]
name=["joe", "greg", "tom", "sam", "bob"]
happened=["read a book", "ate a cake", "wrote a book", "made a sandwich", "visited a museum"]
residence=["India", "Germany","China", "France", "Brazil"]
went=["for a walk", "to the cinema", "on a trip", "to the mall", "to university"]
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ' went ' + random.choice(went) + ' and ' + random.choice(happened))