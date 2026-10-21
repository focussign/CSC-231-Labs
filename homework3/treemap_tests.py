import io
import re
import sys
import traceback
from contextlib import redirect_stdout


def _assert(expected, actual, call, pmsg=None, fmsg=None):
    _default = f"Called {call}. Expected value: {expected}\t Your code: {actual}"
    if not pmsg:
        pmsg = _default
    if not fmsg:
        fmsg = _default

    if actual == expected:
        print(f"\u2713 passed: {pmsg}")
        return True
    else:
        print(f"\u2717 failed: {fmsg}")
        return False


def test(fail_out=False, msg="Aborting all tests."):
    def decorator(func):
        def wrapper(self):
            try:
                print('-' * 5, func.__name__, '-' * 5)
                passed = func(self)
                self.suite_passed *= passed
                if passed:
                    self.passed_count += 1
                    self.passed_tests.append(func.__name__)
                    print('\u2713' * 3, func.__name__, "all passed!")
                else:
                    print('\u2717' * 3, func.__name__, "- a test above failed.")
            except NotImplementedError:
                print(f"\u2717 failed: Not yet implemented. Aborting further tests of this function.")
                self.suite_passed = False
                return
            except Exception as e:
                self.suite_passed = False
                print(f"\u2717 failed due to an unanticipated exception")
                traceback.print_exc(file=sys.stdout)
                if fail_out:
                    print('\u2717' * 3, msg)
                    exit(0)
                print("Aborting further tests of this function.")
                return

        return wrapper

    return decorator


