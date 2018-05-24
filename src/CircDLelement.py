#!/usr/bin/env python
# package: bridges.base
from DLelement import *
##
#  @brief This class can be used to instantiate Circular Doubly Linked
#  List Elements.
#
#	Structurally they are the same as doubly linked elements
#  except that each node constructed with the next and the previous pointers
#	points to itself.
#
#  User's implementation of the circularly linked list needs to ensure that
#  the last node's next pointer points to the first node and the first node's
#	previous pointer points to the last node, as the visualization generation
#	is dependent on this.
#
#  Elements have labels (string) that are displayed on the visualization.
#  Elements take an generic object E as a user defined parameter, which can be
#	any native type or object.
#
#  Elements contain a visualizer (ElementVisualizer) object for setting visual
#	attributes (color, shape, opacity, size), necessary for displaying them in a web
#	browser.
#
#	Elements also have a LinkVisualizer object that is used when they are
#	linked to another element, appropriate for setting link attributes, between
#  the element and its previous or next nodes.
#
#  @author Kalpathi Subramanian
#
#	@date   7/17/16, 1/16/17
#
#  @param <E>  the generic parameter object that contains application specific data,
#		defined by the user when instantiating this object.
#
#	\sa Example Tutorial at <br>
#		http://bridgesuncc.github.io/Hello_World_Tutorials/CDLL.html
#
#
class CircDLelement(DLelement):
    ##
    #
    #	Constructs an empty CircDLelement with next and prev pointers set
    #	to itself
    #
    #
    def __init__(self, e = None, next = None, prev = None):
        if e is not None:
            super(CircDLelement, self).__init__()
        else:
            super(CircDLelement, self).__init__()
        self.next = next
        self.prev = prev


    ##
    #
    #	This method gets the data structure type
    #
    #	@return  The date structure type as a string
    #
    #
    def get_data_structure_type(self):
        return "CircularDoublyLinkedList"

    ##
    #
    # This method returns the pointer to the next DLelement
    #
    # @return the DLelement assigned to the next pointer
    #
    #
    def get_next(self):
        return self.next

    ##
    #
    # This method returns the pointer to the previous DLelement
    #
    # @return the DLelement assigned to the prev pointer
    #
    #
    def get_prev(self):
        return self.prev
