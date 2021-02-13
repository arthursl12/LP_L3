NULL = -1 # The  null  link

class  HeapManager:
    """ Implements a very  simple  heap  manager."""
    def  __init__(self , initialMemory):
        """ Constructor. Parameter  initialMemory  is the  array of
        data  that we will use to  represent  the  memory."""
        self.memory = initialMemory
        self.memory[0] = self.memory.__len__()
        self.memory[1] = NULL
        self.freeStart = 0
    
    def findBlock(self,idx):
        for block in self.freePairs:
            if (idx == block[1]):
                return block
    
    def  allocate(self , requestSize):
        """ Allocates a block of data, and return its address. The parameter
        requestSize is the amount of space that must be allocated."""
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
        
        # Now:
        # p is the index of a block of sufficient size,
        # lag is the index of p’s predecessor in the free list, or NULL,
        # nextFree is the index of p’s successor in the free list, or NULL.
        
        # If the block has more space than we need, carve out what we need from 
        # the front and return the unused end part to the free list.
        unused = self.memory[p] - size
        if  unused > 1:
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
    
    def deallocate(self, addr):
        """
        Desaloca um bloco com endereço 'addr'. Esse endereço precisa ter sido
        fornecido pelo método 'allocate' e esse bloco não pode ter sido 
        desalocado previamente.
        
        Adaptado do método 'desallocate' do livro
	    """
        blockSize = addr - 1        # O tamanho real está no índice anterior
        realAddr = addr - 1         # O bloco começa de fato no índice anterior
     
        # Procura onde colocar ele na lista de blocos vazios
        p = self.freeStart
        lag = NULL
        while (p != NULL  and  p < realAddr):
            lag = p
            p = self.memory[p + 1]

        # Agora:
        # p: índice do bloco logo após o que queremos desalocar, ou NULL
        # lag: índice do bloco que vem antes do nosso na lista livre, ou NULL
        
		# If the one to come after ours is adjacent to it, merge it into ours and restore the property
		# described above.

        if (realAddr + self.memory[realAddr] == p):
            # Adicionar bloco à frente ao atual (que queremos desalocar) 
            self.memory[realAddr] = self.memory[realAddr] + self.memory[p]  # Soma os tamanhos
            p = self.memory[p+1]        

        if (lag == NULL):
            # Esse bloco recém-desalocado (junto com o da frente) 
            # é o primeiro livre
            self.freeStart = realAddr
            self.memory[realAddr+1] = p     
        else:
            if (lag + self.memory[lag] == realAddr):
                # Bloco livre anterior é adjacente, temos que fundi-lo também
                self.memory[lag] = self.memory[lag] + self.memory[realAddr] # Soma os tamanhos
                self.memory[lag+1] = p      
            else:
                # Nenhuma das opções, só uma inserção simples na lista de livres
                self.memory[lag+1] = realAddr
                self.memory[realAddr+1] = p

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
    
    h.deallocate(a)
    print("Memory = ", h.memory)
    h.deallocate(b)
    print("Memory = ", h.memory)
    
    c = h.allocate (7)
    print("Memory = ", h.memory)
    
test()