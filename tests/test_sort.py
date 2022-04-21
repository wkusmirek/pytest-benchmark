from src.sort import bubble_sort, merge_sort, insertion_sort

data = [83,97,22,55,53,12,8,57,1,60,62,74,40,26,45,86,49,89,25,69,61,48,87,95,23,78,35,47,37,85,96,32,7,10,90,43,67,27,3,91,84,31,5,50,82,71,68,4,92,38,41,11,65,17,99,24,88,9,76,59,21,66,93,70,15,30,29,98,20,64,33,14,51,13,58,18,16,19,28,75,56,72,54,6,77,46,100,34,80,52,73,81,94,42,79,36,2,63,39,44]

def test_bubble_sort_5(benchmark):
    benchmark.pedantic(bubble_sort, args=[[3,1,2,5,4]], rounds=20)

def test_merge_sort_5(benchmark):
    benchmark.pedantic(merge_sort, args=[[3,1,2,5,4]], rounds=20)

def test_insertion_sort_5(benchmark):
    benchmark.pedantic(insertion_sort, args=[[3,1,2,5,4]], rounds=20)


def test_bubble_sort_10(benchmark):
    benchmark.pedantic(bubble_sort, args=[[7,3,1,10,8,6,2,9,5,4]], rounds=20)

def test_merge_sort_10(benchmark):
    benchmark.pedantic(merge_sort, args=[[7,3,1,10,8,6,2,9,5,4]], rounds=20)

def test_insertion_sort_10(benchmark):
    benchmark.pedantic(insertion_sort, args=[[7,3,1,10,8,6,2,9,5,4]], rounds=20)
    
    
def test_bubble_sort_100(benchmark):
    benchmark.pedantic(bubble_sort, args=[data], rounds=20)

def test_merge_sort_100(benchmark):
    benchmark.pedantic(merge_sort, args=[data], rounds=20)

def test_insertion_sort_100(benchmark):
    benchmark.pedantic(insertion_sort, args=[data], rounds=20)
