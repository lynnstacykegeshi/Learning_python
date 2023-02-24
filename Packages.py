import  ecommerce.shipping
ecommerce.shipping.calc_shipping()

#alternative way, to importa a specific function

from ecommerce.shipping import calc_shipping
calc_shipping()

#to import entire model
from ecommerce import shipping
shipping.calc_shipping()