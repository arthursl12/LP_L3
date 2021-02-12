import pytest
from heap import HeapManager, NULL

class Test1:
    def setup_method(self):
        self.h = HeapManager([0 for x in range(0, 10)])
    
    def test_full_frag(self):
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        assert self.h.memory == [2,-1,2,-1,2,-1,2,-1,2,-1]
    
    def test_allocation(self):
        assert self.h.memory == [10,-1,0,0,0,0,0,0,0,0]
        
        a = self.h.allocate (4)
        assert a == 1
        assert self.h.memory == [5,-1,0,0,0,5,-1,0,0,0]
        assert self.h.freeStart == 5
        
        b = self.h.allocate (2)
        assert b == 6
        assert self.h.memory == [5,-1,0,0,0,3,-1,0,2,-1]
        assert self.h.freeStart == 8
        
        c = self.h.allocate (1)
        assert c == 9
        assert self.h.memory == [5,-1,0,0,0,3,-1,0,2,-1]
        assert self.h.freeStart == NULL
    
    def test_minimum_size(self):
        with pytest.raises(Exception) as e_info:
            self.h = HeapManager([])
        with pytest.raises(Exception) as e_info:
            self.h = HeapManager([0])
        self.h = HeapManager([0,0])
        
            
        