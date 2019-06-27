#!/usr/bin/env python
from bridges.element import *

##
# @brief This class can be used to create arrays of type Element<E>.
#
# @author 	Matthew McQuaigue
#
# @date  	10/8/16, 6/09/19
#
#	This class can be used to create arrays of type Element<E>  where E
#	is a generic object representing application specific data.
#
#	Arrays are internally represented as 1D arrays; currently 1D, 2D  and
#	3D arrays are supported.
#
#
#
class Array():
    dims = [1,1,1] #used for setting size of array based on dimensions
    def __init__(self, num_dims, **kwargs):
        """
        Array constructor
        Args:
            num_dims: The dimensions of the array (1-3). Defaults to 1 dimension (int)
        Kwargs:
            dims: size of each dimension (array)
            x_dim: number of elements on the x dimension (int)
            y_dim: number of elements on the y dimension (int)
            z_dim: number of elements on the z dimension (int)
        Returns:
            None
        """
        self._array_data = []
        self._num_dims = num_dims
        self._dims = [1, 1, 1]
        if kwargs:
            if 'dims' in kwargs:
                self._set_dimensions(kwargs['dims'])
                self._dims = kwargs['dims']
            else:
                self._dims[0] = self._dims[1] = self._dims [2] = self._size = 0
            if 'x_dim' in kwargs and num_dims >= 1:
                self._dims[0] = kwargs['x_dim']
            if 'y_dim' in kwargs and num_dims >= 2:
                self._dims[1] = kwargs['y_dim']
            if 'z_dim' in kwargs and num_dims == 3:
                self._dims[2] = kwargs['z_dim']

    @property
    def num_dims(self) -> int:
        """
        Getter for representing the number of dimensions in the array
        Returns:
            int: number of dimensions
        """
        return self._num_dims

    @num_dims.setter
    def num_dims(self, value: int) -> None:
        """
        Setter function for the number of dimensions for the array
        Args:
            value: An integer for the number of dimensions (Between 1 and 3 inclusive)
        Returns:
            None
        Raises:
            ValueError: if dimension passed in is < 1 or > 3
        """
        if value > 3:
            raise ValueError("Invalid number of dimensions. Only 1D, 2D and 3D arrays supported at this time")
        self._num_dims = value

    @property
    def size(self) -> int:
        """
        Getter for representing the size of array
        Returns:
            int: the size
        """
        return self._size

    @size.setter
    def size(self, sz: int) -> None:
        """
        Setter for representing the size of the array
        Args:
            (int) sz: The size to be set for array
        Returns:
            None
        """
        self._size = sz

    def _get_data_structure_type(self) -> str:
        """
        Gets the data structure type
        Raises:
            ValueError: if number of dimenstions is < 1 or > 3
        Returns:
            str: type of data structure
        """
        if (self.num_dims >= 1) and (self.num_dims <= 3):
            return "Array"
        else:
            raise ValueError("Invalid number of dimensions. Only 1D, 2D and 3D arrays supported at this time")

    def _set_dimensions(self, dim: list) -> None:
        """
        Sets the size of each dimension and allocates array space
        Args:
            (list) dim: size of each dimension in array
        Returns:
             None
        """
        sz = 1
        k = 0
        while k < self.num_dims:
            Array.dims[k] = dim[k]
            sz = sz * dim[k]
            k += 1
        #  first check the dimensions are all positive
        if sz < 0:
            raise ValueError("Invalid dimension value, must be  positive")
        self.size = sz
        #  allocate space for the array with elements
        k = 0
        while k < self.size:
            self._array_data.append(Element())
            k += 1

    def get_element(self, **kwargs):
        """
        Getter function for an element in the array at given position
        Kwargs:
            (int) index: the index of array to get in array
            (int) x: column index into array
            (int) y: row index into array
            (int) z: slice index into array
        Returns:
            Element: the element at position given
        """
        if 'index' in kwargs:
            return self._array_data[kwargs['index']]
        if 'x' in kwargs and 'y' in kwargs:
            if 'z' in kwargs:
                return self._array_data[
                    kwargs['z'] * self._dims[0] * self._dims[1] + kwargs['y'] * self._dims[0] + kwargs['x']]
            else:
                return self._array_data[kwargs['y'] * self._dims[1] + kwargs['x']]

    def set_element(self, el: Element, **kwargs):
        """
        Setter function for an element in the array at given position
        Args:
            (Element) el: element object to be assigned to index
        Kwargs:
            (int) index: the index of array to get in array
            (int) x: column index into array
            (int) y: row index into array
            (int) z: slice index into array
        Returns:
            None
        """
        if 'index' in kwargs:
            self._array_data[kwargs['index']] = el
        if 'x' in kwargs and 'y' in kwargs:
            if 'z' in kwargs:
                self._array_data[kwargs['z']*self._dims[0]*self._dims[1] + kwargs['y']*self._dims[0] + kwargs['x']] = el
            else:
                self._array_data[kwargs['y']*self._dims[1]+ kwargs['x']] = el

    def _get_data_structure_representation(self) -> dict:
        """
        Generating the JSON string for a bridges array object
        Returns:
            dict: the dict that will represent the json when dumped
        """
        nodes_json = dict()
        #add json representation for each element to dict
        i = 0
        while i < self.size:
            if self._array_data[i] is not None:
                nodes_json.update(self._array_data[i]._get_element_representation())
            i += 1
        json_dict = {
            "nodes": [nodes_json]
        }
        return json_dict
