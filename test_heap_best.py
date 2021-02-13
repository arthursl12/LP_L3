import pytest
from heap_best import HeapManager, NULL
from filecmp import cmp

class TestAllocation:
    def setup_method(self):
        self.h = HeapManager([0 for x in range(0, 10)])
    
    def test_full_frag(self):
        self.h.allocate(1)
        assert self.h.freeStart == 2
        assert self.h.memory[2] == 8
        
        self.h.allocate(1)
        assert self.h.freeStart == 4
        assert self.h.memory[4] == 6
        
        self.h.allocate(1)
        assert self.h.freeStart == 6
        assert self.h.memory[6] == 4
        
        self.h.allocate(1)
        assert self.h.freeStart == 8
        assert self.h.memory[8] == 2
        
        self.h.allocate(1)
        assert self.h.freeStart == NULL
        assert self.h.memory == [2,-1,2,-1,2,-1,2,-1,2,-1]
    
    def test_allocation_1(self):
        assert self.h.memory == [10,-1,0,0,0,0,0,0,0,0]
        
        a = self.h.allocate (4)
        assert a == 1
        assert self.h.memory == [5,-1,0,0,0,5,-1,0,0,0]
        assert self.h.freeStart == 5
        assert self.h.memory[5] == 5
        
        b = self.h.allocate (2)
        assert b == 6
        assert self.h.memory == [5,-1,0,0,0,3,-1,0,2,-1]
        assert self.h.freeStart == 8
        assert self.h.memory[8] == 2
        
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
        assert self.h.memory[2] == 8
        
        b = self.h.allocate (2)
        assert b == 3
        assert self.h.memory == [2,-1,3,-1,0,5,-1,0,0,0]
        assert self.h.freeStart == 5
        assert self.h.memory[5] == 5
        
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
        
class TestDeallocBasic:
    def setup_method(self):
        self.h = HeapManager([0 for x in range(0, 10)])
    
    def test_deallocation_empty(self):
        assert self.h.memory == [10,-1,0,0,0,0,0,0,0,0]
        assert self.h.freeStart == 0

        a = self.h.allocate(9)
        assert self.h.memory == [10,-1,0,0,0,0,0,0,0,0]
        assert self.h.freeStart == NULL
        
        self.h.deallocate(a)
        assert self.h.memory == [10,-1,0,0,0,0,0,0,0,0]
        assert self.h.freeStart == 0
    
    def test_deallocation_basic(self):
        a = self.h.allocate (1)
        assert self.h.memory == [2,-1,8,-1,0,0,0,0,0,0]
        assert self.h.freeStart == 2
        
        self.h.deallocate(a)
        a = self.h.allocate (9)
        assert self.h.freeStart == NULL
        
        self.h.deallocate(a)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 10
    
class TestArquivosIguais:
    def test_compara(self):
        assert cmp('heap_best.py','6.py',shallow=True)