import sys
import copy as cp
print_array = []

INT_MIN = -sys.maxsize-1


class BTreeNode:
    """Btree Node"""
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.data = val


def in_order(temp, g_val = []):
    """Function for In-order Traversal"""

    # if temp:
    # """Recursive Solution"""
    #     in_order(temp.left)
    #     # print(temp.data)
    #     g_val.append(temp.data)
    #     in_order(temp.right)

    """Non Recursive Solution"""
    if not temp:
        return

    btree_stack = []
    st_temp = temp

    while 1:
        while st_temp:
            btree_stack.append(st_temp)
            st_temp = st_temp.left

        if not len(btree_stack):
            break

        st_temp = btree_stack.pop()
        g_val.append(st_temp.data)
        st_temp = st_temp.right

    btree_stack.clear()


def pre_order(temp, g_val = []):
    """Function for Pre-Order Traversal"""

    # if temp:
    # """Recursive Solution"""
    #     g_val.append(temp.data)
    #     pre_order(temp.left)
    #     pre_order(temp.right)

    """Non Recursive Solution"""

    if not temp:
        return

    btree_stack = []
    st_temp = temp

    while 1:
        while st_temp:
            g_val.append(st_temp.data)
            btree_stack.append(st_temp)
            st_temp = st_temp.left

        if not len(btree_stack):
            break

        st_temp = btree_stack.pop()
        st_temp = st_temp.right

    btree_stack.clear()


def post_order(temp, g_val = []):
    """Function for Post Order Traversal"""

    """recursive Solution"""
    # if temp:
    #     post_order(temp.left)
    #     post_order(temp.right)
    #     g_val.append(temp.data)

    """Non Recursive Solution"""
    if not temp:
        return

    btree_stack = [temp]
    prev = None

    while len(btree_stack):
        current = btree_stack.pop()
        if not prev or prev.left == current or prev.right == current:
            btree_stack.append(current)
            if current.left:
                btree_stack.append(current.left)
            elif current.right:
                btree_stack.append(current.right)
            else:
                g_val.append(current.data)
                btree_stack.pop()
        elif current.left == prev:
            btree_stack.append(current)
            if current.right:
                btree_stack.append(current.right)
        else:
            g_val.append(current.data)
            # btree_stack.pop()

        prev = current

    btree_stack.clear()


def level_order(temp, g_val = []):
    """Level Order Traversal"""

    if not temp:
        return

    btree_q = [temp]

    while len(btree_q):
        curr = btree_q.pop(0)
        g_val.append(curr.data)
        if curr.left:
            btree_q.append(curr.left)
        if curr.right:
            btree_q.append(curr.right)

    btree_q.clear()


def add_new_node(root, new_val):
    """Addition of a new Node"""

    temp = root
    binary_q = [temp]

    while len(binary_q):
        temp = binary_q.pop(0)
        if temp.left:
            binary_q.append(temp.left)
        elif not temp.left:
            temp.left = BTreeNode(new_val)
            break

        if temp.right:
            binary_q.append(temp.right)
        else:
            temp.right = BTreeNode(new_val)
            break

    binary_q.clear()


def find_element(temp, m_key):
    """Finding any element"""
    if not temp:
        return 0

    """Recursive Solution"""
    # if temp.data == m_key:
    #     return 1
    # if find_element(temp.left, m_key):
    #     return 1
    #
    # return find_element(temp.right, m_key)

    """Non Recursive Solution"""
    data_q = [temp]
    cur = None

    while len(data_q):
        cur = data_q.pop(0)
        if cur.data == m_key:
            data_q.clear()
            return 1
        if cur.left:
            data_q.append(cur.left)
        if cur.right:
            data_q.append(cur.right)

    data_q.clear()
    return 0


def find_max(temp):
    """Find Max Element"""
    if not temp:
        return INT_MIN

    max_element = temp.data

    data_q = [temp]

    while len(data_q):
        cur = data_q.pop(0)
        if cur.data > max_element:
            max_element = cur.data
        if cur.left:
            data_q.append(cur.left)
        if cur.right:
            data_q.append(cur.right)

    data_q.clear()
    return max_element


def re_level_order(temp):
    """Print Reverse level order"""
    global g_val

    if not temp:
        return

    btree_q = [temp]

    while len(btree_q):
        curr = btree_q.pop(0)
        g_val.append(curr.data)
        if curr.right:
            btree_q.append(curr.right)
        if curr.left:
            btree_q.append(curr.left)

    btree_q.clear()
    g_val.reverse()


