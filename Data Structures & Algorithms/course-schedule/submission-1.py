from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for course,prereq in prerequisites:
            adj_list[course].append(prereq)

        visited = set()
        curr_path = set()

        def has_cycle(curr_course: int) -> bool:
            visited.add(curr_course)
            curr_path.add(curr_course)

            for neighbor in adj_list[curr_course]:
                if (neighbor in curr_path) or (neighbor not in visited and has_cycle(neighbor)):
                    return True
            curr_path.remove(curr_course)
            return False

        for i in range(numCourses):
            if not i in visited:
                if has_cycle(i):
                    return False
        return True

        
        
        
       


        