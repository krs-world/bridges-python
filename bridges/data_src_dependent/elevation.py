
##
#    @brief  Class that holds elevation data
#    
#    Class that holds Elevation data. 
#   The data is stored as a 2d array .data of .cols columns and .rows rows.
#    The data at [0][0] are at location xll, yll and the spatial resolution 
#    is cellsize.
#    
#    @author Jay Strahler, Kalpathi Subramanian
#    
#    @date 3/28/20, 12/29/20
#    
#    

class ElevationData:
    ##
    # @brief Get data width
    #
    @property
    def cols(self):
        return self.ncols

    ##
    # @brief Set width of elevation data grid
    # @param ncols  elevation data width to set
    #
    @cols.setter
    def cols(self, ncols):
        self.ncols = ncols

    ##
    # @brief Get data height
    #
    @property
    def rows(self):
        return self.nrows

    ##
    # @brief Set height of elevation data grid
    # @param nrows  dlevation data height to set
    #
    @rows.setter
    def rows(self, nrows):
        self.nrows = nrows 

    ##
    # @brief Get elevation data
    #
    @property
    def data(self):
        return self._data

    ##
    # @brief Set elevation data
    # @param eledata  elevation data to set
    #
    @data.setter
    def data(self, eledata):
        self._data = eledata

    ##
    # @brief Get X coord of data origin
    #
    @property
    def xll(self):

    ##
    # @brief Set X coord of origin of  elevation data grid
    # @param value  lower left x coord of data
    #
    @xll.setter
    def xll(self, value):
        self._xll = value

    ##
    # @brief Get Y coord of data origin
    #
    @property
    def yll(self):
        return self._yll

    ##
    # @brief Set Y coord of origin of  elevation data grid
    # @param value  lower left y coord of data
    #
    @yll.setter
    def yll(self, value):
        self._yll = value

    ##
    # @brief Get data resolution (cell size)
    #
    @property
    def cellsize(self):
        return self._cellsize

    ##
    # @brief Set max elevation value in the data
    # @param value  cell size of this dataset
    #
    @cellsize.setter
    def cellsize(self, value):
        self._cellsize = value
    
    ##
    # @brief Get max elevation value in the data
    #
    @property
    def maxVal(self):
        return self._maxVal

    @maxVal.setter
    def maxVal(self, value):
        self._maxVal = value



    ##
    # @brief Constructor
    def __init__(self):
        self.ncols = 0
        self.nrows = 0
        self._data = []
        self._xll = 0
        self._yll = 0
        self._cellsize = 0
        self.name = None
        self._maxVal = 0
