import MAX
from .eg_bev_feature import eg_bev_feature

print('Loading bev feature')

MAX.features.register('bev', 1, 'Control Bell ExpressVu using evenghost receiver', eg_bev_feature)
