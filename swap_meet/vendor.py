from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = None):
        #inventory: list
        self.inventory = inventory if inventory else []
    
    def add(self, item):
        self.inventory.append(item)
        return item
        
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_id(self, id):
        #returns the item with the matching id
        for items in self.inventory:
            if items.id == id:
                return items
        
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        other_vendor.remove(their_item)
        other_vendor.add(my_item)
        self.remove(my_item)
        self.add(their_item)
        return True

    def swap_first_item(self, other_vendor):
        #other_vendor is an instance of Vendor()
        if len(self.inventory) !=0 and len(other_vendor.inventory) != 0:
            return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return False
    
    def get_by_category(self, category):
        matched_list = [inventory for inventory in self.inventory if inventory.__class__.__name__ == category]
        return matched_list

    def get_best_by_category(self, category):
        matched_category = self.get_by_category(category)
        if len(matched_category) == 0:
            return None
        return max(matched_category, key = lambda each_category: each_category.condition)


    def swap_best_by_category(self,other_vendor, my_priority, their_priority):
        item_wanted_by_vendor = other_vendor.get_best_by_category(my_priority)
        item_wanted_by_other_vendor = self.get_best_by_category(their_priority)
        if item_wanted_by_vendor == None or item_wanted_by_other_vendor == None:
            return False
        return self.swap_items(other_vendor, item_wanted_by_other_vendor, item_wanted_by_vendor)
    
    def swap_by_newest(self, other_vendor, my_priority, their_priority):
        items_wanted_by_vendor = other_vendor.get_by_category(my_priority)
        items_wanted_by_other_vendor= self.get_by_category(their_priority)
        newest_item_wanted_by_vendor = (min(items_wanted_by_vendor, key = lambda item: item.age))
        # print(newest_item_wanted_by_vendor)
        newest_item_wanted_by_other_vendor = min(items_wanted_by_other_vendor, key = lambda item: item.age)
        # print(newest_item_wanted_by_other_vendor)
        return self.swap_items(other_vendor, newest_item_wanted_by_other_vendor, newest_item_wanted_by_vendor)
        print(f" self: {self.inventory}\n other{other_vendor.inventory}")