class TestSuite:

    def __init__(self, module_name):
        self.module = module_name
        self.suite_passed = True
        self.passed_count = 0
        self.test_count = 4
        self.passed_tests = []


    @test()
    def test_01_delitem(self):

        passed = True
        tree = self.module.TreeMap()
        print("Creating a new empty tree")
        try:
            del tree[5]
            print("\u2717 FAILED: call to 'del tree[5]' on an empty tree should raise a KeyError")
            passed = False
        except KeyError:
            print("\u2713 passed: called del tree[5] on an empty tree correctly raised a KeyError")

        print("tree[10] = 'Alice'")
        tree[10] = 'Alice'
        print("del tree[10]")
        del tree[10]
        passed *= _assert(expected=0,
                          actual=len(tree),
                          call="len(tree)",
                          fmsg="len(tree) should be zero after deleting the only node in the tree")

        passed *= _assert(expected=False,
                          actual=10 in tree,
                          call="(10 in tree)",
                          fmsg="'10 in tree' should return False after the key was deleted")

        passed *= _assert(expected=None,
                          actual=tree.root,
                          call="tree.root",
                          fmsg="tree.root should be None after deleting the only node in the tree",
                          pmsg="tree.root is None after deleting the only node in the tree")

        try:
            del tree[10]
            print("\u2717 FAILED: call to 'del tree[10]' on a now-empty tree should have raised a KeyError")
            passed = False
        except KeyError:
            print("\u2713 passed: called del tree[10] on a now-empty tree correctly raised a KeyError")

        print("Putting people back in the tree:")
        print("tree[10] = 'Alice'")
        tree[10] = 'Alice'
        print("tree[5] = 'Bob'")
        tree[5] = 'Bob'
        print("tree[15] = 'Charlie'")
        tree[15] = 'Charlie'

        print(
            "Deleting the root (10:Alice). The tree should have two nodes with 15:Charlie the new root and 5:Bob the left child")
        print("del tree[10]")
        del tree[10]
        passed *= _assert(expected='Charlie',
                          actual=tree.root.value,
                          call="tree.root.value",
                          fmsg=f"tree.root.value should be Charlie after deleting the root with two children. Your tree.root.value={tree.root.value}")

        passed *= _assert(expected=15,
                          actual=tree.root.key,
                          call="tree.root.key",
                          fmsg=f"tree.root.key should be 16 after deleting the root with two children. Your tree.root.key={tree.root.key}")

        passed *= _assert(expected=2,
                          actual=len(tree),
                          call="len(tree)")

        passed *= _assert(expected=False,
                          actual=10 in tree,
                          call="(10 in tree)",
                          fmsg="(10 in tree) should return False after the key was deleted. Your code returned True")

        try:
            del tree[10]
            print("\u2717 FAILED: called del[10] (which was previously deleted) should have raised a KeyError")
            passed = False
        except KeyError:
            print("\u2713 passed: called del[10] (which was previously deleted) correctly raised a KeyError")

        act = len(tree)
        passed *= _assert(expected=2,
                          actual=act,
                          call="len(tree)",
                          fmsg=f"len(tree) should be still two after trying to delete a node that wasn't there. Your len(tree)={act}",
                          pmsg="len(tree) should be still two after trying to delete a node that wasn't there")

        print("Now deleting the left child (5:Bob). The tree should now be only 15:Charlie at the root.")
        print("del tree[5]")
        del tree[5]
        passed *= _assert(expected='Charlie',
                          actual=tree.root.value,
                          call="tree.root.value",
                          fmsg=f"tree.root.value should still be value=Charlie after deleting the one child. Your tree.root.value={tree.root.value}",
                          pmsg="tree.root.value should still be value=Charlie after deleting the one child.",
                          )

        passed *= _assert(expected=15,
                          actual=tree.root.key,
                          call="tree.root.key",
                          fmsg=f"tree.root.key should still be key=15 after deleting the one child. Your tree.root.key={tree.root.key}",
                          pmsg="tree.root.key should still be key=15 after deleting the one child",
                          )

        passed *= _assert(expected=1,
                          actual=len(tree),
                          call="len(tree)")

        passed *= _assert(expected=False,
                          actual=5 in tree,
                          call="(5 in tree)")

        print("Now deleting the final node (15:Charlie)")
        print("del tree[15]")
        del tree[15]
        act = len(tree)
        passed *= _assert(expected=0,
                          actual=act,
                          call="len(tree)",
                          fmsg=f"len(tree) should be zero after deleting all the nodes. Your len(tree)={act}")

        passed *= _assert(expected=None,
                          actual=tree.root,
                          call="tree.root",
                          fmsg=f"tree.root should be None after deleting all the nodes. Your tree.root={tree.root}")

        passed *= _assert(expected=False,
                          actual=15 in tree,
                          call="(15 in tree)",
                          fmsg="(15 in tree) should return False after the key was deleted. Your code returned True")

        print("\nCreating a new tree and putting in 5 key:value pairs:")
        print("tree = TreeMap()")
        tree = self.module.TreeMap()
        print("tree[10] = 'Alice'")
        tree[10] = 'Alice'
        print("tree[5] = 'Bob'")
        tree[5] = 'Bob'
        print("tree[1] = 'Charlie'")
        tree[1] = 'Charlie'
        print("tree[15] = 'Dave'")
        tree[15] = 'Dave'
        print("tree[12] = 'Ernie'")
        tree[12] = 'Ernie'
        print("It would be a good idea to draw what that tree should look like!")

        print("Deleting a leaf node: del tree[1]")
        del tree[1]
        passed *= _assert(expected=4,
                          actual=len(tree),
                          call="len(tree)",
                          fmsg='deleted a leaf node (tree[1]). length should be 4')

        passed *= _assert(expected=None,
                          actual=tree.root.left.left,
                          call="tree.root.left.left",
                          fmsg=f'tree.root.left.left (left grandchild of root) should be None after deleting that leaf node. Your tree.root.left.left={tree.root.left.left}',
                          pmsg='tree.root.left.left (left grandchild of root) should be None after deleting that leaf node')

        passed *= _assert(expected=False,
                          actual=1 in tree,
                          call="(1 in tree)")

        print("Deleting a node with one child: del tree[15]")
        del tree[15]
        passed *= _assert(expected=3,
                          actual=len(tree),
                          call='len(tree)')

        passed *= _assert(expected='Ernie',
                          actual=tree.root.right.value,
                          call="tree.root.right.value",
                          fmsg=f"tree.root.right.value (root's right child) should NOW have value='Ernie' after deleting the original right child. Your tree.root.right.value={tree.root.right.value}",
                          pmsg="tree.root.right.value (root's right child) should NOW have value='Ernie' after deleting the original right child")

        passed *= _assert(expected=12,
                          actual=tree.root.right.key,
                          call="tree.root.right.key",
                          fmsg=f"tree.root.right.key (root's right child) should NOW have key=12 after deleting the original right child. Your tree.root.right.key={tree.root.right.key}",
                          pmsg="tree.root.right.key (root's right child) should NOW have key=12 after deleting the original right child")

        passed *= _assert(expected=False,
                          actual=15 in tree,
                          call="(15 in tree)")

        print("\nCreating a new tree and putting in 6 key:value pairs:")
        print("tree = TreeMap()")
        tree = self.module.TreeMap()
        print("tree['Frank'] = 'Zonk'")
        tree['Frank'] = 'Zonk'
        print("tree['Bob'] = 12345")
        tree['Bob'] = 12345
        print("tree['Alice'] = 84431")
        tree['Alice'] = 84431
        print("tree['Dave'] = 131234")
        tree['Dave'] = 131234
        print("tree['Charlie'] = 123455")
        tree['Charlie'] = 123455
        print("tree['Cara'] = 99999")
        tree['Cara'] = 99999
        print("It would be a good idea to draw what that tree should look like!")

        print("Delete 'Bob' who is the left child of the root: del tree['Bob']")
        del tree['Bob']
        passed *= _assert(expected=99999,
                          actual=tree.root.left.value,
                          call="tree.root.left.value",
                          fmsg=f"left child of the root should have been replaced by its inorder successor node ('Cara':99999), so the tree.root.left.value=99999. Your tree.root.left.value={tree.root.left.value}",
                          pmsg="left child of the root should have been replaced by its inorder successor node ('Cara':99999), so the tree.root.left.value=99999")

        passed *= _assert(expected='Cara',
                          actual=tree.root.left.key,
                          call="tree.root.left.key",
                          fmsg=f"left child of the root should have been replaced by its inorder successor node ('Cara':99999), so tree.root.left.key=='Cara'. Your tree.root.left.key={tree.root.left.key}",
                          pmsg="left child of the root should have been replaced by its inorder successor node ('Cara':99999), so tree.root.left.key=='Cara'")

        passed *= _assert(expected=5,
                          actual=len(tree),
                          call='len(tree)')

        passed *= _assert(expected=False,
                          actual='Bob' in tree,
                          call="('Bob' in tree)")

        print("Now delete 'Cara', who is the new left child of the root: del tree['Cara']")
        del tree['Cara']
        passed *= _assert(expected='Charlie',
                          actual=tree.root.left.key,
                          call="tree.root.left.key",
                          fmsg=f"left child of the root should have been replaced by its inorder successor node ('Charlie':123455), so tree.root.left.key=='Charlie'. Your tree.root.left.key={tree.root.left.key}",
                          pmsg="left child of the root should have been replaced by its inorder successor node ('Charlie':123455), so tree.root.left.key=='Charlie'")

        passed *= _assert(expected=123455,
                          actual=tree.root.left.value,
                          call="tree.root.left.value",
                          fmsg=f"left child of the root should have been replaced by its inorder successor node ('Charlie':123455), so tree.root.left.value==123455. Your tree.root.left.value={tree.root.left.value}",
                          pmsg="left child of the root should have been replaced by its inorder successor node ('Charlie':123455), so tree.root.left.value==123455")

        passed *= _assert(expected=4,
                          actual=len(tree),
                          call="len(tree)")

        passed *= _assert(expected=False,
                          actual='Cara' in tree,
                          call="('Cara' in tree)")

        return passed

    def _get_test_tree(self):
        print("Creating a new tree and inserting the following:")
        tree = self.module.TreeMap()
        print("tree['Charlie'] = 55555")
        tree['Charlie'] = 55555
        print("tree['Bob'] = 44444")
        tree['Bob'] = 44444
        print("tree['Alice'] = 33333")
        tree['Alice'] = 33333
        print("tree['Banks'] = 123145")
        tree['Banks'] = 123145
        print("tree['Dave'] = 891273")
        tree['Dave'] = 891273
        print("tree['Chris'] = 9012")
        tree['Chris'] = 9012
        print("tree['Ernie'] = 0000000")
        tree['Ernie'] = 0000000
        print("tree['Doug'] = 123")
        tree['Doug'] = 123
        print("tree['Frank'] = 0000000")
        tree['Frank'] = 0000000
        return tree

    @test()
    def test_02_inorder_traversal(self):

        passed = True
        tree = self._get_test_tree()
        print("It would be a good idea to draw the tree!")

        print(
            "I am capturing the output of your method and putting it into a string, then stripping out all of the whitespace.")
        f = io.StringIO()
        with redirect_stdout(f):
            tree.traverse_inorder()
        actual = re.sub(r'\s+', '', f.getvalue())

        print("This comparison will fail if you have incorrect capitalization or extra character in your printing.")
        expected = "TreeNode(Alice,33333)TreeNode(Banks,123145)TreeNode(Bob,44444)TreeNode(Charlie,55555)TreeNode(Chris,9012)TreeNode(Dave,891273)TreeNode(Doug,123)TreeNode(Ernie,0)TreeNode(Frank,0)"
        passed *= _assert(expected=expected,
                          actual=actual,
                          call="traverse_inorder()",
                          pmsg=f"called traverse_inorder():\n\t{'Expected: ':<12}{expected}\n\t{'Your code: ':<12}{actual}",
                          fmsg=f"called traverse_inorder():\n\t{'Expected: ':<12}{expected}\n\t{'Your code: ':<12}{actual}")

        tree = self.module.TreeMap()
        f = io.StringIO()
        with redirect_stdout(f):
            tree.traverse_inorder()
        actual = re.sub(r'\s+', '', f.getvalue())
        passed *= _assert(expected='',
                          actual=actual,
                          call="traverse_inorder() on an empty tree should not print anything")

        return passed

    @test()
    def test_03_preorder_traversal(self):

        passed = True
        tree = self._get_test_tree()
        print("It would be a good idea to draw the tree!")

        print(
            "I am capturing the output of your method and putting it into a string, then stripping out all of the whitespace.")
        f = io.StringIO()
        with redirect_stdout(f):
            tree.traverse_preorder()
        actual = re.sub(r'\s+', '', f.getvalue())

        expected = "TreeNode(Charlie,55555)TreeNode(Bob,44444)TreeNode(Alice,33333)TreeNode(Banks,123145)TreeNode(Dave,891273)TreeNode(Chris,9012)TreeNode(Ernie,0)TreeNode(Doug,123)TreeNode(Frank,0)"
        passed *= _assert(expected=expected,
                          actual=actual,
                          call="traverse_preorder()",
                          pmsg=f"called traverse_preorder():\n\t{'Expected: ':<12}{expected}\n\t{'Your code: ':<12}{actual}",
                          fmsg=f"called traverse_preorder():\n\t{'Expected: ':<12}{expected}\n\t{'Your code: ':<12}{actual}")

        tree = self.module.TreeMap()
        f = io.StringIO()
        with redirect_stdout(f):
            tree.traverse_preorder()
        actual = re.sub(r'\s+', '', f.getvalue())
        passed *= _assert(expected='',
                          actual=actual,
                          call="traverse_preorder() on an empty tree should not print anything")

        return passed

    @test()
    def test_04_postorder_traversal(self):

        passed = True
        tree = self._get_test_tree()
        print("It would be a good idea to draw the tree!")

        print(
            "I am capturing the output of your method and putting it into a string, then stripping out all of the whitespace.")
        f = io.StringIO()
        with redirect_stdout(f):
            tree.traverse_postorder()
        actual = re.sub(r'\s+', '', f.getvalue())

        expected = "TreeNode(Banks,123145)TreeNode(Alice,33333)TreeNode(Bob,44444)TreeNode(Chris,9012)TreeNode(Doug,123)TreeNode(Frank,0)TreeNode(Ernie,0)TreeNode(Dave,891273)TreeNode(Charlie,55555)"
        passed *= _assert(expected=expected,
                          actual=actual,
                          call="traverse_postorder()",
                          pmsg=f"called traverse_postorder():\n\t{'Expected: ':<12}{expected}\n\t{'Your code: ':<12}{actual}",
                          fmsg=f"called traverse_postorder():\n\t{'Expected: ':<12}{expected}\n\t{'Your code: ':<12}{actual}")

        tree = self.module.TreeMap()
        f = io.StringIO()
        with redirect_stdout(f):
            tree.traverse_postorder()
        actual = re.sub(r'\s+', '', f.getvalue())
        passed *= _assert(expected='',
                          actual=actual,
                          call="traverse_postorder() on an empty tree should not print anything")

        return passed

    def run_all(self):
        self.test_01_delitem()
        self.test_02_inorder_traversal()
        self.test_03_preorder_traversal()
        self.test_04_postorder_traversal()
