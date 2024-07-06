class Graph:
    def __init__(self, file: str):
        self.file = file
        self.data = {}

        self.load()

    def load(self):
        with open(self.file) as f:
            for line in f:
                letter, *row = line.split()

                if letter == 'p':
                    self.v = int(row[1])
                    self.e = int(row[2])
                elif letter == 'e':
                    vertex = int(row[0])
                    neighbor = int(row[1])

                    if vertex not in self.data:
                        self.data[vertex] = []
                    self.data[vertex].append(neighbor)
                    
if __name__ == "__main__":
    graph = Graph('graph.txt')
    print(graph.data)
        
        