def del_tree(*args):
    """Delete The tree"""
    del_list = []
    for temp in args:
        if not temp:
            return

        btree_q = [temp]

        while len(btree_q):
            curr = btree_q.pop(0)
            del_list.append(curr)
            if curr.left:
                btree_q.append(curr.left)
            if curr.right:
                btree_q.append(curr.right)

        while len(del_list):
            cur = del_list.pop()
            if cur.left:
                cur.left = None
            if cur.right:
                cur.right = None
            if cur.data:
                cur.data = None

        btree_q.clear()
        del_list.clear()


def clc_height(temp):
    """Calculate Tree Height"""
    left_length = 0
    right_length = 0

    if not temp:
        return -1

    if temp.left:
        left_length = clc_height(temp.left)
    if temp.right:
        right_length = clc_height(temp.right)

    if left_length > right_length:
        return left_length + 1
    else:
        return right_length + 1


def find_diameter(temp):
    """Calculates The Diameter/width (Max distance between any two nodes) of a tree"""
    if not temp:
        return 0

    lwidth = clc_height(temp.left)
    rwidth = clc_height(temp.right)

    return max([(lwidth + rwidth + 1), find_diameter(temp.left), find_diameter(temp.right)])


def find_deepest_node(temp):
    """Calculate Deepest Node"""
    if not temp:
        return None

    btree_q = [temp]

    while len(btree_q):
        curr = btree_q.pop(0)
        if curr.right:
            btree_q.append(curr.right)
        if curr.left:
            btree_q.append(curr.left)

    btree_q.clear()
    return curr


def f_level_sum(temp):
    """Finds the sum of each level and push it into a list
    and finally returns that list"""

    l_of_sum = []
    node_sum = 0
    if not temp:
        return None

    btree_q = []
    btree_q.append(temp)
    btree_q.append(None)

    while len(btree_q):
        btree_element = btree_q.pop(0)

        if btree_element:
            node_sum += btree_element.data

            if btree_element.left:
                btree_q.append(btree_element.left)

            if btree_element.right:
                btree_q.append(btree_element.right)
        else:
            l_of_sum.append(node_sum)
            node_sum = 0
            if len(btree_q):
                btree_q.append(None)

    return l_of_sum


def print_r_to_l(temp):
    """Prints all the Root-To-Leaf arrays"""

    if not temp:
        return

    global print_array

    print_array.append(str(temp.data))
    if temp.left:
        print_r_to_l(temp.left)
    if temp.right:
        print_r_to_l(temp.right)
    if not temp.left and not temp.right:
        print(' '.join(print_array))

    print_array.pop()


def find_root_path(temp, key, path = []):
    """Finds the path between a particular node and Root"""

    if not temp or not key:
        return False

    path.append(temp)
    if temp.data == key:
        return True

    if find_root_path(temp.left, key, path):
        return True
    if find_root_path(temp.right, key, path):
        return True

    path.pop()
    return False


def find_lca_path(temp, key1, key2, path = []):
    """Finds the path from Root to Least Common Ancestor (LCA)"""

    if not temp or not key1 or not key2:
        return None

    path1 = []
    path2 = []
    if not find_root_path(temp, key1, path1):
        return None

    if not find_root_path(temp, key2, path2):
        return None
    l_len = len(path1) if len(path1) < len(path2) else len(path2)

    for idx in range(l_len):
        if path1[idx] == path2[idx]:
            path.append(path1[idx])
        else:
            break

    return path[-1]


def find_n_path(temp, key1, key2):
    """Finds the relative Path and Path Length between two nodes"""

    path = []

    if not temp or not key1 or not key2:
        yield -1
        yield path

    l_path = []
    k1_path = []
    k2_path = []
    lca_node = find_lca_path(temp, key1, key2, l_path)

    if not lca_node:
        yield -1
        yield path
    if not find_root_path(temp, key1, k1_path):
        yield -1
        yield path
    if not find_root_path(temp, key2, k2_path):
        yield -1
        yield path

    if lca_node.data != key1 and lca_node.data != key2:
        if lca_node.left == k1_path[len(l_path)]:
            lpath = k1_path[len(l_path):]
            rpath = k2_path[len(l_path):]
        else:
            rpath = k1_path[len(l_path):]
            lpath = k2_path[len(l_path):]
    elif lca_node.data == key1:
        if lca_node.left == k2_path[len(l_path)]:
            lpath = k2_path[len(l_path):]
            rpath = []
        else:
            lpath = []
            rpath = k2_path[len(l_path):]
    else:
        if lca_node.left == k1_path[len(l_path)]:
            lpath = k1_path[len(l_path):]
            rpath = []
        else:
            lpath = []
            rpath = k1_path[len(l_path):]

    lpath.reverse()
    path = lpath
    path.append(lca_node)
    path += rpath

    yield (len(k1_path) - 1) + (len(k2_path) - 1) - (2 * (len(l_path) - 1))
    yield list(map(lambda x: x.data, path))


