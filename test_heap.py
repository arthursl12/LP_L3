import pytest
from heap import HeapManager, NULL

class TestAllocation:
    def setup_method(self):
        self.h = HeapManager([0 for x in range(0, 10)])
    
    def test_full_frag(self):
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        assert self.h.memory == [2,-1,2,-1,2,-1,2,-1,2,-1]
    
    def test_allocation_1(self):
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
    
    def test_allocation_2(self):
        assert self.h.memory == [10,-1,0,0,0,0,0,0,0,0]
        
        a = self.h.allocate (1)
        assert a == 1
        assert self.h.memory == [2,-1,8,-1,0,0,0,0,0,0]
        assert self.h.freeStart == 2
        
        b = self.h.allocate (2)
        assert b == 3
        assert self.h.memory == [2,-1,3,-1,0,5,-1,0,0,0]
        assert self.h.freeStart == 5
        
        c = self.h.allocate (3)
        assert c == 6
        assert self.h.memory == [2,-1,3,-1,0,5,-1,0,0,0]
        assert self.h.freeStart == NULL
    
    def test_minimum_size(self):
        with pytest.raises(Exception) as e_info:
            self.h = HeapManager([])
        with pytest.raises(Exception) as e_info:
            self.h = HeapManager([0])
        self.h = HeapManager([0,0])
        
class TestDealloc:
    def setup_method(self):
        self.h = HeapManager([0 for x in range(0, 10)])
    
    def test_deallocation_empty(self):
        assert self.h.memory == [10,-1,0,0,0,0,0,0,0,0]
        assert self.freePairs == [(10,0)]
        self.h.deallocate(1)
        assert self.h.memory == [10,-1,0,0,0,0,0,0,0,0]
        assert self.freePairs == [(10,0)]
    
    def test_deallocation_basic(self):
        a = self.h.allocate (1)
        assert self.h.memory == [2,-1,8,-1,0,0,0,0,0,0]
        assert self.freePairs == [(8,2)]
        
        self.h.deallocate(a)
        assert self.h.memory == [10,-1,0,0,0,0,0,0,0,0]
        assert self.freePairs == [(10,0)]
    
    def test_deallocation_1(self):
        # self.h.memory == [10,-1,0,0,0,0,0,0,0,0]
        
        a = self.h.allocate (4)
        # self.h.memory == [5,-1,0,0,0,5,-1,0,0,0]
        
        b = self.h.allocate (2)
        # self.h.memory == [5,-1,0,0,0,3,-1,0,2,-1]
        
        c = self.h.allocate (1)
        # self.h.memory == [5,-1,0,0,0,3,-1,0,2,-1]
        assert self.h.freeStart == NULL
        assert self.freePairs == []
        
        self.h.deallocate(a)
        assert self.h.memory == [5,-1,0,0,0,3,-1,0,2,-1]
        assert self.freePairs == [(5,0)]
        
        self.h.deallocate(c)
        assert self.h.memory == [5,-1,0,0,0,3,-1,0,2,-1]
        assert self.freePairs == [(5,0),(2,8)]
        
        self.h.deallocate(b)
        assert self.h.memory == [10,-1,0,0,0,0,0,0,0,0]
        assert self.freePairs == [(10,0)]
    
    def test_full_refrag(self):
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        # self.h.memory == [2,-1,2,-1,2,-1,2,-1,2,-1]
        assert self.freePairs == []
        
        self.h.deallocate(5)
        assert self.h.memory == [2,-1,2,-1,2,-1,2,-1,2,-1]
        assert self.freePairs == [(4,2)]
        
        self.h.deallocate(1)
        assert self.h.memory == [2,-1,2,-1,2,-1,2,-1,2,-1]
        assert self.freePairs == [(2,0),(2,4)]
        
        self.h.deallocate(3)
        assert self.h.memory == [6,-1,0,0,0,0,2,-1,2,-1]
        assert self.freePairs == [(6,0)]
        
        self.h.deallocate(9)
        assert self.h.memory == [6,-1,0,0,0,0,2,-1,2,-1]
        assert self.freePairs == [(6,0),(2,8)]
        
        self.h.deallocate(9)
        assert self.h.memory == [6,-1,0,0,0,0,2,-1,2,-1]
        assert self.freePairs == [(6,0),(2,8)]
        
        self.h.deallocate(7)
        assert self.h.memory == [10,-1,0,0,0,0,0,0,0,0]
        assert self.freePairs == [(10,0)]
        
        
