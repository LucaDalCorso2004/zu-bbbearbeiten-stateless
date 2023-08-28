import helper, unittest

class TestStringMethods(unittest.TestCase):

    def test_add(self):
        helper.delete_all()
        title = "Lorem ipsum"
        helper.add(title)
        item2 = helper.todos[0].isCompleted
        item = helper.todos[0].title
        self.assertEqual(item,"Lorem ipsum")
        self.assertEqual(item2,False)  

    def test_update(self):
        helper.update(0)
        item3 = helper.todos[0].isCompleted
        
        self.assertEqual(item3,True) 
    def test_VerBBBisierung(self):
        title = "B"
        helper.add(title)
        item = helper.todos[0].title
        self.assertEqual(item,"Bbb")   
        title2 = "b"
        helper.add(title2)
        item2 = helper.todos[0].title
        self.assertEqual(item2,"Bbb")        
         

# python -m unittest Test/test_helper.py