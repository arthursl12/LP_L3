import pytest
from heap_best import HeapManager, NULL

class TestDealloc2:
    def setup_method(self):
        self.h = HeapManager([0 for x in range(0, 10)])
    
    def test_full_frag(self):
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        self.h.allocate(1)
        # self.h.memory == [2,-1,2,-1,2,-1,2,-1,2,-1]
        
        self.h.deallocate(5)
        assert self.h.memory == [2,-1,2,-1,2,-1,2,-1,2,-1]
        assert self.h.freeStart == 4
        assert self.h.memory[4] == 2
        assert self.h.memory[5] == -1
        
        self.h.deallocate(1)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 2
        assert self.h.memory[1] == 4
        assert self.h.memory[4] == 2
        assert self.h.memory[5] == -1
        
        for i in range(2,10):
            with pytest.raises(Exception) as e_info:
                self.h.allocate(i)
        
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
        
        self.h.deallocate(9)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 2
        assert self.h.memory[1] == 4
        assert self.h.memory[4] == 2
        assert self.h.memory[5] == 8
        assert self.h.memory[8] == 2
        assert self.h.memory[9] == -1
        
        c = self.h.allocate(1)
        assert self.h.freeStart == 4
        assert self.h.memory[4] == 2
        assert self.h.memory[5] == 8
        assert self.h.memory[8] == 2
        assert self.h.memory[9] == -1
        
        c1 = self.h.allocate(1)
        assert self.h.freeStart == 8
        assert self.h.memory[8] == 2
        assert self.h.memory[9] == -1
        
        self.h.deallocate(c)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 2
        assert self.h.memory[1] == 8
        assert self.h.memory[8] == 2
        assert self.h.memory[9] == -1
        
        self.h.deallocate(c1)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 2
        assert self.h.memory[1] == 4
        assert self.h.memory[4] == 2
        assert self.h.memory[5] == 8
        assert self.h.memory[8] == 2
        assert self.h.memory[9] == -1
        
        for i in range(2,10):
            with pytest.raises(Exception) as e_info:
                self.h.allocate(i)
        
        self.h.deallocate(7)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 2
        assert self.h.memory[1] == 4
        assert self.h.memory[4] == 6
        assert self.h.memory[5] == -1
        
        c = self.h.allocate(1)
        assert self.h.freeStart == 4
        assert self.h.memory[4] == 6
        assert self.h.memory[5] == -1
        self.h.deallocate(c)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 2
        assert self.h.memory[1] == 4
        assert self.h.memory[4] == 6
        assert self.h.memory[5] == -1
        
        c = self.h.allocate(2)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 2
        assert self.h.memory[1] == 7
        assert self.h.memory[7] == 3
        assert self.h.memory[8] == -1
        self.h.deallocate(c)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 2
        assert self.h.memory[1] == 4
        assert self.h.memory[4] == 6
        assert self.h.memory[5] == -1
        
        c = self.h.allocate(4)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 2
        assert self.h.memory[1] == -1
        self.h.deallocate(c)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 2
        assert self.h.memory[1] == 4
        assert self.h.memory[4] == 6
        assert self.h.memory[5] == -1
        
        c = self.h.allocate(5)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 2
        assert self.h.memory[1] == -1
        self.h.deallocate(c)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 2
        assert self.h.memory[1] == 4
        assert self.h.memory[4] == 6
        assert self.h.memory[5] == -1
        
        for i in range(6,10):
            with pytest.raises(Exception) as e_info:
                self.h.allocate(i)
                
        c = self.h.deallocate(3)
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 10
        assert self.h.memory[1] == -1