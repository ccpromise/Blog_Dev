import sys, orm, asyncio
from models import User, Blog, Comment


@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(user='root', password='password', db='test', loop = loop)

    u = User(name='Test', email='test_1111111111@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()
    yield from orm.destory_pool()


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([test( loop )]))
loop.close()
if loop.is_closed():
    sys.exit(0)