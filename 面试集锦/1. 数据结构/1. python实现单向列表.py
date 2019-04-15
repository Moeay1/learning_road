# -*- coding: utf-8 -*-
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        prev = self.head
        self.length = 0
        # 当prev指向第一个节点时, prev.next为None,退出循环
        while prev:
            self.length += 1
            prev = prev.next
        return self.length

    def is_empty(self):
        # 检测链表是否为空
        return self.head is None

    def __str__(self):
        if self.is_empty():
            return 'it is empty'
        nlist = ""
        prev = self.head
        while prev:
            nlist += str(prev.data) + ''
            prev = prev.next
        return nlist

    def append(self, data):
        node = Node(data)
        prev = self.head
        # 当链表为空
        if prev is None:
            self.head = node
        # 遍历并添加到链表末尾
        else:
            while prev.next:
                prev = prev.next
            prev.next = node

    def get(self, index):
        index = index if index >= 0 else len(self) + index

        if len(self) < index or index < 0:
            print('out of index')
            return None

        prev = self.head
        while index:
            prev = prev.next
            index -= 1
        return prev.data

    def update(self, index, data):
        index = index if index >= 0 else len(self) + index
        if len(self) < index or index < 0:
            print('out of index')
            return False

        prev = self.head
        while index:
            prev = prev.next
            index -= 1
        prev.data = data
        return prev.data

    def insert(self, index, data):
        node = Node(data)
        if abs(index + 1) > len(self):
            return False

        index = index if index >= 0 else len(self) + index
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            prev = self.head
            while index - 1:
                prev = prev.next
                index -= 1
            prev.next, node.next = node, prev.next
        return node.data

    def delete(self, index):

        if len(self) < index:
            return False

        prev = self.head
        index = index if index >= 0 else len(self) + index
        prevp = None
        print('index is ', index)

        while index:
            prevp = prev
            prev = prev.next
            index -= 1

        if not prevp:
            temp = self.head
            print('temp is ', temp.data)
            self.head = prev.next
        else:
            temp = prevp.next
            prevp.next = prev.next
        return temp.data

    def __reversed__(self):
        def reverse(pre_node, node):
            if pre_node is self.head:
                pre_node.next = None
            if node:
                next_node = node.next
                node.next = pre_node
                return reverse(node, next_node)
            else:
                self.head = pre_node

            return reverse(self.head, self.head.next)
