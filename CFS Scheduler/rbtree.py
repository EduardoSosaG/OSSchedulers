'''
Eduardo Sosa
CS337 - Project 03
March 7th, 2022
rbtree.py
'''


class RBNode:
    '''Defines the RBNode class which will make up the components of
    the RB tree.'''

    def __init__(self, key, parent=None, left_child=None,
                 right_child=None, red=False, process=None):

        self.key = key
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.red = red
        self.process = process

    # returns the key of the node.
    def get_key(self):
        return self.key

    # returns the parent of the node.
    def get_parent(self):
        return self.parent

    # returns the left child of the node.
    def get_left_child(self):
        return self.left_child

    # returns the right child of the node.
    def get_right_child(self):
        return self.right_child

    # returns whether the node is red.
    def get_red(self):
        return self.red

    # returns the process at that node.
    def get_process(self):
        return self.process

    # sets the key of the node.
    def set_key(self, key):
        self.key = key

    #  sets the parent of the node.
    def set_parent(self, parent):
        self.parent = parent

    # sets the right child of the node.
    def set_right_child(self, right_child):
        self.right_child = right_child

    # sets the left child of the node.
    def set_left_child(self, left_child):
        self.left_child = left_child

    # sets true or false for whether the node is red.
    def set_red(self, red):
        self.red = red

    # sets the process of the node.
    def set_process(self, process):
        self.process = process


