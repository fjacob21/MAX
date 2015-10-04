import MAX
from .openhouse_script import openhouse_script

print('Loading open house script')

MAX.scripts.register('openhouse', 1, 'Script to open my house things', openhouse_script)
