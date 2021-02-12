NULL = -1 # The  null  link

class  HeapManager:
    """ Implements a very  simple  heap  manager."""
    def  __init__(self , initialMemory):
        """ Constructor. Parameter  initialMemory  is the  array of
        data  that we will use to  represent  the  memory."""
        self.memory = initialMemory
        self.memory [0] = self.memory.__len__()
        self.memory [1] = NULL
        self.freeStart = 0
    
    def  allocate(self , requestSize):
        """ Allocates a block of data , and  return  its  address. Theparameter
        requestSize  is the  amount  of space  that  must be  allocaed."""
        size = requestSize + 1
        # Do first-fit  search: linear  search  of the  free  list  for
        # the  first  block of  sufficient  size.
        p = self.freeStart
        lag = NULL
        while p != NULL  and  self.memory[p] < size:
            lag = p
            p = self.memory[p + 1]
        if p == NULL:
            raise  MemoryError ()
        nextFree = self.memory[p + 1]
        # Now p is the  index of a block  of  sufficient  size ,
        # lag is the  index of p’s predecessor  in the
        # free list , or NULL , and  nextFree  is the  index  of
        # p’s successor  in the  free list , or NULL.
        # If the  block  has  more  space  than we need , carve
        # out  what we need  from  the  front  and  return  the
        # unused  end  part to the  free  list.
        unused = self.memory[p] - size
        if  unused  > 1:
            # Se tiver mais de uma posição livre
            nextFree = p + size
            self.memory[nextFree] = unused
            self.memory[nextFree + 1] = self.memory[p + 1]
            self.memory[p] = size
        if lag == NULL:
            self.freeStart = nextFree
        else:
            self.memory[lag + 1] = nextFree
        return p + 1
    def deallocate(addr):
        """
        
        """
        pass
    
"""
Bloco ocupa n+1 posições: a primeira diz o tamanho do bloco
Bloco mínimo (1) ocupa 2 posições, por isso na hora de marcar o próximo bloco
livre, temos que garantir que haja pelo menos dois espaços na memória
"""
def  test():
    h = HeapManager ([0 for x in range(0, 10)])
    print("Memory = ", h.memory)
    a = h.allocate (4)
    print("a = ", a, ", Memory = ", h.memory)
    b = h.allocate (2)
    
    # b = h.allocate (2)
    print("b = ", b, ", Memory = ", h.memory)
    
test()