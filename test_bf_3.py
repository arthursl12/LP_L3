import pytest
from heap_best import HeapManager, NULL

class TestDealloc2:
    def setup_method(self):
        self.h = HeapManager([0 for x in range(0, 45)])
        self.a = self.h.allocate(6)
        self.b = self.h.allocate(1)
        self.c = self.h.allocate(4)
        self.d = self.h.allocate(1)
        self.e = self.h.allocate(2)
        self.f = self.h.allocate(1)
        
        self.h.deallocate(self.a)
        self.h.deallocate(self.c)
        self.h.deallocate(self.e)
        
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 7
        assert self.h.memory[1] == 9
        assert self.h.memory[9] == 5
        assert self.h.memory[10] == 16
        assert self.h.memory[16] == 3
        assert self.h.memory[17] == 21
        assert self.h.memory[21] == 24
        assert self.h.memory[22] == -1
    
    def test_4(self):
        g = self.h.allocate(4)
        assert self.c == g
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 7
        assert self.h.memory[1] == 16
        assert self.h.memory[16] == 3
        assert self.h.memory[17] == 21
        assert self.h.memory[21] == 24
        assert self.h.memory[22] == -1
    
    def test_3(self):
        g = self.h.allocate(3)
        assert self.c == g
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 7
        assert self.h.memory[1] == 16
        assert self.h.memory[16] == 3
        assert self.h.memory[17] == 21
        assert self.h.memory[21] == 24
        assert self.h.memory[22] == -1
    
    def test_2(self):
        g = self.h.allocate(2)
        assert self.e == g
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 7
        assert self.h.memory[1] == 9
        assert self.h.memory[9] == 5
        assert self.h.memory[10] == 21
        assert self.h.memory[21] == 24
        assert self.h.memory[22] == -1
        
    def test_1(self):
        g = self.h.allocate(1)
        assert self.e == g
        assert self.h.freeStart == 0
        assert self.h.memory[0] == 7
        assert self.h.memory[1] == 9
        assert self.h.memory[9] == 5
        assert self.h.memory[10] == 21
        assert self.h.memory[21] == 24
        assert self.h.memory[22] == -1