def find_path_from_sum(temp, sum_key):
    """Checks whether there is a path,
    for which the sum of all nodes are equals to sum_key"""

    if not temp:
        return []

    path = []
    tree_path = []
    level_order(temp, tree_path)

    # In tree_path, inserting 0 in index 0 to start the actual indexing from 1
    tree_path.insert(0,0)

    for o_idx in range(len(tree_path) - 1, 0, -1):
        i_idx = o_idx
        while i_idx > 0:
            path.append(tree_path[i_idx])
            i_idx = int(i_idx/2)
        if sum(path) == sum_key:
            path.reverse()
            return path
        path.clear()

    return []


def mirror_tree(root):
    """Mirror a tree"""
    if not root:
        return

    mirror_tree(root.left)
    mirror_tree(root.right)

    temp = root.left
    root.left = root.right
    root.right = temp


def build_tree_from_traversal(in_order_list = [], pre_order_list = []):
    """When the inorder and preorder traversal of a tree is provided,
    format the tree from those"""

    if len(in_order_list) == 0:
        return None

    new_node = BTreeNode(pre_order_list.pop(0))
    in_order_idx = in_order_list.index(new_node.data)
    new_node.left = build_tree_from_traversal(in_order_list[: in_order_idx], pre_order_list)
    new_node.right = build_tree_from_traversal(in_order_list[in_order_idx + 1 :], pre_order_list)

    return new_node


try:
    print("====== Start of Program ======")

    # ip_list = list(map(int, input('Provide The numbers\nTo be added into the binary tree:\n').split()))
    # key = int(input('Provide the key to be found:\n'))
    # key1 = int(input('Provide key1 to get the path:\n'))
    # key2 = int(input('Provide key2 to get the path:\n'))
    # sum_key = int(input('Provide key for check sum path:\n'))

    ip_list = [1, 2, 3, 4, 5, 6, 7]
    key = 5
    key1 = 3
    key2 = 6
    sum_key = 11
    in_order_list = [4, 2, 5, 1, 6, 3, 7]
    pre_order_list = [1, 2, 4, 5, 3, 6, 7]

    g_val = []
    g_new_val = []
    path_btwn_nodes = []

    new_root = build_tree_from_traversal(in_order_list, pre_order_list)
    level_order(new_root, g_new_val)
    print(f"The new tree is: {' '.join(map(str, g_new_val))}")

    root = BTreeNode(ip_list[0])
    for ip_idx in range(1,len(ip_list)):
        add_new_node(root, ip_list[ip_idx])

    print(f'The Height of the btree is: {clc_height(root)}')
    print_r_to_l(root)

    # in_order(root, g_val)
    # pre_order(root, g_val)
    # post_order(root, g_val)
    level_order(root, g_val)
    # re_level_order(root, g_val)
    print(f"The tree is: {' '.join(map(str, g_val))}")

    if find_element(root, key):
        print(f'Found {key}')
    else:
        print(f'Not Found {key}')

    node_n_path = find_n_path(root,key1,key2)
    path_length_btw_keys = node_n_path.__next__()
    path_btwn_nodes = node_n_path.__next__()
    if path_length_btw_keys == -1:
        raise Exception("Invalid Key provided")

    print(f'path_length_btw_keys: {path_length_btw_keys}')
    print(f"Path between keys: {path_btwn_nodes}")
    l_sum_list = f_level_sum(root)
    print(f"Max Sum between all levels: {max(l_sum_list)}")

    print(f'The Diameter of binary tree is: {find_diameter(root)}')

    print(f'The deepest node is: {find_deepest_node(root).data}')

    print(f"Max Number in the list is: {find_max(root)}")

    check_sum_path = find_path_from_sum(root,sum_key)
    print(f"Check Sum Path: {check_sum_path}")

    r_root = cp.deepcopy(root)
    r_g_val = []
    mirror_tree(r_root)
    level_order(r_root,r_g_val)
    print(f"Reverse Tree is: {' '.join(map(str, r_g_val))}")
    print(f"The tree is: {' '.join(map(str, g_val))}")

    del_tree(root, r_root)
    if root.data or r_root.data:
        print("lists are not deleted")
    else:
        print("lists are deleted")

except:
    print(sys.exc_info())
finally:
    print("====== End of Program ======")
