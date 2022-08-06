package Heap;

public class maxHeap {
	int[] heap;
	int n = 0;
	int size;
	
	boolean isFull() {
		if (heap.length == n) {
			return true;
		}
		return false;
	}
	
	boolean isEmpty() {
		if(n == 0) {
			return true;
		}
		return false;
	}
	
	void Creation(int size) {
		this.size = size;
		heap = new int[size];
	}
	
	void insert(int item) {
		int ptr;
		if(isFull()) {throw new RuntimeException("Full");}
		ptr = ++n;
		while((ptr != 1) && (item > heap[ptr/2])) {
			heap[ptr] = heap[ptr/2];
			ptr /= 2;
		}
		heap[ptr] = item;
	}
	
	int remove() {
		int parent; 
		int child; 
		int item; 
		int temp;
		if(isEmpty()) {throw new RuntimeException("Empty"); }
		item = heap[1];
		temp = heap[n--];
		parent = 1;
		child = 2;
		while(child <= n) {
			if(child < n && (heap[child] < heap[child+1])) {
				child++;
			}
			if(temp >= heap[child]) break;
			heap[parent] = heap[child];
			child *= 2;
		}
		heap[parent] = temp;
		return item;
	}
	void removeOutput() {
		while(n > 0) {
			System.out.print(remove());
			System.out.print(" ");
		}
	}
	
	
	public static void main(String[] args) {
		maxHeap mh = new maxHeap();
		mh.Creation(20);
		mh.insert(23);
		mh.insert(39);
		mh.insert(7);
		mh.insert(20);
		mh.insert(14);
		mh.insert(15);
		mh.insert(46);
		mh.insert(66);
		mh.insert(75);
		mh.insert(49);
		mh.insert(32);
		mh.removeOutput();

	}

}
