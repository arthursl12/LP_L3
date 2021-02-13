import pytest
from heap import HeapManager, NULL

class TestDealloc1:
    def setup_method(self):
        self.h = HeapManager([0 for x in range(0, 10)])
    
    def test_deallocation_1(self):        
        a = self.h.allocate (4)
        assert self.h.freeStart == 5
        assert self.h.memory[5] == 5
        assert self.h.memory[6] == -1
        
        b = self.h.allocate (2)
        assert self.h.freeStart == 8
        assert self.h.memory[8] == 2
        assert self.h.memory[9] == -1
        
        c1 = self.h.allocate (1)
        assert self.h.freeStart == NULL
        
        self.h.deallocate(a)
        assert self.h.memory == [5,-1,0,0,0,3,-1,0,2,-1]
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 5
        assert self.h.memory[1] == -1
        
        for i in range(5,10):
            with pytest.raises(Exception) as e_info:
                self.h.allocate(i)
        a = self.h.allocate(4)
        assert self.h.freeStart == NULL
        self.h.deallocate(a)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 5
        assert self.h.memory[1] == -1
        
        self.h.deallocate(c1)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 5
        assert self.h.memory[1] == 8
        assert self.h.memory[8] == 2
        assert self.h.memory[9] == -1
        
        for i in range(5,10):
            with pytest.raises(Exception) as e_info:
                self.h.allocate(i)
        c = self.h.allocate(1)
        assert c == c1
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 5
        self.h.deallocate(c)
        
        c2 = self.h.allocate(2)
        assert c2 != c
        assert self.h.freeStart == 3
        assert self.h.memory[3] == 2
        assert self.h.memory[4] == 8
        assert self.h.memory[8] == 2
        assert self.h.memory[9] == -1
        self.h.deallocate(c2)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 5
        assert self.h.memory[1] == 8
        assert self.h.memory[8] == 2
        assert self.h.memory[9] == -1

        self.h.deallocate(b)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 10
        
        d = self.h.allocate(9)
        assert self.h.freeStart == NULL
    
    def test_full_refrag(self):
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        # self.h.memory == [2,-1,2,-1,2,-1,2,-1,2,-1]
        
        self.h.deallocate(5)
        for i in range(2,10):
            with pytest.raises(Exception) as e_info:
                self.h.allocate(i)
        assert self.h.freeStart == 4
        assert self.h.memory[4] == 2
        assert self.h.memory[5] == -1
        
        
        self.h.deallocate(1)
        for i in range(2,10):
            with pytest.raises(Exception) as e_info:
                self.h.allocate(i)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 2
        assert self.h.memory[1] == 4
        assert self.h.memory[4] == 2
        assert self.h.memory[5] == -1
        
        c = self.h.allocate(1)
        assert self.h.freeStart == 4
        assert self.h.memory[4] == 2
        assert self.h.memory[5] == -1
        self.h.deallocate(c)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 2
        assert self.h.memory[1] == 4
        assert self.h.memory[4] == 2
        assert self.h.memory[5] == -1
        
        self.h.deallocate(3)
        # assert self.h.memory == [6,-1,0,0,0,0,2,-1,2,-1]
        # assert self.h.freePairs == [(6,0)]
        for i in range(6,10):
            with pytest.raises(Exception) as e_info:
                self.h.allocate(i)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 6
        
        t = self.h.allocate(5)
        assert self.h.freeStart == NULL
        self.h.deallocate(t)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 6
        
        t = self.h.allocate(4)
        assert self.h.freeStart == NULL
        self.h.deallocate(t)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 6
        
        t = self.h.allocate(3)
        assert self.h.freeStart == 4
        assert self.h.memory[4] == 2
        self.h.deallocate(t)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 6
        
        self.h.deallocate(9)
        # assert self.h.memory == [6,-1,0,0,0,0,2,-1,2,-1]
        # assert self.h.freePairs == [(6,0),(2,8)]
        for i in range(6,10):
            with pytest.raises(Exception) as e_info:
                self.h.allocate(i)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 6
        assert self.h.memory[1] == 8
        assert self.h.memory[8] == 2
        
        t = self.h.allocate(1)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 6
        assert self.h.memory[1] == -1
        self.h.deallocate(t)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 6
        assert self.h.memory[1] == 8
        assert self.h.memory[8] == 2
        
        self.h.deallocate(7)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 10
        
        c = self.h.allocate(9)
        assert self.h.freeStart == NULL
        self.h.deallocate(c)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 10
