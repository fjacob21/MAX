import MAX
from .wemo_light_feature import wemo_light_feature

print('Loading Light feature')
MAX.features.register('light', 1, 'Light control feature', wemo_light_feature)
