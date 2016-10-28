import unittest

class test_dict(unittest.TestCase):
    def test_create_dict(self):
        sheep = {"name":"shaun","breed":"sheep","age":10}
        self.assertTrue(len(sheep)==3)

    def test_access_dict_value_as_attribute(self):
        sheep = {"name":"shaun","breed":"sheep","age":10}
        error = False

        try:
            self.assertTrue(sheep.name=="shaun")
        except:
            error = True

        if not error: 
            self.fail("should be got error")


    def test_walk_through_tree(self):
        separator = ','

        def walk_through(tree):
            if len(tree['sun'])>0:
                return tree['name'] + separator + walk_through(tree['sun'])
            else:
                return tree['name'] 

        family_sheep = {'name':'grangranpa', 'sun':{'name':'granpa','sun':{'name':'shaun', 'sun':{'name':"shaun's sun", 'sun':{}}}}}
        
        self.assertTrue(walk_through(family_sheep)== "grangranpa,granpa,shaun,shaun's sun")



if __name__ == "__main__":
    unittest.main()
