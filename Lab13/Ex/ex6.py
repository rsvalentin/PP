from functional import seq
from collections import namedtuple

Transaction = namedtuple('Transaction', ['reason', 'amount'])
transactions = [
    Transaction(reason='github', amount=7),
    Transaction(reason='food', amount=10),
    Transaction(reason='coffee', amount=5),
    Transaction(reason='netflix', amount=5),
    Transaction(reason='food', amount=5),
    Transaction(reason='youtube', amount=25),
    Transaction(reason='food', amount=10),
    Transaction(reason='amazon', amount=200),
    Transaction(reason='paycheck', amount=-1000)
]


if __name__ == '__main__':
    seq(1, 2, 3, 4)\
        .map(lambda x: x * 2)\
        .filter(lambda x: x > 4)\
        .reduce(lambda x, y: x + y)  # 14
    # sau fara \
    (seq(1, 2, 3, 4)
        .map(lambda x: x * 2)
        .filter(lambda x: x > 4)
        .reduce(lambda x, y: x + y))  # 14

    # sintaxa inspirata din Spark:
    food_cost = seq(transactions) \
        .filter(lambda x: x.reason == 'food') \
        .map(lambda x: x.amount).sum()

    # sintaxa inspirata din LINQ
    food_cost = seq(transactions)\
        .where(lambda x: x.reason == 'food')\
        .select(lambda x: x.amount).sum()

    words = 'I dont want to believe I want to know'.split(' ')
    seq(words).map(lambda word: (word, 1)).reduce_by_key(lambda x, y: x + y)
    '''[('dont', 1), ('I', 2), ('to', 2), ('know', 1), ('want', 2), ('believe', 1)]'''