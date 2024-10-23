import unittest
import todo

class TestToDoCLI(unittest.TestCase):
    
    def test_add_task(self):
        todo.add_task("Write unit tests")
        tasks = todo.load_tasks()
        self.assertEqual(tasks[-1]["description"], "Write unit tests")
        self.assertFalse(tasks[-1]["completed"])

    def test_mark_task_completed(self):
        todo.add_task("Test mark as completed")
        tasks = todo.load_tasks()
        index = len(tasks) - 1
        todo.mark_task_completed(index)
        tasks = todo.load_tasks()
        self.assertTrue(tasks[index]["completed"])

if __name__ == '__main__':
    unittest.main()
