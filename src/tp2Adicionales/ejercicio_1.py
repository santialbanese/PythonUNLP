#1)
zen = """Beautiful is better than ugly.
Explained is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Plano is better than nesting.
Spacing is better than dense.
Readability is important.
Special cases are not special enough to break the rules.
However, practicality beats purity.
Mistakes should never pass quietly.
Unless they are explicitly silenced.
Faced with ambiguity, avoid the temptation to guess.
There should be one, and preferably just one, obvious way to do it.
Even though that's not obvious at first unless you're Dutch.
Now it's better than ever.
Although it's never much better than now.
If implementation is hard to explain, it's a bad idea.
If implementation is easy to explain, it may be a good idea.
Namespaces are a great idea, let's have more of those."""

zen = zen.split("\n")
for aux in zen:
    if aux.split()[1][0].lower().startswith(('a', 'e', 'i', 'o', 'u')):
        print(aux)