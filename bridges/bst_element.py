from bridges.bin_tree_element import *
##
#    @brief The BSTElement class is the building block for creating binary search trees.
#
#   The BSTElement class is the building block for creating binary search tree structures.
#    It contains two children (viz., left, right), and a search key, to be used
#    in search operations .
#
#    BSTElement contains a visualizer (ElementVisualizer) object for setting visual
#    attributes (color, shape, opacity, size), necessary for displaying them in a
#    web browser.
#
#    BST Elements also have a LinkVisualizer object, that is used when they are linked to
#    another element, appropriate for setting link attributes, for instance, between
#    the current element and its left or right child
#
#  	@author Kalpathi Subramanian, Mihai Mehedint, Matthew McQuaigue
#
#  	@date 6/22/16, 1/7/17, 5/17/17
#
#  	@brief This class extends the BinTreeElement class by adding a 'key' value
#  	for use in a binary search tree implementations.
#
#
class BSTElement(BinTreeElement):

    def __init__(self, **kwargs) -> None:
        """
        Constructor bst element
        Kwargs:
            (str) key: The label for the tree element that shows in visualization
            (generic) e: the generic object that the tree element will hold
            (BinTreeElement) left: the tree element assigned to child 0
            (BinTreeElement) right: the tree element assigned to child 1
        Returns:
            None
        """
        if 'e' in kwargs:
            if 'left' in kwargs and 'right' in kwargs:
                super(BinTreeElement, self).__init__(e=kwargs['e'], left = kwargs['left'], right = kwargs['right'])
            else:
                super(BinTreeElement, self).__init__(e = kwargs['e'])
        else:
            super(BinTreeElement, self).__init__()
        if 'key' in kwargs:
            self._key = kwargs['key']

    def get_data_structure_type(self) -> str:
        """
        Get the data structure representation
        Returns:
            str
        """
        return "BinarySearchTree"

    @property
    def key(self) -> str:
        """
        Getter for the bst element key
        Returns:
            str: the key label
        """
        return self._key

    @key.setter
    def key(self, key: str) -> None:
        """
        Setter for the bst element key
        Args:
            key: the key for the element
        Returns:
            None
        """
        self._key = key

    @property
    def left(self):
        """
        Getter for the left element in BST
        Returns:
            BinTreeElement
        """
        return super(BSTElement, self).left

    @property
    def right(self):
        """
        Getter for the right element in BST
        Returns:
            BinTreeElement
        """
        return super(BSTElement, self).right
