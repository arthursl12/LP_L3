import pytest
from heap import HeapManager as FirstFit
from heap_best import HeapManager as BestFit

class TestComp1:
    def setup_method(self):
        self.bf = BestFit([0 for x in range(0, 7)])
        self.ff = FirstFit([0 for x in range(0, 7)])
        
    
    def test_bf_succ(self):
        h = self.bf
        a = h.allocate(2)
        b = h.allocate(1)
        c = h.allocate(1)
        
        h.deallocate(a)
        h.deallocate(c)
        
        d = h.allocate(1)
        e = h.allocate(2)
    
    def test_ff_fails(self):
        h = self.ff
        a = h.allocate(2)
        b = h.allocate(1)
        c = h.allocate(1)
        
        h.deallocate(a)
        h.deallocate(c)
        
        d = h.allocate(1)
        with pytest.raises(Exception) as e_info:
            e = h.allocate(2)

class TestComp2:
    def setup_method(self):
        self.bf = BestFit([0 for x in range(0, 11)])
        self.ff = FirstFit([0 for x in range(0, 11)])
        
    
    def test_bf_fails(self):
        h = self.bf
        a = h.allocate(4)
        b = h.allocate(1)
        c = h.allocate(3)
        
        h.deallocate(a)
        h.deallocate(c)
        
        d = h.allocate(1)
        e = h.allocate(2)
        with pytest.raises(Exception) as e_info:
            f = h.allocate(3)
        
    
    def test_ff_succ(self):
        h = self.ff
        a = h.allocate(4)
        b = h.allocate(1)
        c = h.allocate(3)
        
        h.deallocate(a)
        h.deallocate(c)
        
        d = h.allocate(1)
        e = h.allocate(2)
        f = h.allocate(3)