class RBTree:
    '''Defines an RB tree with all the rules along with an insertion
    method and a deletion method with their respective fix-up methods.'''

    def __init__(self):
        self.nil = RBNode(0)
        self.root = self.nil
        self.min_vruntime = self.root
        self.size = 0

    def append(self, value):
        '''appends a value or a node to the tree and then runs insert-fixup
        to retain the balance of said tree'''

        # increases the size by 1.
        self.size += 1

        # checks to see whether the value is a value or a process.
        if (isinstance(value, int)):
            new_node = RBNode(value, self.nil, self.nil, self.nil, red=True)
        else:
            new_node = RBNode(value.get_vruntime(), self.nil, self.nil,
                              self.nil, red=True, process=value)
            value = value.get_vruntime()
        if new_node.get_key() < self.min_vruntime.get_key():
            self.min_vruntime = new_node
        y_pointer = self.nil
        x_pointer = self.root

        while x_pointer != self.nil:
            y_pointer = x_pointer
            if value < x_pointer.get_key():
                x_pointer = x_pointer.get_left_child()
            else:
                x_pointer = x_pointer.get_right_child()
        new_node.set_parent(y_pointer)

        # if the y pointer is nil, then the new_node is the root.
        if y_pointer == self.nil:
            self.root = new_node
            self.min_vruntime = new_node
        # else, we find its new position.
        else:
            if value < y_pointer.get_key():
                y_pointer.set_left_child(new_node)
            else:
                y_pointer.set_right_child(new_node)
        if value < self.min_vruntime.get_key():
            self.min_vruntime = new_node

        # we run insert fix up to retain the balance of the tree.
        self.insert_fixup(new_node)

    def insert_fixup(self, node):
        '''Insert fixup rotates and recolors when we have added a new node
        to retain the balance of the tree'''

        # while the parent of the node is red
        while (node.get_parent().get_red()):
            parent = node.get_parent()
            grandparent = parent.get_parent()

            if grandparent.get_left_child() == parent:
                uncle = grandparent.get_right_child()
            else:
                uncle = grandparent.get_left_child()
            if uncle.get_red():
                uncle.set_red(False)
                parent.set_red(False)
                grandparent.set_red(True)
                node = grandparent
            else:
                # run is_triangle to find out whether we form a triangle.
                triangle = self.is_triangle(grandparent, node)

                # if we are a triangle, then rotate towards
                # the opposite direction.
                if triangle is not None:
                    node = parent
                    self.rotate(node, triangle)

                # sets the parent to black, sets the grandparent to red.
                node.get_parent().set_red(False)
                node.get_parent().get_parent().set_red(True)

                # rotate the grandparent.
                line = self.is_line(node.get_parent().get_parent(), node)
                self.rotate(node.get_parent().get_parent(), line)
        self.root.set_red(False)

    def is_triangle(self, grandparent, node):
        ''' determines whether the grandparent and the node
        form a triangle'''

        # sets triangle to none.
        triangle = None

        # if there is triangle, rotate right or left
        if grandparent.get_right_child().get_left_child() == node:
            triangle = "right"
        elif grandparent.get_left_child().get_right_child() == node:
            triangle = "left"
        return triangle

    def is_line(self, grandparent, node):
        '''determines whether the grandparent and the node
        form a line'''

        line = None
        if grandparent.get_right_child().get_right_child() == node:
            line = "left"
        elif grandparent.get_left_child().get_left_child() == node:
            line = "right"
        return line

    def rotate(self, node, direction):
        '''takes in a node and a direction and
        rotates the node in that direction'''

        if direction == "right":
            self.rotate_right(node)
        else:
            self.rotate_left(node)

    def rotate_left(self, node):
        '''rotates the node to the left'''

        y_pointer = node.get_right_child()
        node.set_right_child(y_pointer.get_left_child())
        y_pointer.get_left_child().set_parent(node)
        y_pointer.set_parent(node.get_parent())

        if node.get_parent() == self.nil:
            self.root = y_pointer
        else:
            if node == node.get_parent().get_left_child():
                node.get_parent().set_left_child(y_pointer)
            else:
                node.get_parent().set_right_child(y_pointer)
        y_pointer.set_left_child(node)
        node.set_parent(y_pointer)

    def rotate_right(self, node):
        '''rotates the node to the right.'''

        y_pointer = node.get_left_child()
        node.set_left_child(y_pointer.get_right_child())
        y_pointer.get_right_child().set_parent(node)
        y_pointer.set_parent(node.get_parent())

        if node.get_parent() == self.nil:
            self.root = y_pointer
        else:
            if node == node.get_parent().get_left_child():
                node.get_parent().set_left_child(y_pointer)
            else:
                node.get_parent().set_right_child(y_pointer)
        y_pointer.set_right_child(node)
        node.set_parent(y_pointer)

    # returns the min vruntime
    def get_min_vruntime(self):
        return self.min_vruntime

    # returns the size of the RB tree
    def get_size(self):
        return self.size

    def remove_min_vruntime(self):
        ''' removes the minimum vruntime from the tree, creates a new
        vruntime depending on the attributes of the min vruntime node and
        then calls the remove method.'''

        min_vruntime = self.min_vruntime
        if min_vruntime.get_right_child() == self.nil:
            self.min_vruntime = min_vruntime.get_parent()
        else:
            self.min_vruntime = min_vruntime.get_right_child()

        # call the remove method on min vruntime
        self.remove(min_vruntime)

    def remove(self, node):
        '''the remove method takes a node in and then removes it.
        We then call the remove fix up method which keeps the tree
        balanced.'''

        # decrease the size of the rb tree
        self.size -= 1
        y = node
        y_color = y.get_red()
        if node.get_left_child() == self.nil:
            x = node.get_right_child()
            self.transplant(node, node.get_right_child())
        elif node.get_right_child() == self.nil:
            x = node.get_left_child()
            self.transplant(node, node.get_left_child())
        else:
            # find the minimum on the right side of the node.
            y = self.tree_minimum(node.get_right_child())
            y_color = y.get_red()
            x = y.get_right_child()
            if y.get_parent() == node:
                x.set_parent(y)
            else:
                # swap y with the right child
                self.transplant(y, y.get_right_child())
                y.set_right_child(node.get_right_child())
                y.get_right_child().set_parent(y)
            self.transplant(node, y)
            y.set_left_child(node.get_left_child())
            y.get_left_child().set_parent(y)
            y.set_red(node.get_red())
        if y_color is False:
            self.delete_fixup(x)

    def delete_fixup(self, node):
        '''this function fixes a tree after a node has been removed or
        transplanted. This function makes sure the tree remains balanced.'''

        while node != self.root and node.get_red() is False:
            if node == node.get_parent().get_left_child():
                w = node.get_parent().get_right_child()
                if w.get_red() is True:
                    w.set_red(False)
                    node.get_parent().set_red(True)
                    self.rotate_left(node.get_parent())
                    w = node.get_parent().get_right_child()
                if (w.get_left_child().get_red() is False
                        and w.get_right_child().get_red() is False):
                    w.set_red(True)
                    node = node.get_parent()
                else:
                    if w.get_right_child().get_red() is False:
                        w.get_left_child().set_red(False)
                        w.set_red(True)
                        parent = node.get_parent()
                        self.rotate_right(w)
                        node.set_parent(parent)
                        w = node.get_parent().get_right_child()
                    w.set_red(node.get_parent().get_red())
                    node.get_parent().set_red(False)
                    w.get_right_child().set_red(False)
                    self.rotate_left(node.get_parent())
                    node = self.root
            else:
                w = node.get_parent().get_left_child()
                if w.get_red() is True:
                    w.set_red(False)
                    node.get_parent().set_red(True)
                    self.rotate_right(node.get_parent())
                    w = node.get_parent().get_left_child()
                if (w.get_right_child().get_red() is False
                        and w.get_left_child().get_red() is False):
                    w.set_red(True)
                    node = node.get_parent()
                else:
                    if w.get_left_child().get_red() is False:
                        w.get_right_child().set_red(False)
                        w.set_red(True)
                        parent = node.get_parent()
                        self.rotate_left(w)
                        node.set_parent(parent)
                        w = node.get_parent().get_left_child()
                    w.set_red(node.get_parent().get_red())
                    node.get_parent().set_red(False)
                    w.get_left_child().set_red(False)
                    self.rotate_right(node.get_parent())

                    node = self.root
        node.set_red(False)

    def transplant(self, u, v):
        '''substitutes u and v for each other and swaps the
        attributes of one node with the other.'''

        if u.get_parent() == self.nil:
            self.root = v
        elif u == u.get_parent().get_left_child():
            u.get_parent().set_left_child(v)
        else:
            u.get_parent().set_right_child(v)
        v.set_parent(u.get_parent())

    def tree_minimum(self, node):
        '''finds the minimum down a node.'''

        # recursively call on the left child.
        while node.get_left_child() != self.nil:
            node = node.get_left_child()
        return node

    def tree_maximum(self, node):
        '''finds the maximum down a node.'''

    # recursively finds the maximum down a node.
        while node.get_right_child() != self.nil:
            node = node.get_right_child()
        return node

    def print_tree_inorder(self, root):
        ''' print the tree in inorder trasversal'''

        # print the node, the color, the parent and the two
        # children of a node
        if root != self.nil:
            self.print_tree_inorder(root.get_left_child())
            print("-------")
            print("Node:", root.get_key())
            print("Is Red: ", root.get_red())
            print("parent: ", root.get_parent().get_key())
            print("children:", root.get_left_child().get_key(),
                  root.get_right_child().get_key())
            self.print_tree_inorder(root.get_right_child())

    def tree_inorder(self):
        '''calls the print in order function and passes the root.'''

        self.print_tree_inorder(self.root)
