import MAX
from .wol_feature import wol_feature

print('Loading Wake on Lan feature')
MAX.features.register('wol', 1, 'Wake on Lan feature', wol_feature)
