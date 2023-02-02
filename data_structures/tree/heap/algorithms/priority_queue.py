from data_structures.tree.heap.min_heap import MinHeap


class PriorityQueue(MinHeap):
    def get_top_priority(self, _priority_array: list) -> int:
        """
        Gets current top priority

        :param _priority_array: priority array

        :returns priority
        """
        _priority = _priority_array[0]
        self.delete(_priority_array, data=_priority_array[0])
        return _priority


if __name__ == '__main__':
    # priority map
    priority_map = {
        1: 'Director',
        5: 'Senior',
        6: 'Junior',
        4: 'Lead',
        2: 'CEO'
    }

    # generate priority queue
    priority_array = []
    priority_queue = PriorityQueue()
    for priority in priority_map.keys():
        priority_queue.insert(priority_array, priority)

    # facilitate the priority queue according to the priority
    for _ in range(len(priority_map.keys())):
        priority = priority_queue.get_top_priority(priority_array)
        print(priority_map.get(priority))
