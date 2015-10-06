import MAX
from .closehouse_script import closehouse_script

print('Loading close house script')

MAX.scripts.register('closehouse', 1, 'Script to close my house things', closehouse_script)
