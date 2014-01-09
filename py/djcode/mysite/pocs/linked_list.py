from apt_pkg import init

__author__ = 'rami'


class Node(object):
    def __init__( self, data, next ):
        self.data = data
        self.next = next

    def add_before(self, value):
        new_node = Node(value, self)
        return new_node

    def __repr__(self):
        return '%s--%s' % self.data, self.next

    def __str__(self):
        return '%s' % self.data

def get_print_list_str(node, prefix=''):
    if not node:
        return '%s --> --||' % prefix
    else:
        prefix = '%s --> %s ' % (prefix, node)
        return get_print_list_str( node.next, prefix)

def reverse_list_recursively( prev, node ):
    if not node:
        return prev
    else:
        new_head = reverse_list_recursively(node, node.next)
        node.next = prev
        return new_head

def reverse_list_iteratively( head ):
    cur = head
    prev = None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    head = prev
    return head




