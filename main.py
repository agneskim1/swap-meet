from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

vendor = Clothing(condition = 4, age = 4)
# #create an instance of vendor

# # print(vendor.add("cat"))

# # print(vendor.remove("kitty"))

# # item = Item()
# # print(item)

# # print(item.get_category())

# # print(vendor.get_by_id(123))
# clothing = Clothing(condition = 4)
# item = Item(id = 123, condition = 4)

# print(clothing.id)
# # print(clothing.condition)
# print(item.condition)
# print(item.condition_description())
# print(vendor.get_by_category("Clothing"))
# print(vendor.get_best_by_category("Clothing"))

item_a = Decor(condition=2.0, age = 2.0)
item_b = Electronics(condition=4.0, age = 4.0)
item_c = Decor(condition=4.0, age = 4.0)
tai = Vendor(
    inventory=[item_a, item_b, item_c]
)

# them
item_d = Clothing(condition=2.0, age = 2.0)
item_e = Decor(condition=4.0, age = 4.0)
item_f = Clothing(condition=4.0, age = 4.0)
jesse = Vendor(
    inventory=[item_d, item_e, item_f]
)

# Act
print(tai.swap_by_newest(other_vendor=jesse,my_priority="Clothing",their_priority="Decor"))

print(item_d.age)
(tai.swap_best_by_category(jesse, "Clothing", "Decor"))

