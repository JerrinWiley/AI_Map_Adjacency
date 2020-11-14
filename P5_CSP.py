import pandas


# Loosely based on backtracking code from geeksforgeeks.com
class Graph:
    # class properties to record graph information
    def __init__(self, vertices):
        self.V = vertices
        self.nva = 0
        self.graph = [[0 for column in range(vertices)]\
                              for row in range(vertices)]

    # returns NVA count
    def get_nva(self):
        return self.nva

    # is safe for vertex v
    def is_safe(self, v, color, c):
        for ind in range(self.V):
            if self.graph[v][ind] == 1 and color[ind] == c:
                return False
        return True

    # Checks if adjacent countries are the same color
    def graph_coloring(self, m, color, v):
        # Checks if all vertices are accounted for
        if v == self.V:
            return True

        for c in range(1, m+1):
            self.nva += 1
            if self.is_safe(v, color, c):
                color[v] = c
                if self.graph_coloring(m, color, v + 1):
                    return True
                color[v] = 0

    def graph_solver(self, m):
        color = [0] * self.V
        if self.graph_coloring(m, color, 0) is None:
            print('No Solution')
            return []

        # Print the solution
        # print("Solution exist and Following are the assigned colours:")
        row = []
        for c in color:
            row.append(c)
        return row


def csp_map_solver(filename):
    map_data = pandas.read_excel(filename)
    colors = [0, 'Red', 'Green', 'Blue', 'Yellow']
    graph1 = []
    names = list(map_data.columns)
    names.pop(0)

    for i in range(map_data.shape[0]):
        temp_list = list(map_data.iloc[i])
        temp_list.pop(0)
        graph1.append(temp_list)

    max_colors = 4
    h = Graph(len(graph1))
    h.graph = graph1
    answer = h.graph_solver(max_colors)
    # print(answer)
    min_colors = max(answer)

    for j in range(len(answer)):
        answer[j] = colors[answer[j]]
    territory_colors = dict(zip(names, answer))
    # print(answer)

    print_answer = 'NVA = %s\nNumber of colors needed: %s\n' % (h.get_nva(), min_colors)
    for k in range(len(graph1)):
        adjacent_count = 1
        sub_answer = '%s:%s -> {' % (names[k], territory_colors.get(names[k]))
        for l in range(len(graph1)):
            if graph1[k][l] == 1:
                if adjacent_count == 1:
                    sub_answer += '%s:%s' % (names[l], territory_colors.get(names[l]))
                else:
                    sub_answer += ', %s:%s' % (names[l], territory_colors.get(names[l]))
                adjacent_count += 1

        sub_answer += '}'
        print_answer += sub_answer + '\n'

    return print_answer


name = ['adjacency_matrix_Aust.xlsx', 'adjacency_matrix_US.xlsx', 'adjacency_matrix_India.xlsx']
for ind in name:
    ans = csp_map_solver(ind)
    write_file = ind
    file_name = ''
    write_file.split()
    for l in range(len(write_file)-5):
        file_name += write_file[l]
    file_name += '_report.txt'
    with open(file_name, 'w') as text_file:
        text_file.write(ans)
        text_file.close
