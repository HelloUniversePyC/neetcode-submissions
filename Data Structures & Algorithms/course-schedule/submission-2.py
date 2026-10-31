from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        in_degree = [0]*numCourses

        for course,prereq in prerequisites:
            adj_list[course].append(prereq)
            in_degree[prereq]+=1
        
        q = deque(i for i in range(numCourses) if in_degree[i] == 0)

        order = []

        while q:
            curr_course = q.popleft()
            order.append(curr_course)
            for neighbor in adj_list[curr_course]:
                in_degree[neighbor]-=1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        return len(order) == numCourses
      

        
        
        
       


        