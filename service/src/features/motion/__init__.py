import MAX
from .wemo_motion_feature import wemo_motion_feature

print('Loading Motion feature')
MAX.features.register('motion', 1, 'Motion sensor feature', wemo_motion_feature)
