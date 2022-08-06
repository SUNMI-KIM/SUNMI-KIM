package ArrayLinearList;

public class ArrayLinearList {
	int N;
	int size;
	int increment;
	int[] itemList;
	
	public ArrayLinearList() {
		N = -1;
		size = 50;
		increment = 10;
		itemList = new int[size];
	}
	
	public boolean isEmpty() {
		return N == -1;
	}
	
	public void insert(int x) {
		int pos = 0;
		if(N == size - 1) {
			size += increment;
			itemList = new int[size];
		}
		if(N == -1) {
			N++;
			itemList[N] = x;
		}
		else {
			for(int i = 0; i<=N; i++) {
				if(x > itemList[i]) pos ++;
			}
			for(int i = N + 1; i>pos; i++) {
				itemList[i] = itemList[i-1];
			}
			itemList[pos] = x;
			N++;
		}
	}
	
	public void delete(int x) {
		if(isEmpty()) {
			System.out.println("List is Empty");
		}
		else {
			int loc = -1;
			for(int i = 0; i <= N; i++) {
				if(x == itemList[i]) loc = i;
			}
			if (loc == -1) System.out.println("삭제할 원소 " + x + " 가 없습니다.");
			else {
				for(int i = loc; i< N; i++) {
					itemList[i] = itemList[i+1];
				}
			}
		}
	}
	
	
	
	public static void main(String[] args) {

	}

}
