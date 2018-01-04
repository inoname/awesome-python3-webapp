import orm,asyncio
from models import User, Blog, Comment

async def test():
	loop = asyncio.get_event_loop()
	await orm.create_pool(loop, host='localhost', user='root', password='root', db='awesome')
	u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
	print(u)
	await u.save()
	
loop2 = asyncio.get_event_loop()
loop2.run_until_complete(test())
loop2.close()