# TODO: Testes para freePairs
class TestFreePairs:
    def setup_method(self):
        self.h = HeapManager([0 for x in range(0, 10)])
    
    def test_full_frag(self):
        assert self.freePairs == [(10,0)]
        
        self.h.allocate(1)
        assert self.freePairs == [(8,2)]
        
        self.h.allocate(1)
        assert self.freePairs == [(6,4)]
        
        self.h.allocate(1)
        assert self.freePairs == [(4,6)]
        
        self.h.allocate(1)
        assert self.freePairs == [(2,8)]
        
        self.h.allocate(1)
        assert self.freePairs == []
        # self.h.memory == [2,-1,2,-1,2,-1,2,-1,2,-1]
    
    def test_allocation_1(self):
        assert self.h.memory == [10,-1,0,0,0,0,0,0,0,0]
        assert self.freePairs == [(10,0)]
        
        a = self.h.allocate (4)
        assert a == 1
        assert self.h.memory == [5,-1,0,0,0,5,-1,0,0,0]
        assert self.h.freeStart == 5
        assert self.freePairs == [(5,5)]
        
        b = self.h.allocate (2)
        assert b == 6
        assert self.h.memory == [5,-1,0,0,0,3,-1,0,2,-1]
        assert self.h.freeStart == 8
        assert self.freePairs == [(2,8)]
        
        c = self.h.allocate (1)
        assert c == 9
        assert self.h.memory == [5,-1,0,0,0,3,-1,0,2,-1]
        assert self.h.freeStart == NULL
        assert self.freePairs == []
    
    def test_allocation_2(self):
        assert self.h.memory == [10,-1,0,0,0,0,0,0,0,0]
        assert self.freePairs == [(10,0)]
        
        a = self.h.allocate (1)
        assert a == 1
        assert self.h.memory == [2,-1,8,-1,0,0,0,0,0,0]
        assert self.h.freeStart == 2
        assert self.freePairs == [(8,2)]
        
        b = self.h.allocate (2)
        assert b == 3
        assert self.h.memory == [2,-1,3,-1,0,5,-1,0,0,0]
        assert self.h.freeStart == 5
        assert self.freePairs == [(5,5)]
        
        c = self.h.allocate (3)
        assert c == 6
        assert self.h.memory == [2,-1,3,-1,0,5,-1,0,0,0]
        assert self.h.freeStart == NULL
        assert self.freePairs == []

# TODO: Testes com alloc e desalloc para fragmentar a memória
class TestFreePairs:
    def setup_method(self):
        self.h = HeapManager([0 for x in range(0, 10)])
    
    def test_full_frag(self):
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        # self.h.memory == [2,-1,2,-1,2,-1,2,-1,2,-1]
        assert self.freePairs == []
        
        self.h.deallocate(5)
        assert self.h.memory == [2,-1,2,-1,2,-1,2,-1,2,-1]
        assert self.freePairs == [(4,2)]
        
        self.h.deallocate(1)
        assert self.h.memory == [2,-1,2,-1,2,-1,2,-1,2,-1]
        assert self.freePairs == [(2,0),(2,4)]
        
        with pytest.raises(Exception) as e_info:
            self.h.allocate(3)
        
        self.h.deallocate(9)
        assert self.h.memory == [2,-1,2,-1,2,-1,2,-1,2,-1]
        assert self.freePairs == [(2,0),(2,4),(2,8)]
        
        with pytest.raises(Exception) as e_info:
            self.h.allocate(3)
        with pytest.raises(Exception) as e_info:
            self.h.allocate(4)
        with pytest.raises(Exception) as e_info:
            self.h.allocate(5)
        with pytest.raises(Exception) as e_info:
            self.h.allocate(6)
        
        self.h.deallocate(7)
        assert self.h.memory == [2,-1,2,-1,6,-1,0,0,0,0]
        assert self.freePairs == [(2,0),(6,4)]
        
        self.h.deallocate(self.h.allocate(3))
        self.h.deallocate(self.h.allocate(4))
        self.h.deallocate(self.h.allocate(5))
        with pytest.raises(Exception) as e_info:
            self.h.allocate(6)