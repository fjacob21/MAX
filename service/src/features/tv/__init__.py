import MAX
from .eg_tv_feature import eg_tv_feature

print('Loading tv feature')

MAX.features.register('tv', 1, 'Evenghost tv control', eg_tv_feature)
