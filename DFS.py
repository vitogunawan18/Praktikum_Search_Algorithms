# Python3 program to print DFS traversal
# dari sebuah graf yang diberikan
from collections import defaultdict

# Kelas ini merepresentasikan sebuah graf yang diarahkan
# menggunakan representasi daftar kejadian
class Graph:

    # Konstruktor
    def __init__(self):

        # Kamus default untuk menyimpan graf
        self.graph = defaultdict(list)

    # Fungsi untuk menambahkan tepi ke graf
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Fungsi yang digunakan oleh DFS
    def DFSUtil(self, v, visited):

        # Tandai node saat ini sebagai sudah dikunjungi
        # dan cetak
        visited.add(v)
        print(v, end=' ')

        # Panggil rekursif untuk semua titik ujung
        # yang berdekatan dengan titik ini
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # Fungsi untuk melakukan penelusuran DFS. Ini menggunakan
    # DFSUtil() rekursif
    def DFS(self, v): # Indent this function definition to make it a method of the Graph class

        # Buat himpunan untuk menyimpan node yang sudah dikunjungi
        visited = set()

        # Panggil fungsi bantu rekursif
        # untuk mencetak penelusuran DFS
        self.DFSUtil(v, visited)

# Kode pengguna
if __name__ == "__main__":
    g = Graph()
    g.addEdge('A', 'B')
    g.addEdge('A', 'C')
    g.addEdge('B', 'C')
    g.addEdge('C', 'A')
    g.addEdge('C', 'D')
    g.addEdge('D', 'D')

    print("Berikut adalah Penelusuran Depth First (dimulai dari node C)")
    g.DFS('C')